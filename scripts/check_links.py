"""Check that source links resolve. On a pull request only the records it changes are checked.

    python3 scripts/check_links.py --base origin/main   # links in records changed since origin/main
    python3 scripts/check_links.py --all                # every link (slow)

A link that is gone (404, 410, the domain doesn't exist) is an error. Sites that block scripts
(401, 403, 429), server errors and timeouts are warnings: a reviewer opens those by hand.
"""
import argparse
import concurrent.futures
import json
import os
import ssl
import subprocess
import sys
import urllib.error
import urllib.request

from common import DATA, ROOT, read_json

ap = argparse.ArgumentParser()
g = ap.add_mutually_exclusive_group(required=True)
g.add_argument('--base', help='git ref to diff against, e.g. origin/main')
g.add_argument('--all', action='store_true')
args = ap.parse_args()

if args.all:
    files = [os.path.join(dp, f) for dp, _, fs in os.walk(DATA) for f in fs if f.endswith('.json')]
else:
    out = subprocess.run(['git', '-C', ROOT, 'diff', '--name-only', '--diff-filter=AM', f'{args.base}...HEAD', '--', 'data'],
                         capture_output=True, text=True, check=True).stdout.split()
    files = [os.path.join(ROOT, f) for f in out if f.endswith('.json')]


def urls_in(o, found):
    if isinstance(o, dict):
        if isinstance(o.get('url'), str):
            found.add(o['url'])
        if o.get('type') in ('contact-form', 'website') and isinstance(o.get('value'), str):
            found.add(o['value'])
        for v in o.values():
            urls_in(v, found)
    elif isinstance(o, list):
        for v in o:
            urls_in(v, found)
    return found


where = {}
for f in files:
    for u in urls_in(read_json(f), set()):
        where.setdefault(u, []).append(os.path.relpath(f, ROOT))

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36 '
      '(Beyond-The-Jersey link check; https://github.com/Beyond-The-Jersey/data)')
CTX = ssl.create_default_context()


def check(url):
    last = None
    for method in ('HEAD', 'GET'):
        try:
            req = urllib.request.Request(url, method=method, headers={'User-Agent': UA, 'Accept': '*/*'})
            return url, urllib.request.urlopen(req, timeout=20, context=CTX).status
        except urllib.error.HTTPError as e:
            last = e.code
            if method == 'HEAD':
                continue  # many servers refuse HEAD; try GET before judging
            return url, e.code
        except urllib.error.URLError as e:
            last = 'no-such-host' if 'Name or service not known' in str(e.reason) or 'nodename' in str(e.reason) else type(e.reason).__name__
        except Exception as e:  # timeouts, TLS errors
            last = type(e).__name__
    return url, last


errors, warnings = [], []
with concurrent.futures.ThreadPoolExecutor(16) as ex:
    for url, status in ex.map(check, sorted(where)):
        if isinstance(status, int) and status < 400:
            continue
        line = f'{url} → {status} (in {", ".join(where[url])})'
        (errors if status in (404, 410, 'no-such-host') else warnings).append(line)

for w in warnings:
    print('warning:', w)
for e in errors:
    print('error:', e)
print(f'{len(where)} links checked in {len(files)} files: {len(errors)} gone, {len(warnings)} to open by hand.')
sys.exit(1 if errors else 0)
