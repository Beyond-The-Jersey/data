"""One-off migration (25 Sep 2026): normalized/*.json -> data/<type>/<id>.json, one file per record.

It also fixes what can be fixed without new research (issue #279) and writes every change to
docs/migration-2026-09-25.md. Run once from the repo root:

    python3 scripts/migrate_2026_09_25.py --website <path to Beyond-The-Jersey/website>

The website path is only used to know which shirt images exist (public/assets/shirts). This script
is removed after the migration; it stays in the git history.
"""
import argparse
import collections
import json
import os
import re
import shutil

OD = collections.OrderedDict
FILES = ['sports', 'leagues', 'clubs', 'owners', 'claims', 'sponsors', 'kits', 'deals', 'changes', 'dropped', 'contacts']
KEY = {'contacts': 'clubId'}
TODAY = '2026-09-25'

ap = argparse.ArgumentParser()
ap.add_argument('--website', required=True)
args = ap.parse_args()

load = lambda n: json.load(open(f'normalized/{n}.json', encoding='utf-8'), object_pairs_hook=OD)
d = {n: load(n) for n in FILES}
levels, tiers = load('levels'), load('tiers')
log = collections.defaultdict(list)


def by_id(n):
    return {x[KEY.get(n, 'id')]: x for x in d[n]}


# ------------------------------------------------------------ 1. seasons
SEASON = re.compile(r'^(\d{4})-(\d{2})$')
for k in d['kits']:
    m = SEASON.match(k.get('season') or '')
    if not m:
        continue
    start, end = m.group(1), str(int(m.group(1)) + 1)
    fixed = []
    if k.get('periodFrom') == start:
        k['periodFrom'] = k['season']; fixed.append('periodFrom')
    if k.get('periodTo') in (end, start):
        k['periodTo'] = k['season']; fixed.append('periodTo')
    if fixed:
        log['Seasons written YYYY-YY'].append(f"kits/{k['id']}: {' and '.join(fixed)} → {k['season']}")

# ------------------------------------------------------------ 2. invented claims
PLACEHOLDER = re.compile(r'^https?://(www\.)?example\.(com|org|net)\b', re.I)
guessed = {c['id'] for c in d['claims']
           if not c.get('source') or PLACEHOLDER.match(c['source'].get('url') or '')
           or re.match(r'inference', c['source'].get('name') or '', re.I)}
d['claims'] = [c for c in d['claims'] if c['id'] not in guessed]
for c in sorted(guessed):
    log['Invented claims removed ("Inference based on company name", example.com)'].append(f'claims/{c}')
dropped_owner_refs = set()
for s in d['sponsors']:
    before = list(s['claimIds'])
    s['claimIds'] = [c for c in s['claimIds'] if c not in guessed]
    if s['claimIds'] == before or s['claimIds'] or s['tier'] == 'unrated':
        continue
    log['Sponsors back to unrated (their rating rested on an invented claim)'].append(
        f"sponsors/{s['id']}: was {s['tier']} ({s.get('verdict')}); owner {s.get('ownerId')} dropped")
    if s.get('ownerId'):
        dropped_owner_refs.add(s['ownerId'])
    s.update(tier='unrated', status='unrated', verdict=None, ownerId=None, ownership=None)
    s['note'] = ((s.get('note') or '') + f' Rating removed {TODAY}: its only claim was an invented ownership record (#279).').strip()
# "<Sponsor> is the <role> of <club> for 2026-27" claims restate a deal or a kit sponsor that is
# already a record, cite a stub owner, and no sponsor cites them. They are not evidence: drop them.
DEAL_FACT = re.compile(r'^(?P<sp>.+?) is the (?P<role>.+?) (?:of|for) (?P<club>[a-z0-9-]+)(?: for| in) (?P<season>[0-9-]+)\.?$')
cited = {i for s in d['sponsors'] for i in s['claimIds']} | {
    i for s in d['sponsors'] if s.get('why') for i in s['why']['claimIds']}
pairs = {(x['clubId'], x['sponsorId']) for x in d['deals']} | {
    (k['clubId'], p['sponsorId']) for k in d['kits'] for p in k['sponsors']}
