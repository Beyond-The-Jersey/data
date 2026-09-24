"""Sponsor ratings with the owner chain and the evidence behind each one."""

RATINGS = [
    {
        "sponsorId": "aeroflot",
        "tier": "severe",
        "ownership": "owned",
        "owner": {
            "id": "russian-federation",
            "name": "Russian Federation (Federal Agency for State Property Management)",
            "type": "state",
            "country": "RU",
            "note": "Severe because the state owner is directly tied to an ongoing armed conflict. Russia planned to sell ~23.76% of its stake (Interfax, 2026), which would cut the state to ~50% but keep control. Sanctions context: https://www.consilium.europa.eu/en/policies/sanctions-against-russia-explained/."
        },
        "claim": {
            "text": "PJSC Aeroflot is majority state-owned: the Russian Federation is the controlling shareholder of approximately 73.8% of shares. Russia is the direct belligerent in the ongoing war in Ukraine, and Aeroflot plus its state parent have been targeted by EU/US sanctions since 2022.",
            "short": "PJSC Aeroflot is majority state-owned: the Russian Federation is the controlling shareholder of approximately 73.8% of shares.",
            "source": {
                "name": "Aeroflot Investor Relations, Shareholder Capital; Council of the EU sanctions explainer",
                "date": "2025 / 2026",
                "url": "https://ir.aeroflot.com/ensecurities/shareholder-capital"
            }
        },
        "verdict": "PJSC Aeroflot is majority state-owned: the Russian Federation is the controlling shareholder of approximately 73.8% of shares.",
        "confidence": "high",
        "note": "Severe because the state owner is directly tied to an ongoing armed conflict. Russia planned to sell ~23.76% of its stake (Interfax, 2026), which would cut the state to ~50% but keep control. Sanctions context: https://www.consilium.europa.eu/en/policies/sanctions-against-russia-explained/."
    },
    {
        "sponsorId": "aia",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "aia-group",
            "name": "AIA Group Limited (HKEX: 1299)",
            "type": "listed-company",
            "country": "HK",
            "note": "Listed Hong Kong company → none. Historical note: AIA was spun out of AIG; the US government's AIG bailout stake was long ago exited."
        },
        "claim": {
            "text": "AIA Group Limited is incorporated in Hong Kong with limited liability and listed on the Hong Kong Stock Exchange (stock code 1299); it presents itself as the largest independent publicly listed pan-Asian life insurer. No state or state-fund owner.",
            "short": "AIA Group Limited is incorporated in Hong Kong with limited liability and listed on the Hong Kong Stock Exchange (stock code 1299); it presents itself as the….",
            "source": {
                "name": "AIA Group Limited official filings/press release; company corporate documents",
                "date": "2023-07",
                "url": "https://www.aia.com/content/dam/group-wise/en/docs/press-release/2023/AIA%20Group%20Press%20Release_ENG_13%20July%202023.pdf.coredownload.pdf"
            }
        },
        "verdict": "Owned by AIA Group Limited (HKEX: 1299). Nothing found.",
        "confidence": "high",
        "note": "Listed Hong Kong company → none. Historical note: AIA was spun out of AIG; the US government's AIG bailout stake was long ago exited."
    },
    {
        "sponsorId": "betano",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "kaizen-gaming",
            "name": "Kaizen Gaming International Limited (partly owned by Allwyn)",
            "type": "private-company",
            "country": "GR",
            "note": "Private Greek/Czech owners, no state link → none. Kaizen is registered/parented in Malta while Greek-founded; country shown as GR as the operating origin. Ownership percentage sourced from trade press, hence medium confidence."
        },
        "claim": {
            "text": "Betano is owned by Kaizen Gaming International Limited, a private Greek-founded GameTech group; its parent has reached decacorn status and Allwyn holds a 36.75% stake. Owners are private investors (Allwyn/KKCG of Czech billionaire Karel Komarek), with no state or state-fund owner.",
            "short": "Betano is owned by Kaizen Gaming International Limited, a private Greek-founded GameTech group; its parent has reached decacorn status and Allwyn holds a 36.75%….",
            "source": {
                "name": "Kaizen Gaming official; EGR Global (Allwyn 36.75% stake)",
                "date": "2026",
                "url": "https://www.egr.global/intel/news/betanos-parent-company-achieves-decacorn-status/"
            }
        },
        "verdict": "Owned by Kaizen Gaming International Limited (partly owned by Allwyn). Nothing found.",
        "confidence": "medium",
        "note": "Private Greek/Czech owners, no state link → none. Kaizen is registered/parented in Malta while Greek-founded; country shown as GR as the operating origin. Ownership percentage sourced from trade press, hence medium confidence."
    },
    {
        "sponsorId": "circle-usdc",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "circle-internet-group",
            "name": "Circle Internet Group, Inc. (NYSE: CRCL) — public shareholders",
            "type": "listed-company",
            "country": "US",
            "note": "Listed US company, no state link → none."
        },
        "claim": {
            "text": "USDC is issued by Circle; the issuer's parent, Circle Internet Group, Inc., listed on the NYSE in June 2025 via an S-1 registration (SEC CIK 1876042). It is a US-listed company with dispersed public shareholders and no state or state-fund owner.",
            "short": "USDC is issued by Circle; the issuer's parent, Circle Internet Group, Inc., listed on the NYSE in June 2025 via an S-1 registration (SEC CIK 1876042).",
            "source": {
                "name": "SEC Form S-1, Circle Internet Group, Inc.",
                "date": "2025-06",
                "url": "https://www.sec.gov/Archives/edgar/data/1876042/000119312525178989/d839239ds1.htm"
            }
        },
        "verdict": "Owned by Circle Internet Group, Inc. (NYSE: CRCL) — public shareholders. Nothing found.",
        "confidence": "high",
        "note": "Listed US company, no state link → none."
    },
    {
        "sponsorId": "clickhouse",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "clickhouse-inc",
            "name": "ClickHouse, Inc. (private, VC-backed)",
            "type": "private-company",
            "country": "US",
            "note": "Private owner → none. GIC (Singapore) is a minority investor only; Singapore's record is clean, so no abuse link. Arguable concern if any SWF minority counts; recorded here."
        },
        "claim": {
            "text": "ClickHouse, Inc. is a private San Francisco analytics company whose Series C (led by Khosla Ventures) and $400m Series D (led by Dragoneer) brought in financial investors including Bessemer, Index and Singapore's sovereign fund GIC. Owner is private; only minority sovereign-fund exposure.",
            "short": "ClickHouse, Inc.",
            "source": {
                "name": "ClickHouse official Series C/D announcements",
                "date": "2025-05 / 2026-01",
                "url": "https://clickhouse.com/blog/clickhouse-raises-350-million-series-c-to-power-analytics-for-ai-era"
            }
        },
        "verdict": "Owned by ClickHouse, Inc. (private, VC-backed). Nothing found.",
        "confidence": "medium",
        "note": "Private owner → none. GIC (Singapore) is a minority investor only; Singapore's record is clean, so no abuse link. Arguable concern if any SWF minority counts; recorded here."
    },
    {
        "sponsorId": "cmc-markets",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "cmc-markets-plc",
            "name": "CMC Markets Plc (London-listed; Cruddas family significant holder)",
            "type": "listed-company",
            "country": "GB",
            "note": "Listed UK company with a founder/family anchor, no state link → none."
        },
        "claim": {
            "text": "CMC Markets is a London-listed CFD broker founded and led by Peter Cruddas, Baron Cruddas, whose family is among the top shareholders; the rest is free float. No state or state-fund owner.",
            "short": "CMC Markets is a London-listed CFD broker founded and led by Peter Cruddas, Baron Cruddas, whose family is among the top shareholders; the rest is free float.",
            "source": {
                "name": "CMC Markets Plc press release (founder appointed to the Lords); Finance Magnates/TradingView on shareholder base",
                "date": "2020 / 2025",
                "url": "https://www.cmcmarkets.com/group/press-releases/peter-cruddas-appointed-to-the-house-of-lords-as-baron-cruddas-of-shoreditch"
            }
        },
        "verdict": "Owned by CMC Markets Plc (London-listed; Cruddas family significant holder). Nothing found.",
        "confidence": "high",
        "note": "Listed UK company with a founder/family anchor, no state link → none."
    },
    {
        "sponsorId": "deutsche-telekom",
        "tier": "concern",
        "ownership": "part-owned",
        "owner": {
            "id": "federal-republic-of-germany",
            "name": "Federal Republic of Germany (direct stake + KfW) with the remainder free float",
            "type": "state",
            "country": "DE",
            "note": "State is the largest single owner block → state link, but Germany's record is not seriously abusive → concern. Alternative reading: none. KfW stake note: https://www.kfw.de/About-KfW/Newsroom/Latest-News/News-Details_134528.html"
        },
        "claim": {
            "text": "Deutsche Telekom's own shareholder-structure page shows the Federal Republic of Germany as the anchor shareholder via KfW (approx. 14.4%) plus a direct federal holding, together roughly 28-30% of shares, with the balance free float.",
            "short": "Deutsche Telekom's own shareholder-structure page shows the Federal Republic of Germany as the anchor shareholder via KfW (approx.",
            "source": {
                "name": "Deutsche Telekom Investor Relations, Shareholder structure; KfW newsroom",
                "date": "2026-06-30",
                "url": "https://www.telekom.com/en/investor-relations/share/shareholder-structure"
            }
        },
        "verdict": "Deutsche Telekom's own shareholder-structure page shows the Federal Republic of Germany as the anchor shareholder via KfW (approx.",
        "confidence": "medium",
        "note": "State is the largest single owner block → state link, but Germany's record is not seriously abusive → concern. Alternative reading: none. KfW stake note: https://www.kfw.de/About-KfW/Newsroom/Latest-News/News-Details_134528.html"
    },
    {
        "sponsorId": "gazprom",
        "tier": "severe",
        "ownership": "owned",
        "owner": {
            "id": "russian-federation",
            "name": "Russian Federation (Federal Agency for State Property Management + state-controlled Rosneftegaz)",
            "type": "state",
            "country": "RU",
            "note": "Severe: state-controlled and the state is the direct party to an ongoing armed conflict. State-control claim corroborated by the company's own investor page; war-funding claim from Yale HRL PDF."
        },
        "claim": {
            "text": "The Russian Government controls over 50% of Gazprom's shares (Russian Federation direct 38.37% plus government-controlled Rosneftegaz 10.97% and Rosgazifikatsiya 0.89%, per the company's own share register). Gas revenues underwrite the Russian state, and Yale HRL concluded with high confidence that Gazprom, as a Russian state-owned company, 'underwrote and funded' the war effort.",
            "short": "The Russian Government controls over 50% of Gazprom's shares (Russian Federation direct 38.37% plus government-controlled Rosneftegaz 10.97% and Rosgazifikatsiya….",
            "source": {
                "name": "Gazprom official 'Shares'/equity capital page; Yale School of Public Health Humanitarian Research Lab, 'Willing Accomplices'",
                "date": "2025-12-31 / 2023",
                "url": "https://www.gazprom.com/investors/stock/"
            }
        },
        "verdict": "The Russian Government controls over 50% of Gazprom's shares (Russian Federation direct 38.37% plus government-controlled Rosneftegaz 10.97% and Rosgazifikatsiya….",
        "confidence": "high",
        "note": "Severe: state-controlled and the state is the direct party to an ongoing armed conflict. State-control claim corroborated by the company's own investor page; war-funding claim from Yale HRL PDF."
    },
    {
        "sponsorId": "indeed",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "recruit-holdings",
            "name": "Recruit Holdings Co., Ltd. (Tokyo-listed)",
            "type": "listed-company",
            "country": "JP",
            "note": "Listed Japanese parent, no state link → none."
        },
        "claim": {
            "text": "Indeed, Inc. was acquired in 2012 and is a key subsidiary of Recruit Holdings Co., Ltd., a Tokyo-listed Japanese holding company that also owns Glassdoor. No state or state-fund owner.",
            "short": "Indeed, Inc.",
            "source": {
                "name": "Recruit Holdings official 'Group Companies' page",
                "date": "2026",
                "url": "https://recruit-holdings.com/en/about/group"
            }
        },
        "verdict": "Owned by Recruit Holdings Co., Ltd. (Tokyo-listed). Nothing found.",
        "confidence": "high",
        "note": "Listed Japanese parent, no state link → none."
    },
    {
        "sponsorId": "kraken",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "payward",
            "name": "Payward, Inc. (d/b/a Kraken)",
            "type": "private-company",
            "country": "US",
            "note": "Private US owner with no state link → none. The Iran sanctions settlement is a lesser, conduct-level link flagged in the note. Kraken named Payward as parent: https://www.kraken.com/."
        },
        "claim": {
            "text": "Kraken is a brand of Payward, Inc., a Delaware-incorporated private company (Kraken Securities LLC is a wholly owned subsidiary of Payward, Inc.). The company is privately held with VC backers including Tribe Capital; no state or state-fund owner. Note: OFAC settled with Payward/Kraken for $362,158.70 over apparent violations of the Iranian Transactions and Sanctions Regulations — a conduct issue, not ownership.",
            "short": "Kraken is a brand of Payward, Inc., a Delaware-incorporated private company (Kraken Securities LLC is a wholly owned subsidiary of Payward, Inc.).",
            "source": {
                "name": "OFAC enforcement release (Nov 28, 2022); Kraken/Payward disclosures",
                "date": "2022-11-28",
                "url": "https://ofac.treasury.gov/system/files/126/20221128_kraken.pdf"
            }
        },
        "verdict": "Owned by Payward, Inc. (d/b/a Kraken). Nothing found.",
        "confidence": "high",
        "note": "Private US owner with no state link → none. The Iran sanctions settlement is a lesser, conduct-level link flagged in the note. Kraken named Payward as parent: https://www.kraken.com/."
    },
    {
        "sponsorId": "lbbw",
        "tier": "concern",
        "ownership": "part-owned",
        "owner": {
            "id": "state-of-baden-wuerttemberg",
            "name": "State of Baden-Württemberg, Sparkassenverband Baden-Württemberg and City of Stuttgart",
            "type": "state",
            "country": "DE",
            "note": "Owner is the German state/public sector; Germany has no 'documented serious abuses' at state level, so this is treated as a lesser link → concern. An honest alternative reading is none (clean state). Recorded here rather than picked silently."
        },
        "claim": {
            "text": "Landesbank Baden-Württemberg is a public-law institution whose Owners are the Savings Banks Association of Baden-Württemberg (SVBW), the State of Baden-Württemberg, the state capital Stuttgart and Landesbeteiligungen Baden-Württemberg — i.e. wholly public/state owner.",
            "short": "Landesbank Baden-Württemberg is a public-law institution whose Owners are the Savings Banks Association of Baden-Württemberg (SVBW), the State of….",
            "source": {
                "name": "Landesbank Baden-Württemberg Ordinance/statute (English translation), LBBW legal documents",
                "date": "1998 (as amended)",
                "url": "https://www.lbbw.de/rechts-und-kundeninformationen/ordinance_of_landesbank_baden_wuerttemberg_en_89p7ho77b_m.pdf"
            }
        },
        "verdict": "Landesbank Baden-Württemberg is a public-law institution whose Owners are the Savings Banks Association of Baden-Württemberg (SVBW), the State of….",
        "confidence": "medium",
        "note": "Owner is the German state/public sector; Germany has no 'documented serious abuses' at state level, so this is treated as a lesser link → concern. An honest alternative reading is none (clean state). Recorded here rather than picked silently."
    },
    {
        "sponsorId": "marex",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "marex-group-plc",
            "name": "Marex Group plc (Nasdaq-listed) — public and former PE sponsors",
            "type": "listed-company",
            "country": "GB",
            "note": "Listed company with PE heritage (private-equity sponsors were prior owners) → none. Owner type recorded as listed-company because the sponsors' control has dispersed post-IPO."
        },
        "claim": {
            "text": "Marex Group plc listed on Nasdaq (June 2024) after growth under private-equity sponsors, creating a public float while sponsors retained significant stakes; the company provides an investors/SEC-filings section evidencing a listed, dispersed ownership. No state or state-fund owner.",
            "short": "Marex Group plc listed on Nasdaq (June 2024) after growth under private-equity sponsors, creating a public float while sponsors retained significant stakes; the….",
            "source": {
                "name": "Marex investor relations (SEC filings); Reuters/trade coverage of June 2024 IPO",
                "date": "2024-06",
                "url": "https://www.marex.com/investors"
            }
        },
        "verdict": "Owned by Marex Group plc (Nasdaq-listed) — public and former PE sponsors. Nothing found.",
        "confidence": "medium",
        "note": "Listed company with PE heritage (private-equity sponsors were prior owners) → none. Owner type recorded as listed-company because the sponsors' control has dispersed post-IPO."
    },
    {
        "sponsorId": "monzo",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "monzo-bank-limited",
            "name": "Monzo Bank Limited (private, VC-backed)",
            "type": "private-company",
            "country": "GB",
            "note": "Private company, dispersed VC ownership → none. No single dominant owner documented, so the owner object points at the bank itself."
        },
        "claim": {
            "text": "Monzo Bank Limited is a UK-incorporated private bank with a full banking licence and no controlling shareholder; ownership is dispersed across venture investors. No state or state-fund owner.",
            "short": "Monzo Bank Limited is a UK-incorporated private bank with a full banking licence and no controlling shareholder; ownership is dispersed across venture investors.",
            "source": {
                "name": "Monzo Investor Information / Annual Report & Group Financial Statements",
                "date": "2026",
                "url": "https://monzo.com/investor-information"
            }
        },
        "verdict": "Owned by Monzo Bank Limited (private, VC-backed). Nothing found.",
        "confidence": "medium",
        "note": "Private company, dispersed VC ownership → none. No single dominant owner documented, so the owner object points at the bank itself."
    },
    {
        "sponsorId": "qatar-airways",
        "tier": "serious",
        "ownership": "owned",
        "owner": {
            "id": "government-of-qatar",
            "name": "Government of the State of Qatar (Qatar Airways Group Q.C.S.C.)",
            "type": "state",
            "country": "QA",
            "note": "Owner is a sovereign state, not a state fund, and Qatar is not a party to an armed conflict, so serious rather than severe. Migrant-worker deaths and unpaid wages documented by HRW and Amnesty; Qatar reformed kafala in 2020 but remedy/compensation remains outstanding (https://www.hrw.org/news/2022/11/17/fifa/qatar-migrant-workers-call-for-compensation-for-abuses)."
        },
        "claim": {
            "text": "Qatar Airways Group Q.C.S.C. is incorporated in Qatar and 'is ultimately wholly owned by the Government of the State of Qatar (the \"Shareholder\")'; the state's kafala/migrant-labour system produced documented serious abuses in the run-up to the 2022 World Cup.",
            "short": "Qatar Airways Group Q.C.S.C.",
            "source": {
                "name": "Qatar Airways Group audited consolidated financial statements (note: corporate information); Human Rights Watch",
                "date": "2022-03 / 2022-11",
                "url": "https://www.qatarairways.com/content/dam/documents/annual-reports/2022/financial-statement-en.pdf"
            }
        },
        "verdict": "Qatar Airways Group Q.C.S.C.",
        "confidence": "high",
        "note": "Owner is a sovereign state, not a state fund, and Qatar is not a party to an armed conflict, so serious rather than severe. Migrant-worker deaths and unpaid wages documented by HRW and Amnesty; Qatar reformed kafala in 2020 but remedy/compensation remains outstanding (https://www.hrw.org/news/2022/11/17/fifa/qatar-migrant-workers-call-for-compensation-for-abuses)."
    },
    {
        "sponsorId": "red-bull",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "mateschitz-yoovidhya-families",
            "name": "Mateschitz family (49%) and Yoovidhya family (51%), via Red Bull GmbH",
            "type": "family",
            "country": "AT",
            "note": "Private/family owner → none. Thailand's state is not in the ownership chain despite the Thai ownership origin."
        },
        "claim": {
            "text": "Red Bull GmbH is a privately held Austrian company owned by two families: the founding Yoovidhya family of Thailand holds 51% and the Mateschitz family (Mark Mateschitz, heir of co-founder Dietrich) holds 49%. Neither owner is a state or state fund.",
            "short": "Red Bull GmbH is a privately held Austrian company owned by two families: the founding Yoovidhya family of Thailand holds 51% and the Mateschitz family (Mark….",
            "source": {
                "name": "Reuters (Red Bull leadership after co-founder's death, referencing the inherited 49% stake)",
                "date": "2022-11-04",
                "url": "https://www.reuters.com/business/retail-consumer/trio-lead-energy-drinks-giant-red-bull-after-co-founders-death-2022-11-04/"
            }
        },
        "verdict": "Owned by Mateschitz family (49%) and Yoovidhya family (51%), via Red Bull GmbH. Nothing found.",
        "confidence": "high",
        "note": "Private/family owner → none. Thailand's state is not in the ownership chain despite the Thai ownership origin."
    },
    {
        "sponsorId": "sap",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "sap-se",
            "name": "SAP SE — free float with founder-family anchors",
            "type": "listed-company",
            "country": "DE",
            "note": "Listed German company → none."
        },
        "claim": {
            "text": "SAP SE is a Frankfurt-listed German software company with a free float of about 84% reported by the company itself; the largest identified holders are founder-family vehicles (Hopp family ~5.1%, Portika gGmbH ~3.6%) — private, not state. No state or state-fund owner.",
            "short": "SAP SE is a Frankfurt-listed German software company with a free float of about 84% reported by the company itself; the largest identified holders are….",
            "source": {
                "name": "SAP Investor Relations, shareholder structure/basic data",
                "date": "2026",
                "url": "https://www.sap.com/investors/en/stock/basic-data.html"
            }
        },
        "verdict": "Owned by SAP SE — free float with founder-family anchors. Nothing found.",
        "confidence": "high",
        "note": "Listed German company → none."
    },
    {
        "sponsorId": "snapdragon",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "qualcomm",
            "name": "Qualcomm Incorporated (Nasdaq-listed) — Snapdragon is its brand",
            "type": "listed-company",
            "country": "US",
            "note": "Listed US company → none. Note only: Qualcomm faces antitrust rather than human-rights findings."
        },
        "claim": {
            "text": "Snapdragon is Qualcomm's product brand, not a separate entity: Qualcomm Incorporated is a US Nasdaq-listed semiconductor company with dispersed public shareholders and no state or state-fund owner.",
            "short": "Snapdragon is Qualcomm's product brand, not a separate entity: Qualcomm Incorporated is a US Nasdaq-listed semiconductor company with dispersed public shareholders….",
            "source": {
                "name": "Qualcomm official 'About Qualcomm' / Snapdragon FAQ",
                "date": "2026",
                "url": "https://www.qualcomm.com/company"
            }
        },
        "verdict": "Owned by Qualcomm Incorporated (Nasdaq-listed) — Snapdragon is its brand. Nothing found.",
        "confidence": "high",
        "note": "Listed US company → none. Note only: Qualcomm faces antitrust rather than human-rights findings."
    },
    {
        "sponsorId": "standard-chartered",
        "tier": "concern",
        "ownership": "owned",
        "owner": {
            "id": "standard-chartered-plc",
            "name": "Standard Chartered Plc — public shareholders",
            "type": "listed-company",
            "country": "GB",
            "note": "Listed UK owner, no state link → none. Honesty flag: the task highlighted SC as 'interesting', and its sanctions-violation history is real, but under a state-ownership rubric the honest tier is none. If conduct counted, concern. ADJUSTED: Raised from none: the 2012 and 2019 forfeitures are a sustained structural record, not a one-off fine, which is what tiers.json calls 'a lesser link'."
        },
        "claim": {
            "text": "Standard Chartered is a London-headquartered, publicly listed bank with dispersed shareholders and no state or state-fund owner. Its Iran/Sudan history is a conduct record, not ownership: the bank agreed to forfeit $227m in 2012 for illegal transactions with Iran, Sudan, Libya and Burma and a further ~$1.1bn in 2019 for Iran-related sanctions/AML failures.",
            "short": "Standard Chartered is a London-headquartered, publicly listed bank with dispersed shareholders and no state or state-fund owner.",
            "source": {
                "name": "US DOJ press release (Dec 10, 2012); DLA Piper legal bulletin on the 2019 USD1.1bn settlement",
                "date": "2012-12-10 / 2019-04",
                "url": "https://www.justice.gov/archives/opa/pr/standard-chartered-bank-agrees-forfeit-227-million-illegal-transactions-iran-sudan-libya-and"
            }
        },
        "verdict": "Standard Chartered is a London-headquartered, publicly listed bank with dispersed shareholders and no state or state-fund owner.",
        "confidence": "high",
        "note": "Listed UK owner, no state link → none. Honesty flag: the task highlighted SC as 'interesting', and its sanctions-violation history is real, but under a state-ownership rubric the honest tier is none. If conduct counted, concern. ADJUSTED: Raised from none: the 2012 and 2019 forfeitures are a sustained structural record, not a one-off fine, which is what tiers.json calls 'a lesser link'."
    },
    {
        "sponsorId": "temporal",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "temporal-technologies",
            "name": "Temporal Technologies, Inc. (private, VC-backed)",
            "type": "private-company",
            "country": "US",
            "note": "Private VC-backed US company → none. Source is business press; company has no published shareholder register."
        },
        "claim": {
            "text": "Temporal Technologies is a private Bellevue, Washington company that raised a $550m Series E at a $12.55bn valuation led by Lightspeed with Wellington, Goldman Sachs Alternatives Growth Equity and Tiger Global — all financial investors, none a state or sovereign fund.",
            "short": "Temporal Technologies is a private Bellevue, Washington company that raised a $550m Series E at a $12.55bn valuation led by Lightspeed with Wellington, Goldman….",
            "source": {
                "name": "Temporal Series E reporting (GeekWire-derived coverage)",
                "date": "2026",
                "url": "https://425business.com/news/temporal-raises-550m-in-series-e-company-valued-at-12-55b/article_3f5859c3-e9d8-4cc7-816f-6616745a60dc.html"
            }
        },
        "verdict": "Owned by Temporal Technologies, Inc. (private, VC-backed). Nothing found.",
        "confidence": "medium",
        "note": "Private VC-backed US company → none. Source is business press; company has no published shareholder register."
    },
    {
        "sponsorId": "trade-nation",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "jasper-white",
            "name": "Jasper White (private UK entrepreneur)",
            "type": "individual",
            "country": "GB",
            "note": "Private individual owner → none. Source is trade press rather than a filing, hence medium confidence."
        },
        "claim": {
            "text": "Trade Nation and its brands are controlled by UK entrepreneur Jasper White, who bought control of the company (then The Trader Management Company Limited) in 2014. It is a private CFD/FX broker with UK (FCA), Australian and Portuguese (CMVM) authorisations — no state or state-fund owner.",
            "short": "Trade Nation and its brands are controlled by UK entrepreneur Jasper White, who bought control of the company (then The Trader Management Company Limited) in 2014.",
            "source": {
                "name": "FX News Group (trade press, citing control by Jasper White)",
                "date": "2025",
                "url": "https://fxnewsgroup.com/forex-news/retail-forex/exclusive-trade-nation-revenues-rise-17-in-2025-to-25m-following-ceo-change"
            }
        },
        "verdict": "Owned by Jasper White (private UK entrepreneur). Nothing found.",
        "confidence": "medium",
        "note": "Private individual owner → none. Source is trade press rather than a filing, hence medium confidence."
    },
    {
        "sponsorId": "turkish-airlines",
        "tier": "serious",
        "ownership": "part-owned",
        "owner": {
            "id": "turkiye-wealth-fund",
            "name": "Türkiye Wealth Fund (Türkiye Varlık Fonu) + Turkish state golden share",
            "type": "state-fund",
            "country": "TR",
            "note": "State fund with a documented serious-abuse state record → serious. Arguable alternative is concern, because ownership is only ~49% and the rest is free float; the privileged state share and fund control tip it to serious. Confidence medium for that reason."
        },
        "claim": {
            "text": "Turkish Airlines' official shareholding disclosure shows the state's Türkiye Wealth Fund as the largest shareholder with 49.12%, with a Ministry of Treasury and Finance 'privileged' share conferring control; the state fund sits at the top of the chain. Turkey has documented serious human-rights abuses (Kurdish conflict, post-2016 purges, press freedom).",
            "short": "Turkish Airlines' official shareholding disclosure shows the state's Türkiye Wealth Fund as the largest shareholder with 49.12%, with a Ministry of Treasury and….",
            "source": {
                "name": "Turkish Airlines official additional disclosure (Capital Markets Board of Türkiye); Türkiye Wealth Fund",
                "date": "2025 / 2026",
                "url": "https://tvf.com.tr/en/investor-relations/reports"
            }
        },
        "verdict": "Turkish Airlines' official shareholding disclosure shows the state's Türkiye Wealth Fund as the largest shareholder with 49.12%, with a Ministry of Treasury and….",
        "confidence": "medium",
        "note": "State fund with a documented serious-abuse state record → serious. Arguable alternative is concern, because ownership is only ~49% and the rest is free float; the privileged state share and fund control tip it to serious. Confidence medium for that reason."
    },
    {
        "sponsorId": "uralkali",
        "tier": "concern",
        "ownership": "owned",
        "owner": {
            "id": "uralchem",
            "name": "Uralchem PJSC (controlled by Dmitry Mazepin and family)",
            "type": "private-company",
            "country": "RU",
            "note": "Honesty flag: the task listed Uralkali under 'state-linked', but the ownership test shows a private owner, so none under the rubric. If the rubric counts the Russian state's war economy (not ownership) as the link, it would be concern. Uralkali itself has largely escaped sanctions (https://statewatch.org.ua/en/publications/rozsliduvannia/sanktsii/...). ADJUSTED: Raised from none: no state stake, but the ultimate owner sits inside a belligerent state and was sanctioned with it."
        },
        "claim": {
            "text": "Uralkali's controlling shareholder is Uralchem PJSC, which holds 81.47% of Uralkali; Uralchem is a private company, with Dmitry Mazepin previously holding 100% and selling a controlling 52% stake in 2022. No direct Russian state or state-fund stake is documented, so the ultimate owner is a private Russian holding.",
            "short": "Uralkali's controlling shareholder is Uralchem PJSC, which holds 81.47% of Uralkali; Uralchem is a private company, with Dmitry Mazepin previously holding 100% and….",
            "source": {
                "name": "Fitch Ratings (rating action recording Uralchem's 81.47% stake); Reuters (Mazepin sells controlling stake in Uralchem)",
                "date": "2021-10-05 / 2022",
                "url": "https://www.fitchratings.com/research/corporate-finance/fitch-revises-uralkali-outlook-to-negative-affirms-at-bb-05-10-2021"
            }
        },
        "verdict": "Uralkali's controlling shareholder is Uralchem PJSC, which holds 81.47% of Uralkali; Uralchem is a private company, with Dmitry Mazepin previously holding 100% and….",
        "confidence": "medium",
        "note": "Honesty flag: the task listed Uralkali under 'state-linked', but the ownership test shows a private owner, so none under the rubric. If the rubric counts the Russian state's war economy (not ownership) as the link, it would be concern. Uralkali itself has largely escaped sanctions (https://statewatch.org.ua/en/publications/rozsliduvannia/sanktsii/...). ADJUSTED: Raised from none: no state stake, but the ultimate owner sits inside a belligerent state and was sanctioned with it."
    },
    {
        "sponsorId": "visit-saudi",
        "tier": "serious",
        "ownership": "owned",
        "owner": {
            "id": "government-of-saudi-arabia",
            "name": "Saudi Tourism Authority (Government of Saudi Arabia)",
            "type": "state",
            "country": "SA",
            "note": "State body → state tier above none. Could be argued severe on Yemen-war grounds, but the Saudi-led intervention has largely wound down, so serious is used. Cross-source: HRW Saudi Arabia chapter https://hrw.org/world-report/2026/country-chapters/saudi-arabia."
        },
        "claim": {
            "text": "Visit Saudi is the flagship destination-marketing platform of the Saudi Tourism Authority, a government body established by royal decree in 2020 and a wholly state-funded entity. Saudi Arabia has documented serious labour-rights abuses: HRW's country chapter records migrant workers facing widespread wage theft and avoidable workplace deaths.",
            "short": "Visit Saudi is the flagship destination-marketing platform of the Saudi Tourism Authority, a government body established by royal decree in 2020 and a wholly….",
            "source": {
                "name": "Saudi Tourism Authority / Visit Saudi official 'About us'; Human Rights Watch World Report",
                "date": "2020-03 / 2026",
                "url": "https://www.visitsaudi.com/en/about-us"
            }
        },
        "verdict": "Visit Saudi is the flagship destination-marketing platform of the Saudi Tourism Authority, a government body established by royal decree in 2020 and a wholly….",
        "confidence": "high",
        "note": "State body → state tier above none. Could be argued severe on Yemen-war grounds, but the Saudi-led intervention has largely wound down, so serious is used. Cross-source: HRW Saudi Arabia chapter https://hrw.org/world-report/2026/country-chapters/saudi-arabia."
    },
    {
        "sponsorId": "vitality",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "discovery-limited",
            "name": "Discovery Limited (Johannesburg-listed)",
            "type": "listed-company",
            "country": "ZA",
            "note": "Currency of sponsor name is ambiguous: 'Vitality' most commonly means the Discovery-owned brand (UK VitalityHealth/VitalityLife are Discovery subsidiaries). If the sponsor is instead US 'Vitality' (John Hancock/Manulife) the owner is likewise a listed insurer and the tier stays none. Flagged rather than picked silently."
        },
        "claim": {
            "text": "The Vitality brand is owned worldwide by Discovery Limited, a Johannesburg-headquartered, JSE-listed financial services group; Discovery states it is the licensed controlling company of the Discovery insurance group and owns the core Vitality IP. No state or state-fund owner.",
            "short": "The Vitality brand is owned worldwide by Discovery Limited, a Johannesburg-headquartered, JSE-listed financial services group; Discovery states it is the licensed….",
            "source": {
                "name": "Discovery Limited corporate site; Discovery Holdings press release (Vitality name change)",
                "date": "2025",
                "url": "https://www.discovery.co.za/"
            }
        },
        "verdict": "Owned by Discovery Limited (Johannesburg-listed). Nothing found.",
        "confidence": "medium",
        "note": "Currency of sponsor name is ambiguous: 'Vitality' most commonly means the Discovery-owned brand (UK VitalityHealth/VitalityLife are Discovery subsidiaries). If the sponsor is instead US 'Vitality' (John Hancock/Manulife) the owner is likewise a listed insurer and the tier stays none. Flagged rather than picked silently."
    },
    {
        "sponsorId": "vodafone",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "vodafone-group-plc",
            "name": "Vodafone Group Plc — public shareholders (Niel family now largest holder)",
            "type": "listed-company",
            "country": "GB",
            "note": "Honesty flag: through most of the period the UAE state fund had a ~16% stake, which would have made this concern; it has now exited, so none. If the rubric freezes the e& period, this becomes concern (UAE state fund). e& state ownership: https://www.eia.gov.ae/"
        },
        "claim": {
            "text": "Vodafone is a London-listed telecoms group. Its largest shareholder was until 2026 Emirates Telecommunications (e&), itself ~60% held by the UAE state via the Emirates Investment Authority; e& agreed to sell its entire ~16.2% stake to Vega, a vehicle of the Niel family, and the sale has since completed. Owner is therefore listed/private with the state-fund link now exited.",
            "short": "Vodafone is a London-listed telecoms group.",
            "source": {
                "name": "Vodafone 'Response to e&'s announcement'; Reuters (Niel becomes Vodafone's top shareholder); e& H1 2026 results (sale completed)",
                "date": "2026-07-10 / 2026-H1",
                "url": "https://www.vodafone.com/news/newsroom/corporate-and-financial/response-to-announcement"
            }
        },
        "verdict": "Owned by Vodafone Group Plc — public shareholders (Niel family now largest holder). Nothing found.",
        "confidence": "medium",
        "note": "Honesty flag: through most of the period the UAE state fund had a ~16% stake, which would have made this concern; it has now exited, so none. If the rubric freezes the e& period, this becomes concern (UAE state fund). e& state ownership: https://www.eia.gov.ae/"
    }
]
