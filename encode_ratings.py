"""Turn the researched ratings into a Python module the builder can consume.

Reads /tmp/ratings.json (produced by a research pass) and writes ratings_data.py.
A few ratings are adjusted here, with the reason recorded alongside the research
note so the reviewer can see the join between research and judgement.

    python3 encode_ratings.py            # re-encode from the research outputs in /tmp
    python3 encode_ratings.py --reapply  # re-apply HOLD and CLAIM_TEXT_FIX to the committed
                                         # ratings_data.py (when the /tmp outputs are gone)

The rating rule (tiers.json; README "Rating rule"):
- serious means owned by a state or state fund *with documented serious abuses*;
  severe means paid for by a state directly tied to ongoing severe abuses. Both
  need a sourced claim of those abuses by a state in the sponsor's owner chain.
- State ownership alone is not a tier. A public owner (a US state university, a
  county tourism board, an Italian region, Swiss cantons) with no such claim is
  held at 'unrated' until a person reviews it: the owner and the evidence stay,
  the builder marks the sponsor 'being-rated'.
- A minority state stake is a lesser link: concern at most, and only with a
  sourced poor record for that state.
- Claim texts state facts from their source. Rating commentary ("State ownership
  alone earns serious", "Human-rights relevance is remote") belongs in the note.
"""
import json
import os
import pprint
import re

SRC = ["/tmp/ratings.json", "/tmp/ratings2.json",
       "/tmp/rate_batch_1_out.json", "/tmp/rate_batch_2_out.json",
       "/tmp/rate_batch_3_out.json",
       "/tmp/rate_us_1_out.json", "/tmp/rate_us_2_out.json",
       "/tmp/rate_us_3_out.json", "/tmp/rate_us_4_out.json",
       "/tmp/rate_us_5_out.json", "/tmp/rate_us_6_out.json", "/tmp/rate_us_7_out.json"]
OUT = "/tmp/data/ratings_data.py"

# sponsorId -> ownership on the shirt's owner chain
PART_OWNED = {"turkish-airlines", "deutsche-telekom", "lbbw"}

# Judgement calls layered on top of the research, never instead of it.
# SC: two multi-hundred-million-dollar forfeitures over four decades of working
# around Iran/Sudan sanctions is a sustained structural adverse record, not a
# one-off fine -> concern under tiers.json's "a lesser link".
# Uralkali: no state stake, but the ultimate owner sits in a belligerent state
# and was itself sanctioned -> concern.
OVERRIDE = {
    # an earlier pass rated this none and called the parent "privately held conglomerate";
    # it shares the hyundai chain (HMC holds 35.17% of Kia) and the same NPS stake, so the
    # two records disagreed on identical evidence. Set explicitly so order cannot win.
    "kia-america": (
        "concern",
        "same chain as hyundai - Hyundai Motor Company holds 35.17% of Kia and the NPS 7.76% stake sits behind it",
    ),
    "standard-chartered": (
        "concern",
        "Raised from none: the 2012 and 2019 forfeitures are a sustained structural "
        "record, not a one-off fine, which is what tiers.json calls 'a lesser link'.",
    ),
    "uralkali": (
        "concern",
        "Raised from none: no state stake, but the ultimate owner sits inside a "
        "belligerent state and was sanctioned with it.",
    ),
}


# Ratings held back under the rule above: tier 'unrated', owner and evidence kept, the
# reason recorded in the note. Remove an entry once a person has reviewed the sponsor.
PUBLIC_ONLY = "public ownership, but no sourced claim of abuses by that owner, which serious needs"
HOLD = {
    "childrens-health": PUBLIC_ONLY + "; the sponsor also covers a private non-profit (Children's Health)",
    "md-anderson-cancer-center": PUBLIC_ONLY,
    "io-sono-friuli-venezia-giulia": PUBLIC_ONLY,
    "sardegna-turismo": PUBLIC_ONLY,
    "pulsee-luce-e-gas": PUBLIC_ONLY,
    "experience-kissimmee": PUBLIC_ONLY,
    "lvcva": PUBLIC_ONLY,
    "ucla-health": PUBLIC_ONLY,
    "uw-health": PUBLIC_ONLY,
    "eni": "a 33% Italian state stake, no sourced claim of abuses by that owner, and the "
           "conflict-exposure sentence had no source",
    "prometeon": "the only claim is about Pirelli's shareholder, not about Prometeon's own ownership",
    "pirelli": "a minority state stake (about 20%): concern at most under tiers.json",
    "mercedes-benz": "minority state stakes (BAIC 9.98%, KIA 5.33%): concern at most under tiers.json",
}

