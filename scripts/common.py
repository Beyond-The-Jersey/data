"""Shared helpers: load the records in data/, and the rating rule (METHOD.md).

Standard library only, so contributors and agents can run the scripts with a plain python3.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
SCHEMA = os.path.join(ROOT, 'schema')

# folder in data/ -> (schema file, key field)
TYPES = {
    'sports': ('sport', 'id'),
    'leagues': ('league', 'id'),
    'clubs': ('club', 'id'),
    'owners': ('owner', 'id'),
    'claims': ('claim', 'id'),
    'sponsors': ('sponsor', 'id'),
    'kits': ('kit', 'id'),
    'deals': ('deal', 'id'),
    'changes': ('change', 'id'),
    'dropped': ('dropped', 'id'),
    'contacts': ('contact', 'clubId'),
}
# The dataset the website and other consumers read: one array per type, plus these.
BUNDLE = ['meta', 'levels', 'tiers'] + list(TYPES)


def read_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load():
    """{type: {key: record}}, plus levels, tiers and order, and {type: {key: path}} for messages."""
    records, paths = {}, {}
    for folder, (_, key) in TYPES.items():
        records[folder], paths[folder] = {}, {}
        d = os.path.join(DATA, folder)
        for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            if not name.endswith('.json'):
                continue
            p = os.path.join(d, name)
            rec = read_json(p)
            records[folder][rec.get(key) if isinstance(rec, dict) else name[:-5]] = rec
            paths[folder][rec.get(key) if isinstance(rec, dict) else name[:-5]] = os.path.relpath(p, ROOT)
    records['levels'] = read_json(os.path.join(DATA, 'levels.json'))
    records['tiers'] = read_json(os.path.join(DATA, 'tiers.json'))
    records['order'] = read_json(os.path.join(DATA, 'order.json'))
    return records, paths


# ------------------------------------------------------------------ the rating rule (METHOD.md)

TIER_SCORE = {'unrated': None, 'none': 0, 'concern': 1, 'serious': 2, 'severe': 3}
LEVEL_ORDER = ['soaked', 'stained', 'spotted', 'clean', 'not-rated']


def kit_level(kit, tier_of):
    """A shirt's blood level from its sponsors' tiers and placements. Mirrors the website's lib/data/rating.ts."""
    if kit.get('levelOverride'):
        return kit['levelOverride']
    xs = [(p['placement'], TIER_SCORE[tier_of(p['sponsorId'])]) for p in kit['sponsors']]
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


def kit_end(k):
    return k.get('periodTo') or k.get('season') or k.get('periodFrom') or ''


def current_kits(kits):
    """The latest home kit per club."""
    out = {}
    for k in kits.values():
        if k['kitType'] == 'home' and (k['clubId'] not in out or kit_end(k) >= kit_end(out[k['clubId']])):
            out[k['clubId']] = k
    return out


def owner_chain(owners, owner_id):
    out = []
    while owner_id and owner_id in owners and owner_id not in out:
        out.append(owner_id)
        owner_id = owners[owner_id].get('parentId')
    return out


SEASON = re.compile(r'^\d{4}-\d{2}$')
YEAR = re.compile(r'^\d{4}$')
PLACEHOLDER_URL = re.compile(r'^https?://(www\.)?(example\.(com|org|net)|localhost)\b', re.I)
PLACEHOLDER_TEXT = re.compile(r'X{3,}|\.\.\.|lorem ipsum', re.I)
