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
