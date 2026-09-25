"""Turn the US-league research batches into pipeline records.

Reads /tmp/ingest_b*_out.json (patch sponsor + arena naming rights per club) and writes
/tmp/data/us_ingest.py, which build_normalized.py merges the same way it merges
research_additions.

Modelling, as agreed: a jersey patch is a sponsor ON the jersey kit (placement "patch"),
an arena naming-rights deal is a DEAL (placement "stadium"), and the venue name goes in the
deal note so it is not lost.
"""
import json
import os
import re
import sys

OUT = "/tmp/data/us_ingest.py"
BATCHES = ["/tmp/ingest_b%d_out.json" % i for i in range(1, 7)]


def slug(s):
    s = (s or "").lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def main():
    seen_owner, seen_sponsor, seen_kit, seen_deal = {}, {}, {}, {}
    owners, sponsors, kits, deals, claims = [], [], [], [], []
    unresolved = []
    n = 0

    for path in BATCHES:
        if not os.path.exists(path):
            continue
        try:
            data = json.load(open(path))
        except Exception as e:
            print("  %s unreadable: %s" % (os.path.basename(path), e))
            continue
        for row in data.get("clubs", []):
            n += 1
            cid = row.get("clubId")
            if not cid:
                continue

            def ensure_org(entry, kind, club):
                """Create-or-reuse the owner + sponsor for one researched organisation."""
                org = (entry or {}).get("orgName")
                if not org:
                    return None
                hint = slug(entry.get("sponsorIdHint") or org)
                oid = hint + "-owner"
                if hint not in seen_sponsor:
                    if oid not in seen_owner:
                        seen_owner[oid] = {
                            "id": oid, "name": org, "type": "unknown",
                            "parentId": None, "note": "%s of %s (2026-27)." % (kind, club),
                        }
                        owners.append(seen_owner[oid])
                    seen_sponsor[hint] = {
                        "id": hint, "name": org, "ownerId": oid, "ownership": "owned",
                        "tier": "unrated", "status": "unrated", "verdict": None,
                        "claimIds": [], "aliases": [], "note": None,
                    }
                    sponsors.append(seen_sponsor[hint])
                # one documented claim per sponsor so the rating pass has something to attach to
                cl_id = "%s-2026" % hint
                if cl_id not in {c["id"] for c in claims}:
                    src = entry.get("source") or {}
                    claims.append({
                        "id": cl_id, "ownerIds": [oid],
                        "text": "%s is the %s of %s for 2026-27." % (org, kind, club),
                        "short": "%s %s 2026-27" % (kind.capitalize(), org),
                        "source": {"name": src.get("name") or "see url",
                                   "date": src.get("date") or "2026-01-01",
                                   "url": src.get("url")},
                        "reviewed": False,
                    })
                return hint

            club = row.get("clubId")
            patch = ensure_org(row.get("patch"), "jersey patch partner", club)
            arena = ensure_org(row.get("arena"), "arena naming-rights holder", club)

            if patch:
                kid = "%s-2026-27-home" % cid
                if kid not in seen_kit:
                    seen_kit[kid] = {
                        "id": kid, "clubId": cid, "season": "2026-27", "kitType": "home",
                        "periodLabel": "2026/27", "periodFrom": "2026-27", "periodTo": "2026-27",
                        "photos": {},
                        "sponsors": [{"sponsorId": patch, "placement": "patch"}],
                        "sponsorsComplete": True,
                        "summary": "Jersey patch: %s." % (row["patch"].get("orgName")),
                        "change": None,
                    }
                    kits.append(seen_kit[kid])
                start = (row["patch"].get("since") or "2026").strip()[:4]
                did = "%s-%s-patch" % (cid, patch)
                if did not in seen_deal:
                    src = row["patch"].get("source") or {}
                    seen_deal[did] = {
                        "id": did, "clubId": cid, "orgName": row["patch"].get("orgName"),
                        "sponsorId": patch, "placement": "patch",
                        "from": start, "to": None, "value": None,
                        "source": {"name": src.get("name") or "see url",
                                   "date": src.get("date") or "2026-01-01",
                                   "url": src.get("url")},
                        "note": "Jersey patch.",
                    }
                    deals.append(seen_deal[did])

            if arena:
                did = "%s-%s-stadium" % (cid, arena)
                if did not in seen_deal:
                    src = row["arena"].get("source") or {}
                    venue = row["arena"].get("venueName")
                    seen_deal[did] = {
                        "id": did, "clubId": cid, "orgName": row["arena"].get("orgName"),
                        "sponsorId": arena, "placement": "stadium",
                        "from": "2026", "to": None, "value": None,
                        "source": {"name": src.get("name") or "see url",
                                   "date": src.get("date") or "2026-01-01",
                                   "url": src.get("url")},
                        "note": ("Arena naming rights: %s." % venue) if venue else "Arena naming rights.",
                    }
                    deals.append(seen_deal[did])

            if not patch and not arena:
                unresolved.append(cid)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write('"""US league patch and arena records, generated by make_us_ingest.py."""\n\n')
        for name, val in (("NEW_OWNERS", owners), ("NEW_SPONSORS", sponsors),
                          ("NEW_KITS", kits), ("NEW_DEALS", deals), ("EXTRA_CLAIMS", claims)):
            f.write("%s = " % name)
            f.write(json.dumps(val, indent=4, ensure_ascii=False))
            f.write("\n\n")

    print("clubs read %d | owners %d sponsors %d kits %d deals %d claims %d"
          % (n, len(owners), len(sponsors), len(kits), len(deals), len(claims)))
    if unresolved:
        print("no patch and no arena (%d): %s" % (len(unresolved), ", ".join(unresolved)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
