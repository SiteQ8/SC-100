#!/usr/bin/env python3
"""Verify non GitHub resources by fetching them.

The GitHub half of this catalogue is verified through an API that answers
honestly. The open web does not. A link can be dead, quietly moved, parked by a
squatter, or perfectly alive but refusing an automated request, and treating all
four the same would either drop good resources or publish dead ones.

So the classification is deliberate:

  ok          answered normally
  moved       answered, but from a different host than the one we asked for
  blocked     refused the automated request, which says nothing about the site
  down        the server answered with a fault of its own, so it is broken now
              rather than gone, and may well be fine tomorrow
  dead        answered that the page does not exist
  unreachable no answer at all

Only dead and unreachable are treated as failures. Blocked and down resources
are kept and labelled, because Cloudflare turning away a script is not evidence
that a training platform has shut down, and a certificate search returning a
gateway error on a bad afternoon is not evidence that it has closed. Pretending
otherwise would quietly delete the most used services in the catalogue.
"""

import concurrent.futures
import ssl
import urllib.error
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")
TIMEOUT = 20

CTX = ssl.create_default_context()


def host(url):
    return urllib.parse.urlparse(url).netloc.lower().removeprefix("www.")


def check(url):
    """Fetch a URL and report what actually happened."""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=CTX) as r:
            final = r.geturl()
            state = "moved" if host(final) != host(url) else "ok"
            return {"state": state, "status": r.status, "final": final}
    except urllib.error.HTTPError as e:
        # A bot filter refusing a script says nothing about the resource.
        if e.code in (401, 403, 405, 406, 429):
            return {"state": "blocked", "status": e.code, "final": url}
        # A server fault means broken today, not gone. Keep it and say so.
        if e.code >= 500:
            return {"state": "down", "status": e.code, "final": url}
        return {"state": "dead", "status": e.code, "final": url}
    except Exception as e:
        return {"state": "unreachable", "status": 0, "final": url,
                "error": type(e).__name__}


def check_all(urls, workers=8):
    out = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(check, u): u for u in urls}
        for f in concurrent.futures.as_completed(futures):
            out[futures[f]] = f.result()
    return out


if __name__ == "__main__":
    import json
    import sys
    print(json.dumps(check_all(sys.argv[1:]), indent=2))