sponsor_ids = {s['id'] for s in d['sponsors']}
for c in list(d['claims']):
    m = DEAL_FACT.match(c['text'])
    sid = c['id'][:-5] if c['id'].endswith('-2026') else None
    if c['id'] not in cited and m and sid in sponsor_ids and (m.group('club'), sid) in pairs:
        d['claims'].remove(c)
        log['Claims that only restated a deal removed (the deal or kit record stays)'].append(f"claims/{c['id']}: {c['text']}")

# Owners nothing points to any more (the invented "<Company> LLC" stubs among them).
while True:
    used = {s.get('ownerId') for s in d['sponsors']} | {o.get('parentId') for o in d['owners']} | {
        o for c in d['claims'] for o in c['ownerIds']}
    orphans = [o for o in d['owners'] if o['id'] not in used]
    if not orphans:
        break
    for o in orphans:
        d['owners'].remove(o)
        why = 'invented stub' if o['id'] in dropped_owner_refs else 'no sponsor or claim refers to it'
        log['Owners nothing refers to removed'].append(f"owners/{o['id']} ({o['name']}): {why}")

# ------------------------------------------------------------ 3. rating commentary in claims
COMMENTARY = {
    'gov-saudi-arabia-record': (
        "The Saudi state's documented record (a record 345 executions in 2024; drug-offence executions continuing "
        "through 2026) makes this serious - severe is reserved for live armed conflict.",
        "The Saudi state's documented record includes a record 345 executions in 2024 and drug-offence executions "
        "continuing through 2026."),
    'pif-record': (
        ", so it carries the same Saudi state money as Aramco and the same serious rating.", "."),
    'gov-qatar-record': (
        "Qatar's documented record - migrant workers still exposed to exploitation despite kafala reform, expression "
        "and assembly tightly restricted - rates serious.",
        "Qatar's documented record: migrant workers still exposed to exploitation despite kafala reform, and "
        "expression and assembly tightly restricted."),
    'state-of-qatar-qia-record': (
        " The F1 global partnership is therefore effectively Gulf state money, which the method places at 'serious' "
        "absent live armed conflict.", ""),
    'gov-malaysia-record': (" is documented, so serious rather than concern.", " is documented."),
    'mubadala-record': (
        " - UAE state money, rated serious on the UAE's upheld unfair mass-trial convictions.",
        ". The UAE's courts have upheld the convictions from an unfair mass trial."),
}
claims = by_id('claims')
for cid, (old, new) in COMMENTARY.items():
    c = claims.get(cid)
    if c and old in c['text']:
        c['text'] = c['text'].replace(old, new)
        if c.get('short') and old in c['short']:
            c['short'] = c['short'].replace(old, new)
        log['Rating commentary removed from claims (facts kept)'].append(f'claims/{cid}: "{old.strip()}"')
    else:
        log['Commentary edits not applied (text differs)'].append(f'claims/{cid}')

# ------------------------------------------------------------ 4. dead and private links
DEAD = json.load(open(os.path.join(args.website, 'data', 'live-overlay.json')))['deadUrls']
DEAD = {u: r for u, r in DEAD.items() if not u.startswith('_')}


def unlink(o, where):
    if isinstance(o, list):
        for x in o:
            unlink(x, where)
    elif isinstance(o, dict):
        if isinstance(o.get('url'), str) and o['url'] in DEAD:
            log['Dead or private links removed (the source stays)'].append(f"{where}: {o['url']}")
            o['note'] = ((o.get('note') or '') + f" Link removed {TODAY} ({DEAD[o['url']]}): {o['url']}").strip()
            o['url'] = None
        for v in o.values():
            unlink(v, where)


for n in ['claims', 'deals', 'kits', 'changes', 'dropped', 'leagues']:
    for x in d[n]:
        unlink(x, f"{n}/{x['id']}")
for c in d['contacts']:
    keep = []
    for ch in c['channels']:
        if ch.get('value') in DEAD or (ch.get('source') or {}).get('url') in DEAD:
            log['Dead or private links removed (the source stays)'].append(f"contacts/{c['clubId']}: {ch['type']} {ch['value']}")
        else:
            keep.append(ch)
    c['channels'] = keep

# ------------------------------------------------------------ 5. deal start dates older than their source
for x in d['deals']:
    s = x.get('source') or {}
    f = x.get('from') or ''
    m = re.match(r'^(\d{4})', s.get('date') or '')
    if f and m and int(m.group(1)) <= int(f[:4]) - 2:
        log['Deal start dates cleared (the source is years older than the start)'].append(
            f"deals/{x['id']}: from {f}, source {s['date']}")
        x['note'] = ((x.get('note') or '') + f" Start date unknown: the record said {f} (the season it was recorded), its source is from {s['date']}.").strip()
        x['from'] = None

