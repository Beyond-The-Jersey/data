# Beyond The Jersey — data

Normalised data files for the site. The site reads `normalized/` and falls back to the seed
while `validate.py` does not print `OK`.

## Files

14 files, all keyed by ASCII kebab-case ids: `clubs`, `sponsors`, `owners`, `claims`, `kits`,
`deals`, `changes`, `dropped`, `contacts`, `sports`, `leagues`, `levels`, `tiers`, `meta`.

* referential fields (`clubId`, `sponsorId`, `ownerId`, `claimIds`) hold **ids**, never names
* `source` is `{name, date, url}` of the primary document, or omitted while it is being looked up
* optional fields are omitted when unknown; `null` is only used where the schema says a value
  is genuinely null (an undisclosed deal value, a kit with no change)
* currencies are `GBP` / `EUR` / `USD`

## Rating rule

The tiers are defined in `tiers.json` (the website's `data/schema` and seed):

| Tier | Needs |
|---|---|
| `severe` | Paid for by a state directly tied to ongoing severe abuses (armed conflict, conflict minerals), with a sourced claim of those abuses. |
| `serious` | Owned by a state or state fund **with documented serious abuses**: a sourced claim of those abuses by a state in the sponsor's owner chain. |
| `concern` | A lesser link, e.g. a minority stake held by a state or state fund with a poor record. |
| `none` | Sponsor and owner checked, with a sourced ownership claim; no link to serious abuses. |
| `unrated` | Not checked yet, or on hold. |

- **State ownership alone is not a tier.** A public owner in a state with no sourced record of serious abuses (a US state university, a county tourism board, an Italian region, Swiss cantons) is not `serious`. Until a person reviews it, it is held at `unrated` in `encode_ratings.HOLD`: the owner and the evidence stay, and the builder marks the sponsor `being-rated`, so the website shows what we know with "Not rated yet".
- **Every `serious` or `severe` sponsor has a `why`** (`why_texts.json`, or the seed's) that cites the abuse claim. `build_normalized.py` lists any that don't under "rating rule:".
- **Claim texts state what their source says.** The reasoning behind a tier ("State ownership alone earns serious", "Human-rights relevance is remote") goes in the rating's `note`, not in the claim.
- **A claim must be about the sponsor it's cited for** (not another company that shares the owner), and its owner must be in that sponsor's chain.

After editing `encode_ratings.HOLD` or `CLAIM_TEXT_FIX`, run `python3 encode_ratings.py --reapply` and rebuild.

## Checking

    python3 validate.py normalized/ --assets <website>/public

Must print `OK`.

## Rebuilding

    pip3 install requests jsonschema
    python3 build_contacts.py      # network; writes contacts_build.json
    python3 enrich_contacts.py     # network; adds a contact page / email to thin records
    python3 build_normalized.py    # writes normalized/ and runs the validator

Run the three in that order. `enrich_contacts.py` only touches records missing an email
or a contact page, and `build_normalized.py` merges the hand-checked channels in
`build_contacts.OVERRIDES` on top, so a flaky fetch can never drop a club.

`build_normalized.py` starts from the website seed and merges the curated additions in
`pipeline_data.py`. `build_from_seed.py` is the earlier seed-only builder.

Set `BTJ_SEED` and `BTJ_VALIDATE` if the website checkout is not at `/tmp/website`.

## Two trees, one id space

`normalized/` is **canonical**. The website reads only that (`BTJ_DATA_SOURCE=repo`
points at it), and `validate.py` runs against it.

`data/` is a regenerated per-club projection of the same records in the older handover
shape, one file per club keyed by the same ASCII slug, plus `index.json`. It is written
by the build, so the two trees cannot drift or disagree on an id again. Differences from
the original handover files, all deliberate:

* ids and filenames are ASCII slugs (`1-fc-koln.json`, not `1-fc-köln.json`)
* `league` is the league id (`premier-league`), not the old underscore form
* there is no letter grade: `tier` is the new tier id, and `worstTier` is the club's
  highest tier across its sponsors
* `sources: ["Wikipedia"]` is replaced by the source object

If something outside the website still reads `data/`, it reads consistent data now.