# Rating commentary inside claim texts, which the cited sources don't say. Exact text.
CLAIM_TEXT_FIX = {
    "childrens-health": [(" State ownership of one half of the patch drives a state tier. Human-rights relevance "
                          "is limited to public-sector healthcare and labour policy.", "")],
    "eni": [(" State ownership alone earns serious. Eni's upstream operations in Libya, Egypt, Nigeria and "
             "Mozambique give it live, conflict-adjacent human-rights exposure on top.", "")],
    "experience-kissimmee": [(" Because the owner is a public body, the state-owner rule puts it in 'serious'. "
                              "Human-rights relevance is remote - a local government tourism body with no "
                              "armed-conflict or conflict-minerals exposure.", "")],
    "io-sono-friuli-venezia-giulia": [(" The owner is therefore a public authority - 'serious' under the "
                                       "state-owner rule. Human-rights relevance: a regional government's "
                                       "destination marketing, with no conflict or minerals exposure.", "")],
    "md-anderson-cancer-center": [(" State ownership, so 'serious' under the rule. Human-rights relevance: "
                                   "public healthcare/research, no conflict exposure.", "")],
    "prometeon": [(" A Chinese state owner of that size is a material state link on a Ferrari sponsor.", "")],
    "pirelli": [(" A Chinese state owner of that size is a material state link on a Ferrari sponsor.", "")],
    "pulsee-luce-e-gas": [(" The Genoa front sponsor is therefore backed by sub-national Swiss state capital.", "")],
    "sardegna-turismo": [(" It is a public-law regional body, so this is sub-national state money.",
                          " It is a public-law regional body.")],
}


def apply_rule(entry):
    """HOLD and CLAIM_TEXT_FIX for one encoded rating. Idempotent."""
    sid = entry["sponsorId"]
    claim = entry.get("claim") or {}
    for old, new in CLAIM_TEXT_FIX.get(sid, []):
        if old in claim.get("text", ""):
            claim["text"] = claim["text"].replace(old, new)
            claim["short"] = short_of(claim["text"])
    if sid in HOLD and not entry.get("hold"):
        entry["tier"] = "unrated"
        entry["hold"] = HOLD[sid]
        note = (entry.get("note") or "").strip()
        entry["note"] = (note + " " if note else "") + "ON HOLD: " + HOLD[sid] + "."
        if entry.get("owner"):
            entry["owner"]["note"] = entry["note"]
        entry["verdict"] = verdict_for("unrated", entry["owner"], claim.get("short", ""))
    return entry


def short_of(text, limit=165):
    t = re.sub(r"\s+", " ", (text or "").strip())
    first = t.split(". ")[0].strip()
    if len(first) > limit:
        first = first[: limit - 1].rsplit(" ", 1)[0] + "…"
    return first if first.endswith((".", "!", "?")) else first + "."


def verdict_for(tier, owner, short):
    name = owner["name"]
    if tier == "none":
        return f"Owned by {name}. Nothing found."
    if tier == "concern":
        return f"{short}"
    return short


