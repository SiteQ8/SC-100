# SC-100

**Microsoft Cybersecurity Architect**
Course material for the delivery beginning 14 September 2026.

[Open the companion](https://siteq8.github.io/SC-100/) · [Official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)

---

## What this is

Teaching material built from the skills measured **as of 28 July 2026**, checked
against the official study guide on 8 September 2026. Four domains, 14 topics,
16 timed sessions across four days, and 48 reference links that are fetched on
every build.

## Read this before using any other SC-100 material

At the time this was written, several widely read study sites still describe a
domain called **Design a Zero Trust strategy and architecture (30 to 35%)**.

That domain no longer exists. The current blueprint is:

| Domain | Weight |
| --- | --- |
| Design solutions that align with security best practices and priorities | 20 to 25% |
| Design security operations, identity, and compliance capabilities | 25 to 30% |
| Design security solutions for infrastructure | 25 to 30% |
| Design security solutions for applications and data | 20 to 25% |

Zero Trust is now taught inside the first domain as a lens rather than as a
third of the exam. A course built from the older sources spends a day on a
weighting that is gone and misses what replaced it.

## What changed in 2026

Eleven items entered or grew in the recent revisions and are flagged in the
material, because a course written from older material is silently out of date
on exactly these points. The largest are agent identity through Entra Agent ID,
secure AI adoption as a named strategy objective, AI workload data security,
Copilot data controls, Security Exposure Management, and the rewrite of the
network objective around Security Service Edge.

## What is checked on every build

**Links.** Microsoft Learn reorganises constantly and a deck full of dead URLs
is embarrassing in front of a room. Every reference is fetched, and a link that
has moved is followed and recorded at its new address.

**Agenda coverage.** Every session names the objective ids it teaches, and the
build fails if a session references an objective that does not exist, or if any
objective has no session. The delivery plan cannot silently drift from the
blueprint.

**Reading coverage.** A topic with no verified reading leaves a student nowhere
to go after the session, so that is a fault too.

**Both languages.** Every topic carries its guidance in English and Arabic, and
the build fails if one is missing.

## A deliberate choice about language

Topic titles, framing and the note on where students go wrong exist in both
languages. The teaching points stay in English on purpose. The exam is in
English, the product names are in English, and translating a term like
Conditional Access would harm a student in the room rather than help them.

## Rebuilding

```
python3 scripts/build.py        verify links and blueprint integrity
python3 scripts/build_site.py   rebuild the companion page
```

Use `--strict` on the first to fail on any unusable link. A daily workflow runs
both, so a link that dies between now and delivery is caught rather than found
live.

## Structure

```
data/objectives.py   the blueprint, with what changed and where students trip
data/agenda.py       the four day plan, proportioned to exam weight
data/links.txt       reference links, one per objective id
scripts/build.py     verification and assembly
```

## Licence

MIT for the course material. Exam objectives belong to Microsoft and the
authoritative list is the study guide linked above, which students should be
sent to rather than to any paraphrase.