# ------------------------------------------------------------ 6. kit images the website doesn't have
shirts = set()
for root, _, files in os.walk(os.path.join(args.website, 'public', 'assets', 'shirts')):
    for f in files:
        shirts.add(os.path.relpath(os.path.join(root, f), os.path.join(args.website, 'public')))
for k in d['kits']:
    for side, p in list(k['photos'].items()):
        if p not in shirts:
            del k['photos'][side]
            log['Kit image references removed (Wikipedia kit templates, dropped from the website)'].append(f"kits/{k['id']}: {side}")

# ------------------------------------------------------------ 7. league status follows coverage
TIER_SCORE = {'unrated': None, 'none': 0, 'concern': 1, 'serious': 2, 'severe': 3}
tier = {s['id']: s['tier'] for s in d['sponsors']}


def level(kit):
    if kit.get('levelOverride'):
        return kit['levelOverride']
    xs = [(p['placement'], TIER_SCORE[tier.get(p['sponsorId'], 'unrated')]) for p in kit['sponsors']]
    rated = [(pl, sc) for pl, sc in xs if sc is not None]
    if not rated:
        return 'not-rated'
    if any(sc == 3 and pl == 'front' for pl, sc in rated) or sum(sc >= 2 for _, sc in rated) >= 2:
        return 'soaked'
    if any(sc == 2 and pl == 'front' for pl, sc in rated) or any(sc == 3 and pl != 'front' for pl, sc in rated):
        return 'stained'
    if any(sc >= 1 for _, sc in rated):
        return 'spotted'
    return 'clean' if len(rated) == len(xs) and kit['sponsorsComplete'] else 'not-rated'


end = lambda k: k.get('periodTo') or k.get('season') or k.get('periodFrom') or ''
current = {}
for k in d['kits']:
    if k['kitType'] == 'home' and (k['clubId'] not in current or end(k) >= end(current[k['clubId']])):
        current[k['clubId']] = k
for lg in d['leagues']:
    ids = [c['id'] for c in d['clubs'] if c['leagueId'] == lg['id']]
    n = sum(1 for c in ids if c in current and level(current[c]) != 'not-rated')
    total = lg.get('clubCount') or len(ids)
    st = 'not-started' if n == 0 else 'complete' if n >= total else 'partial'
    if st != lg['status']:
        log['League status set from coverage'].append(f"leagues/{lg['id']}: {lg['status']} → {st} ({n} of {total} rated)")
        lg['status'] = st

# ------------------------------------------------------------ write
if os.path.exists('data'):
    shutil.rmtree('data')
for n in FILES:
    os.makedirs(f'data/{n}', exist_ok=True)
    for x in d[n]:
        with open(f"data/{n}/{x[KEY.get(n, 'id')]}.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
for n, v in [('levels', levels), ('tiers', tiers)]:
    with open(f'data/{n}.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
# The order the website shows sports and leagues in (tabs, league rows). Everything else is by id.
with open('data/order.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(OD([('sports', [s['id'] for s in d['sports']]), ('leagues', [l['id'] for l in d['leagues']])]),
                       ensure_ascii=False, indent=2) + '\n')

os.makedirs('docs', exist_ok=True)
with open('docs/migration-2026-09-25.md', 'w', encoding='utf-8') as f:
    f.write('# Migration, 25 Sep 2026: one file per record\n\n')
    f.write('`normalized/*.json` (at `5a8f8e1`) was split into `data/<type>/<id>.json` by '
            '`scripts/migrate_2026_09_25.py` (see the git history). On the way it fixed what needs no new research '
            'from issue #279. Everything else is unchanged.\n\n')
    f.write('| Records | Count |\n|---|---|\n')
    for n in FILES:
        f.write(f'| {n} | {len(d[n])} |\n')
    f.write('\n')
    for section, items in log.items():
        f.write(f'## {section} ({len(items)})\n\n')
        f.writelines(f'- {i}\n' for i in items)
        f.write('\n')
print({n: len(d[n]) for n in FILES})
print({k: len(v) for k, v in log.items()})