# Sponsor ids were cleaned of their parenthetical ('citigroup-citi' -> 'citigroup') after
# the rating pass ran, so researched ratings would silently stop matching. Map them across
# instead of paying for the research twice.
ALIAS = {
    "citigroup-citi": "citigroup",
    "citizens-bank-citizens-financial-group": "citizens-bank",
    "coors-brewing-co-molson-coors": "coors-brewing-co",
    "gainbridge-group-1001": "gainbridge",
    "gillette-procter-and-gamble": "gillette",
    "globe-life-globe-life-inc": "globe-life",
    "huntington-national-bank-huntington-bancshares": "huntington-national-bank",
    "jpmorgan-chase-chase": "jpmorgan-chase",
    "jpmorgan-chase-chase-brand": "jpmorgan-chase",
    "levi-strauss-and-co-levi-s": "levi-strauss-and-co",
    "metlife-metropolitan-life-insurance": "metlife",
    "nrg-energy-reliant-brand": "nrg-energy",
    "pnc-bank-pnc-financial-services": "pnc-bank",
    "rate-formerly-guaranteed-rate": "rate",
    "rocket-rocket-companies": "rocket",
    "spectrum-charter-communications": "spectrum",
    "target-target-corporation": "target",
    "tropicana-tropicana-brands-group": "tropicana",
    "xfinity-mobile-comcast": "xfinity-mobile",
}


def main():
    rows = []
    seen = set()
    for path in SRC:
        if not os.path.exists(path):
            print("missing", path)
            continue
        raw = json.load(open(path, encoding="utf-8"))
        for r in (raw["ratings"] if isinstance(raw, dict) else raw):
            r = dict(r)
            r["sponsorId"] = ALIAS.get(r["sponsorId"], r["sponsorId"])
            if r["sponsorId"] in seen:
                continue
            seen.add(r["sponsorId"])
            rows.append(r)
    out = []
    for r in rows:
        sid = r["sponsorId"]
        tier = r["tier"]
        note = (r.get("note") or "").strip()
        if sid in OVERRIDE and tier == "unrated":
            tier = OVERRIDE[sid][0]
        if sid in OVERRIDE:
            tier, why = OVERRIDE[sid]
            note = (note + " " if note else "") + "ADJUSTED: " + why
        owner = r["owner"]
        claim = r.get("claim") or {}
        src = claim.get("source") or {}
        if not src.get("url"):
            continue  # a tier above unrated needs a source with a URL
        text = re.sub(r"\s+", " ", claim.get("text", "")).strip()
        short = short_of(text)
        out.append({
            "sponsorId": sid,
            "tier": tier,
            "ownership": "part-owned" if sid in PART_OWNED else "owned",
            "owner": {
                "id": owner["id"],
                "name": owner["name"],
                "type": owner["type"],
                "country": owner.get("country"),
                "note": note or None,
            },
            "claim": {
                "text": text,
                "short": short,
                "source": {"name": src.get("name"), "date": src.get("date"), "url": src.get("url")},
            },
            "verdict": verdict_for(tier, owner, short),
            "confidence": r.get("confidence"),
            "note": note or None,
        })
        apply_rule(out[-1])
    out.sort(key=lambda x: x["sponsorId"])

    with open(OUT, "w", encoding="utf-8") as f:
        f.write('"""Sponsor ratings with the owner chain and the evidence behind each one."""\n\n')
        f.write("RATINGS = ")
        # this file is imported as Python, so it needs None/True, not JSON null/true
        f.write(pprint.pformat(out, width=118, sort_dicts=False))
        f.write("\n")
    print("wrote", OUT, len(out), "ratings")
    from collections import Counter
    print("tiers:", dict(Counter(x["tier"] for x in out)))


def reapply():
    """Re-apply HOLD and CLAIM_TEXT_FIX to the committed ratings_data.py."""
    import ratings_data
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ratings_data.py")
    out = [apply_rule(dict(r)) for r in ratings_data.RATINGS]
    with open(here, "w", encoding="utf-8") as f:
        f.write('"""Sponsor ratings with the owner chain and the evidence behind each one."""\n\n')
        f.write("RATINGS = ")
        f.write(pprint.pformat(out, width=118, sort_dicts=False))
        f.write("\n")
    from collections import Counter
    print("reapplied to", here, "| held:", sum(1 for x in out if x.get("hold")),
          "| tiers:", dict(Counter(x["tier"] for x in out)))


if __name__ == "__main__":
    import sys
    reapply() if "--reapply" in sys.argv else main()
