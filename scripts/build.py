#!/usr/bin/env python3
"""Assemble the course dataset and verify everything it points at.

Two things go wrong with course material. Links rot, because Microsoft Learn
reorganises constantly and a deck full of dead URLs is embarrassing in front of
a room. And the agenda drifts from the objectives, so a day is spent on
something the exam no longer weights.

Both are checked here rather than trusted. Every link is fetched. Every session
must name topics that exist, and every objective topic must be taught by some
session, so nothing on the exam is silently missing from the delivery.
"""

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "data"))
sys.path.insert(0, str(ROOT / "scripts"))
from objectives import DOMAINS, NEW_IN_2026, SOURCE  # noqa: E402
from agenda import AGENDA, COHORTS, COURSE, RHYTHM  # noqa: E402
from webcheck import check_all  # noqa: E402

OUT = ROOT / "data" / "course.json"

# Microsoft revised SC-100 twice in 2026, in July and again in October, so a
# quarter is the longest the blueprint can go unverified before the build stops.
STALE_WARN_DAYS = 45
STALE_AFTER_DAYS = 90
LINKS = ROOT / "data" / "links.txt"


def main():
    strict = "--strict" in sys.argv
    faults = []

    topics = {}
    for d in DOMAINS:
        for t in d["topics"]:
            if t["id"] in topics:
                faults.append(f"duplicate topic id {t['id']}")
            topics[t["id"]] = dict(t, domain=d["id"])

    # Every flagged 2026 change must attach to a topic that exists, otherwise
    # the warning is about something the course does not actually teach.
    for label, labelAr, tid, why, whyAr in NEW_IN_2026:
        if tid not in topics:
            faults.append(f"2026 change '{label}' points at unknown topic {tid}")
        if not labelAr or not whyAr:
            faults.append(f"2026 change '{label}' has no Arabic")

    # A cohort is a promise to a specific room, so its dates are checked rather
    # than trusted: real ISO dates, in order, spanning the four teaching days.
    for c in COHORTS:
        try:
            a, b = date.fromisoformat(c["from"]), date.fromisoformat(c["to"])
        except (KeyError, ValueError):
            faults.append(f"cohort '{c.get('label', '?')}' has unreadable dates")
            continue
        span = (b - a).days + 1
        if span != COURSE["days"]:
            faults.append(
                f"cohort '{c['label']}' spans {span} days, course is {COURSE['days']}")
        if not c.get("labelAr"):
            faults.append(f"cohort '{c['label']}' has no Arabic label")

    # The agenda and the objective map must agree in both directions.
    taught = set()
    for day in AGENDA:
        for s in day["sessions"]:
            for tid in s["topics"]:
                if tid not in topics:
                    faults.append(f"day {day['day']} session {s['slot']} teaches unknown topic {tid}")
                taught.add(tid)
    untaught = sorted(set(topics) - taught)
    if untaught:
        faults.append(f"objectives with no session: {untaught}")

    # Resources, verified by fetching.
    pairs = []
    for line in LINKS.read_text(encoding="utf-8").strip().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        tid, url = line.split("|", 1)
        if tid not in topics:
            faults.append(f"resource attached to unknown topic {tid}: {url}")
        pairs.append((tid, url.strip()))

    print(f"verifying {len(pairs)} links")
    results = check_all([u for _, u in pairs], workers=8)
    resources, dead = [], []
    for tid, url in pairs:
        r = results[url]
        if r["state"] in ("dead", "unreachable"):
            dead.append(f"{tid}  {r['state']} {r.get('status')}  {url}")
            continue
        resources.append({
            "topic": tid, "url": r["final"], "requested": url,
            "state": r["state"], "status": r["status"],
            "title": url.rstrip("/").split("/")[-1].replace("-", " "),
        })
    states = {}
    for r in resources:
        states[r["state"]] = states.get(r["state"], 0) + 1
    print(f"  {len(resources)} usable, {len(dead)} unusable, states {states}")
    if dead:
        print("\nunusable links:", *dead, sep="\n  ", file=sys.stderr)
        faults.extend(dead)

    # A topic with no reading leaves a student nowhere to go after the session.
    bare = sorted(t for t in topics if not any(r["topic"] == t for r in resources))
    if bare:
        faults.append(f"topics with no verified reading: {bare}")

    if faults:
        print(f"\n{len(faults)} fault(s):", *faults, sep="\n  ", file=sys.stderr)
        if strict or any("unknown" in f or "no session" in f for f in faults):
            sys.exit(1)

    taught_in = {}
    for day in AGENDA:
        for s in day["sessions"]:
            for tid in s["topics"]:
                taught_in.setdefault(tid, []).append(
                    {"day": day["day"], "slot": s["slot"]})
    for d in DOMAINS:
        for tp in d["topics"]:
            tp["taught"] = taught_in.get(tp["id"], [])

    # Which objectives changed in the 2026 revisions, so the badge can sit on the
    # objective rather than in a tab of its own.
    changed = {}
    for label, labelAr, tid, why, whyAr in NEW_IN_2026:
        changed.setdefault(tid, []).append(
            {"label": label, "labelAr": labelAr, "why": why, "whyAr": whyAr})
    for d in DOMAINS:
        for tp in d["topics"]:
            tp["changed"] = changed.get(tp["id"], [])

    # This repository's whole claim is that it tracks the current blueprint.
    # Nothing enforced that, and it sat seven weeks stale with a product name
    # Microsoft had since renamed. The check is now part of the build.
    stale = (date.today() - date.fromisoformat(SOURCE["checked"])).days
    if stale > STALE_AFTER_DAYS:
        print(f"\nBlueprint last verified {stale} days ago against the study guide at",
              file=sys.stderr)
        print(f"  {SOURCE['url']}", file=sys.stderr)
        print("Re-read it, update skills_measured_as_of and checked in data/objectives.py,",
              file=sys.stderr)
        print("then rebuild. Microsoft revises these without notice.", file=sys.stderr)
        sys.exit(1)
    if stale > STALE_WARN_DAYS:
        print(f"  blueprint verified {stale} days ago, re-check soon")

    # A student taught before the blueprint moved was taught against a map
    # Microsoft has since revised, and that is the one thing they most need to
    # know on arriving here, so the page is told which cohorts those were.
    cohorts = [dict(c, revised=c["to"] < SOURCE["skills_measured_as_of"])
               for c in COHORTS]

    course = {
        "course": COURSE,
        "source": SOURCE,
        "built": date.today().isoformat(),
        "cohorts": cohorts,
        "rhythm": [{"from": a, "to": b, "label": c} for a, b, c in RHYTHM],
        "domains": DOMAINS,
        "new_in_2026": [{"label": l, "labelAr": la, "topic": t, "why": w, "whyAr": wa}
                        for l, la, t, w, wa in NEW_IN_2026],
        "agenda": AGENDA,
        "resources": resources,
        "counts": {
            "domains": len(DOMAINS),
            "topics": len(topics),
            "sessions": sum(len(d["sessions"]) for d in AGENDA),
            "resources": len(resources),
            "new_items": len(NEW_IN_2026),
            "cohorts": len(cohorts),
        },
    }
    OUT.write_text(json.dumps(course, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    c = course["counts"]
    print(f"\ncourse.json  {c['domains']} domains, {c['topics']} topics, "
          f"{c['sessions']} sessions, {c['resources']} verified links")
    print(f"  skills measured as of {SOURCE['skills_measured_as_of']}, checked {SOURCE['checked']}")
    stale_cohorts = [c["label"] for c in cohorts if c["revised"]]
    print(f"  {len(cohorts)} cohort(s) taught" +
          (f", blueprint revised since: {', '.join(stale_cohorts)}" if stale_cohorts else ""))


if __name__ == "__main__":
    main()
