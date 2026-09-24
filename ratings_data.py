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
        "sponsorId": "arctempus",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "arctempus",
            "name": "ARCTEMPUS (Arctempus Capital / Grupo StarOneRocket)",
            "type": "private-company",
            "country": "ES",
            "note": "RCD Espanyol's 20 Aug 2026 confirmation names ARCTEMPUS as main sponsor. Private, IESE-linked business network; the Espanyol owner Alan Pace is a counterparty, not an owner."
        },
        "claim": {
            "text": "ARCTEMPUS is a Madrid-based private real-estate, investment and asset-management group formed by merging Star1Rocket, Bestflat and Zenhia; the group is privately held with co-founders Luis Miguel Real and Marc Sarnito and CEO Gonzalo Lopez behind it. No state or sovereign-fund participation is disclosed.",
            "short": "ARCTEMPUS is a Madrid-based private real-estate, investment and asset-management group formed by merging Star1Rocket, Bestflat and Zenhia; the group is privately….",
            "source": {
                "name": "La Grada (Espanyol specialist outlet) - 'ARCTEMPUS Capital sera el nuevo patrocinador del Espanyol'; RCD Espanyol official announcement",
                "date": "2026-08-20",
                "url": "https://lagrada.org/arctempus-capital-patrocinador-espanyol-alan-pace-iese/"
            }
        },
        "verdict": "Owned by ARCTEMPUS (Arctempus Capital / Grupo StarOneRocket). Nothing found.",
        "confidence": "medium",
        "note": "RCD Espanyol's 20 Aug 2026 confirmation names ARCTEMPUS as main sponsor. Private, IESE-linked business network; the Espanyol owner Alan Pace is a counterparty, not an owner."
    },
    {
        "sponsorId": "baghdadi-capital",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "baghdadi-capital-sa",
            "name": "Baghdadi Capital, S.A. (family office of Baihas Baghdadi)",
            "type": "private-company",
            "country": "ES",
            "note": "Name suggests Iraq/Iranian links but ownership is Spanish private family capital. Manages ~EUR 1.5bn AUM across Spain, US, UK, Ireland, Singapore."
        },
        "claim": {
            "text": "Baghdadi Capital, S.A. describes itself as a 'global independent corporate and investment banking family office' founded in February 2023 by Spanish entrepreneur Baihas Baghdadi; it states it is a '100% Spanish family office'. Founder is of Syrian heritage but the entity has no state or sovereign-fund shareholder.",
            "short": "Baghdadi Capital, S.A.",
            "source": {
                "name": "Baghdadi Capital, S.A. official 'Who We Are' page",
                "date": "2026-01",
                "url": "https://baghdadicapital.com/en/"
            }
        },
        "verdict": "Owned by Baghdadi Capital, S.A. (family office of Baihas Baghdadi). Nothing found.",
        "confidence": "high",
        "note": "Name suggests Iraq/Iranian links but ownership is Spanish private family capital. Manages ~EUR 1.5bn AUM across Spain, US, UK, Ireland, Singapore."
    },
    {
        "sponsorId": "barmenia",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "barmenia-versicherungen-ag",
            "name": "Barmenia Versicherungen a.G. (BarmeniaGothaer Group)",
            "type": "private-company",
            "country": "DE",
            "note": "German mutual 'a.G.' structure; Barmenia holds 36% and Gothaer 64% of the joint holding after the 2023/24 merger. No state capital."
        },
        "claim": {
            "text": "Barmenia Versicherungen a.G. is a German mutual insurer (Versicherungsverein auf Gegenseitigkeit) based in Wuppertal and now the leading entity of the BarmeniaGothaer group alongside Gothaer Versicherungsbank VVaG. As a mutual it is owned by its policyholder members, not by shareholders or the state.",
            "short": "Barmenia Versicherungen a.G.",
            "source": {
                "name": "BarmeniaGothaer Group annual report 2025 (Konzerngeschaeftsbericht) / Barmenia legal notice",
                "date": "2025",
                "url": "https://www.barmeniagothaer.de/infos-zur-gruppe/"
            }
        },
        "verdict": "Owned by Barmenia Versicherungen a.G. (BarmeniaGothaer Group). Nothing found.",
        "confidence": "high",
        "note": "German mutual 'a.G.' structure; Barmenia holds 36% and Gothaer 64% of the joint holding after the 2023/24 merger. No state capital."
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
        "sponsorId": "beumer-group",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "beumer-group",
            "name": "BEUMER Group GmbH & Co. KG",
            "type": "private-company",
            "country": "DE",
            "note": "Almost 90 years old, family-run, no listed float, no state stake."
        },
        "claim": {
            "text": "BEUMER Group is a family-owned German intralogistics/conveying systems group based in Beckum; its own main-partner announcement for FC Schalke 04 (from 2026/27) describes it as 'the global family-owned company from Beckum'.",
            "short": "BEUMER Group is a family-owned German intralogistics/conveying systems group based in Beckum; its own main-partner announcement for FC Schalke 04 (from 2026/27)….",
            "source": {
                "name": "FC Schalke 04 official press release 'BEUMER Group to become FC Schalke 04's new main partner'",
                "date": "2026-04-22",
                "url": "https://schalke04.de/en/partner-en/beumer-group-new-main-partner"
            }
        },
        "verdict": "Owned by BEUMER Group GmbH & Co. KG. Nothing found.",
        "confidence": "high",
        "note": "Almost 90 years old, family-run, no listed float, no state stake."
    },
    {
        "sponsorId": "c-hedenkamp",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "c-hedenkamp-gmbh",
            "name": "C. Hedenkamp GmbH & Co. KG",
            "type": "private-company",
            "country": "DE",
            "note": "Small mittelstand firm; family owners in the register. No state link."
        },
        "claim": {
            "text": "C. Hedenkamp GmbH & Co. KG of Hoevelhof (Paderborn registry) is a family-owned German building-materials/construction supplier; the commercial register shows it is controlled via Hedenkamp Verwaltungs GmbH by Wolf Karsten Hedenkamp, Klaus Dietrich Hedenkamp and Markus Hedenkamp.",
            "short": "C.",
            "source": {
                "name": "C. Hedenkamp GmbH & Co. KG official Imprint / Handelsregister entry",
                "date": "2026",
                "url": "https://www.hedenkamp.de/en/impressum/"
            }
        },
        "verdict": "Owned by C. Hedenkamp GmbH & Co. KG. Nothing found.",
        "confidence": "high",
        "note": "Small mittelstand firm; family owners in the register. No state link."
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
        "sponsorId": "corendon",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "corendon-tourism-group",
            "name": "Corendon Tourism Group (Corendon Holdings)",
            "type": "private-company",
            "country": "NL",
            "note": "Dutch/Turkish dual footprint, so some sources treat it as Turkish; ownership is private founder/family either way. CEO Gunay Uslu (Atilay's relative) is a former Dutch state secretary, which is a personnel not ownership link."
        },
        "claim": {
            "text": "Corendon Airlines is a subsidiary of the privately held Corendon Tourism Group, founded in 2000 by Atilay Uslu and Yildiray Karaer; Uslu is listed as owner/founder and chairman. Dutch-headquartered (Amsterdam) group with Turkish operations; no state shareholding.",
            "short": "Corendon Airlines is a subsidiary of the privately held Corendon Tourism Group, founded in 2000 by Atilay Uslu and Yildiray Karaer; Uslu is listed as owner/founder….",
            "source": {
                "name": "Corendon Airlines corporate profile / TravMagazine reporting on Corendon management",
                "date": "2024-01",
                "url": "https://www.travmagazine.nl/en/corendon-introduces-its-new-management-team"
            }
        },
        "verdict": "Owned by Corendon Tourism Group (Corendon Holdings). Nothing found.",
        "confidence": "medium",
        "note": "Dutch/Turkish dual footprint, so some sources treat it as Turkish; ownership is private founder/family either way. CEO Gunay Uslu (Atilay's relative) is a former Dutch state secretary, which is a personnel not ownership link."
    },
    {
        "sponsorId": "deel",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "deel-inc",
            "name": "Deel, Inc.",
            "type": "private-company",
            "country": "US",
            "note": "US SEC investigation into revenue/accounting and a US money-laundering lawsuit have been reported, but these are company-level regulatory matters, not a state-ownership link, so tier stays none. No parent company above Deel, Inc."
        },
        "claim": {
            "text": "Deel, Inc. is a privately held US (Delaware/San Francisco) global payroll and EOR company; it is venture-backed with a $300m Series E at a $17.3bn valuation co-led by Ribbit Capital and Andreessen Horowitz, and has no sovereign or state shareholder on its cap table.",
            "short": "Deel, Inc.",
            "source": {
                "name": "Deel official blog 'Our Series E: Building the global infrastructure of work'; FinTech Global coverage",
                "date": "2025-10-17",
                "url": "https://www.deel.com/blog/new-investment-valuation/"
            }
        },
        "verdict": "Owned by Deel, Inc.. Nothing found.",
        "confidence": "high",
        "note": "US SEC investigation into revenue/accounting and a US money-laundering lawsuit have been reported, but these are company-level regulatory matters, not a state-ownership link, so tier stays none. No parent company above Deel, Inc."
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
        "sponsorId": "digi",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "digi-communications-nv",
            "name": "Digi Communications N.V.",
            "type": "listed-company",
            "country": "RO",
            "note": "Romanian listing plus US/Nasdaq-style ADRs; ownership private/founder with public float. Founder-linked governance litigation exists but no state link."
        },
        "claim": {
            "text": "Digi Communications N.V. is a Dutch-incorporated, Bucharest-listed (BSE: DIGI) telecoms group and the controlling shareholder of Digi Romania (formerly RCS & RDS). Founder Zoltan Teszari is the controlling shareholder; the rest is free float. No state or state-fund stake.",
            "short": "Digi Communications N.V.",
            "source": {
                "name": "Digi Communications N.V. official 'About Us' / Board of Directors (Teszari, controlling shareholder)",
                "date": "2026",
                "url": "https://www.digi-communications.ro/en/about-us"
            }
        },
        "verdict": "Owned by Digi Communications N.V.. Nothing found.",
        "confidence": "high",
        "note": "Romanian listing plus US/Nasdaq-style ADRs; ownership private/founder with public float. Founder-linked governance litigation exists but no state link."
    },
    {
        "sponsorId": "estrella-galicia",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "corporacion-hijos-de-rivera",
            "name": "Corporacion Hijos de Rivera, S.L.",
            "type": "private-company",
            "country": "ES",
            "note": "Fifth-generation family group (Rivera family). No state or fund capital."
        },
        "claim": {
            "text": "Estrella Galicia is the flagship beer brand of Corporacion Hijos de Rivera, which describes itself as a family-owned international brewing group with '100% national and independent capital', headquartered in A Coruna since 1906.",
            "short": "Estrella Galicia is the flagship beer brand of Corporacion Hijos de Rivera, which describes itself as a family-owned international brewing group with '100%….",
            "source": {
                "name": "Corporacion Hijos de Rivera official company page; Estrella Galicia International 'independent family-owned brewery'",
                "date": "2026",
                "url": "http://corporacionhijosderivera.com/en/company"
            }
        },
        "verdict": "Owned by Corporacion Hijos de Rivera, S.L.. Nothing found.",
        "confidence": "high",
        "note": "Fifth-generation family group (Rivera family). No state or fund capital."
    },
    {
        "sponsorId": "flexicar",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "flexicar-internacional",
            "name": "Flexicar Internacional (owner Luis Oliver Cornago)",
            "type": "private-company",
            "country": "ES",
            "note": "Single-owner private group, ~180 dealerships in Spain/Portugal. Not the unrelated Australian Hertz franchise."
        },
        "claim": {
            "text": "Flexicar is Spain's largest used-car dealer network, majority owned by founder Luis Oliver Cornago, who reorganized the group under Flexicar Internacional and injected EUR 7.6m of his own funds; company registry/legal form is private (Flexicar, empresa privada).",
            "short": "Flexicar is Spain's largest used-car dealer network, majority owned by founder Luis Oliver Cornago, who reorganized the group under Flexicar Internacional and….",
            "source": {
                "name": "El Confidencial - 'Flexicar fusiona sus firmas bajo el paraguas internacional'; Spanish Wikipedia 'Flexicar (Espana)'",
                "date": "2025-01-17",
                "url": "https://www.elconfidencial.com/empresas/2025-01-17/flexicar-fusiona-sociedades-batir-facturacion_4044206/"
            }
        },
        "verdict": "Owned by Flexicar Internacional (owner Luis Oliver Cornago). Nothing found.",
        "confidence": "high",
        "note": "Single-owner private group, ~180 dealerships in Spain/Portugal. Not the unrelated Australian Hertz franchise."
    },
    {
        "sponsorId": "fundacion-1890",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "fundacion-1890",
            "name": "Fundacion 1890 (Sevilla FC Foundation)",
            "type": "private-company",
            "country": "ES",
            "note": "The on-shirt 'Fundacion 1890' branding is a stopgap/charitable placement paying the club's own foundation; not a state or fund sponsor."
        },
        "claim": {
            "text": "Fundacion 1890 is the non-profit foundation arm of Sevilla FC, renamed from 'Fundacion Sevilla FC' in June 2025; it took the club's 1890 founding date. It is a private-law entity controlled by Sevilla FC (itself owned by Sevillistas de Nervion S.A.), with no public/state endowment.",
            "short": "Fundacion 1890 is the non-profit foundation arm of Sevilla FC, renamed from 'Fundacion Sevilla FC' in June 2025; it took the club's 1890 founding date.",
            "source": {
                "name": "Diario de Sevilla - 'La Fundacion 1890, nueva cara solidaria del Sevilla'; Sevilla FC official foundation page",
                "date": "2025-06-09",
                "url": "https://www.diariodesevilla.es/sevillafc/fundacion-1890-nueva-cara-solidaria-sevilla-fc-poligono-sur_0_2004112018.html"
            }
        },
        "verdict": "Owned by Fundacion 1890 (Sevilla FC Foundation). Nothing found.",
        "confidence": "medium",
        "note": "The on-shirt 'Fundacion 1890' branding is a stopgap/charitable placement paying the club's own foundation; not a state or fund sponsor."
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
        "sponsorId": "gree",
        "tier": "concern",
        "ownership": "owned",
        "owner": {
            "id": "gree-group-zhuhai-sasac",
            "name": "Gree Group Co., Ltd. (Zhuhai Municipal Government / Zhuhai SASAC)",
            "type": "state",
            "country": "CN",
            "note": "Chinese appliance maker, so Xinjiang/forced-labour questions attach to the wider PRC SOE supply chain but no Gree-specific adverse finding was located: hence concern (partial state ownership) rather than serious. Owner type 'state' (municipal SASAC), country CN."
        },
        "claim": {
            "text": "Gree Electric Appliances Inc. of Zhuhai (SZSE: 000651) is described as a majority state-owned enterprise principally by the city of Zhuhai; its historic largest shareholder, state-owned Gree Group, was owned by the Zhuhai Municipal People's Government. In December 2019 Gree Group sold most of its stake to the private equity vehicle Zhuhai Mingjun, leaving partial (not controlling) state ownership.",
            "short": "Gree Electric Appliances Inc.",
            "source": {
                "name": "Zhuhai Gree Group company history (state-owned nature change); Shenzhen Stock Exchange filings on the 2019 Gree Group/Zhuhai Mingjun share transfer",
                "date": "2024-06-08",
                "url": "http://static.cninfo.com.cn/finalpage/2024-06-08/1220300050.PDF"
            }
        },
        "verdict": "Gree Electric Appliances Inc.",
        "confidence": "medium",
        "note": "Chinese appliance maker, so Xinjiang/forced-labour questions attach to the wider PRC SOE supply chain but no Gree-specific adverse finding was located: hence concern (partial state ownership) rather than serious. Owner type 'state' (municipal SASAC), country CN."
    },
    {
        "sponsorId": "halo",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "halo-lifestyle-llc",
            "name": "Halo Lifestyle LLC (HALO Hydration)",
            "type": "private-company",
            "country": "US",
            "note": "Not to be confused with HALO Water Systems or Halo Sports. Small US private brand, no parent group."
        },
        "claim": {
            "text": "HALO Hydration is the trading brand of HALO Lifestyle LLC, a New York/US private company founded in 2017 by Anshuman Vohra and Robin Shobin; it is venture-backed (including celebrity investors such as Andy Murray and Pitbull) with no state or sovereign-fund ownership.",
            "short": "HALO Hydration is the trading brand of HALO Lifestyle LLC, a New York/US private company founded in 2017 by Anshuman Vohra and Robin Shobin; it is venture-backed….",
            "source": {
                "name": "Preqin asset profile for Halo Hydration; Crunchbase legal-name record (HALO LIFESTYLE LLC)",
                "date": "2025",
                "url": "https://www.preqin.com/data/profile/asset/halo-hydration/624618"
            }
        },
        "verdict": "Owned by Halo Lifestyle LLC (HALO Hydration). Nothing found.",
        "confidence": "medium",
        "note": "Not to be confused with HALO Water Systems or Halo Sports. Small US private brand, no parent group."
    },
    {
        "sponsorId": "hansemerkur",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "hansemerkur-krankenversicherung-ag",
            "name": "HanseMerkur Krankenversicherung a.G. (HanseMerkur Group)",
            "type": "private-company",
            "country": "DE",
            "note": "German mutual insurer. No state or listed-shareholder ownership."
        },
        "claim": {
            "text": "HanseMerkur is Germany's only independent, group-independent mid-sized personal insurer in Hamburg and is structured as a Versicherungsverein auf Gegenseitigkeit (mutual); HanseMerkur Krankenversicherung auf Gegenseitigkeit remains the owner of the group, owing duties only to customers and staff, not shareholders.",
            "short": "HanseMerkur is Germany's only independent, group-independent mid-sized personal insurer in Hamburg and is structured as a Versicherungsverein auf Gegenseitigkeit….",
            "source": {
                "name": "HanseMerkur official company/facts page (mutual structure); HanseMerkur 150-year corporate history",
                "date": "2025",
                "url": "https://vertriebskarriere.hansemerkur.de/das-unternehmen/zahlen-fakten"
            }
        },
        "verdict": "Owned by HanseMerkur Krankenversicherung a.G. (HanseMerkur Group). Nothing found.",
        "confidence": "high",
        "note": "German mutual insurer. No state or listed-shareholder ownership."
    },
    {
        "sponsorId": "hylo",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "ursapharm-arzneimittel-gmbh",
            "name": "URSAPHARM Arzneimittel GmbH",
            "type": "private-company",
            "country": "DE",
            "note": "URSAPHARM is the owner of the HYLO trademark (USPTO registration 5887500 in its name). Not HYLO the drink brand."
        },
        "claim": {
            "text": "HYLO is the flagship dry-eye brand of URSAPHARM Arzneimittel GmbH, a privately held, family/mittelstand German pharmaceutical and medical-device maker headquartered in Saarbrucken, founded 1974 and still independent after 50 years.",
            "short": "HYLO is the flagship dry-eye brand of URSAPHARM Arzneimittel GmbH, a privately held, family/mittelstand German pharmaceutical and medical-device maker….",
            "source": {
                "name": "URSAPHARM Arzneimittel GmbH official company profile and 50th-anniversary release",
                "date": "2024-04-08",
                "url": "https://ursapharm.de/en/press/company-profile/"
            }
        },
        "verdict": "Owned by URSAPHARM Arzneimittel GmbH. Nothing found.",
        "confidence": "medium",
        "note": "URSAPHARM is the owner of the HYLO trademark (USPTO registration 5887500 in its name). Not HYLO the drink brand."
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
        "sponsorId": "knox-hydration",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "knox-hydrate-pty-ltd",
            "name": "Knox Hydrate (Pty) Ltd",
            "type": "private-company",
            "country": "ZA",
            "note": "Task asked for a parent: there is none - KNOX is its own ultimate parent, founder-owned. Now Newcastle United front-of-shirt sponsor (~GBP 60m/3yr)."
        },
        "claim": {
            "text": "Knox Hydration/KNOX Hydrate is a South African sports-drinks company founded in 2024 and based in Cape Town, co-founded and co-owned by former UFC middleweight champion Dricus du Plessis and Australian entrepreneur Ethan Hughes. It has no parent company above it - it is founder-owned private capital.",
            "short": "Knox Hydration/KNOX Hydrate is a South African sports-drinks company founded in 2024 and based in Cape Town, co-founded and co-owned by former UFC middleweight….",
            "source": {
                "name": "Cape Argus / Independent Media interview with KNOX boss Ethan Hughes; The Athletic on the Newcastle United deal",
                "date": "2026-04-20",
                "url": "https://capeargus.co.za/sport/mma/2026-04-20-ufc-africa-and-newcastle-united-knox-hydration-working-to-bring-global-giants-to-sa"
            }
        },
        "verdict": "Owned by Knox Hydrate (Pty) Ltd. Nothing found.",
        "confidence": "medium",
        "note": "Task asked for a parent: there is none - KNOX is its own ultimate parent, founder-owned. Now Newcastle United front-of-shirt sponsor (~GBP 60m/3yr)."
    },
    {
        "sponsorId": "koemmerling",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "profine-gmbh",
            "name": "profine GmbH (owner Dr Peter A. Mrosik / Hidden Peak Capital)",
            "type": "private-company",
            "country": "DE",
            "note": "The Bahraini link is the former owner Arcapita, a Bahraini private bank - not the Bahraini state itself, so no state link at owner level."
        },
        "claim": {
            "text": "Koemmerling is a brand of profine GmbH, the Pirmasens PVC-window-systems group. profine was sold by Bahrain's Arcapita Bank to the Frankfurt private equity firm Hidden Peak Capital, and Dr Peter A. Mrosik is owner and CEO, so the group is privately held rather than state-backed.",
            "short": "Koemmerling is a brand of profine GmbH, the Pirmasens PVC-window-systems group.",
            "source": {
                "name": "Koemmerling/profine official press release 'profine GmbH has a new owner'; profine Group corporate site (Mrosik, owner and CEO)",
                "date": "2024-10-07",
                "url": "https://www.koemmerling.com/en/news-and-media/press/news/profine-gmbh-has-a-new-owner/"
            }
        },
        "verdict": "Owned by profine GmbH (owner Dr Peter A. Mrosik / Hidden Peak Capital). Nothing found.",
        "confidence": "medium",
        "note": "The Bahraini link is the former owner Arcapita, a Bahraini private bank - not the Bahraini state itself, so no state link at owner level."
    },
    {
        "sponsorId": "kosner",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "grupo-saltoki",
            "name": "Grupo Saltoki (Comercial de Suministros, S.A.)",
            "type": "private-company",
            "country": "ES",
            "note": "Brand-origin trivia: the Kosner trademark itself originated in Lyon, France, and the construction-equipment arm joined the French Euromair-Mixer group in 2023, while the HVAC sponsorship sits with Saltoki. Both possible owners are private; no state link either way."
        },
        "claim": {
            "text": "Kosner is a Spanish HVAC/air-conditioning brand whose products are distributed exclusively through Grupo Saltoki's centres; Saltoki itself states it is Kosner's exclusive distributor and the party that drove the Osasuna sponsorship. Grupo Saltoki is a private Navarra-based family distributorship.",
            "short": "Kosner is a Spanish HVAC/air-conditioning brand whose products are distributed exclusively through Grupo Saltoki's centres; Saltoki itself states it is Kosner's….",
            "source": {
                "name": "Saltoki official blog - 'Kosner, marca de climatizacion distribuida por Saltoki, patrocinara a Osasuna'",
                "date": "2023-02-10",
                "url": "https://www.saltoki.com/blog/kosner-climatizacion-patrocinador-osasuna"
            }
        },
        "verdict": "Owned by Grupo Saltoki (Comercial de Suministros, S.A.). Nothing found.",
        "confidence": "medium",
        "note": "Brand-origin trivia: the Kosner trademark itself originated in Lyon, France, and the construction-equipment arm joined the French Euromair-Mixer group in 2023, while the HVAC sponsorship sits with Saltoki. Both possible owners are private; no state link either way."
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
        "sponsorId": "kutxabank",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "kutxabank-sa",
            "name": "Kutxabank, S.A. (owned by BBK, Kutxa and Vital foundations)",
            "type": "private-company",
            "country": "ES",
            "note": "Flagged for proper look because savings-bank ownership feels public; legally the owners are private foundations, so none rather than concern. Not listed (no IPO; the foundations' reserve funds keep it unlisted)."
        },
        "claim": {
            "text": "Kutxabank S.A. is controlled 57% by BBK Fundacion Bancaria, 32% by Kutxa and 11% by Vital - the three former Basque savings banks, now private-law banking foundations. A banking foundation is a private entity (not a state or sovereign fund), so Kutxabank's owner is private even though the foundations pursue public-benefit goals.",
            "short": "Kutxabank S.A.",
            "source": {
                "name": "Kutxabank consolidated interim report 2024 (parent/ownership); El Correo - shareholder breakdown 57/32/11",
                "date": "2024-06-30",
                "url": "https://www.kutxabank.eus/cs/Satellite?blobcol=urldata&blobheadername1=Expires&blobheadervalue4=inline%3B++filename%3D%22Inf+Semestral+KB+consol+30-06-2024_EN.PDF%22"
            }
        },
        "verdict": "Owned by Kutxabank, S.A. (owned by BBK, Kutxa and Vital foundations). Nothing found.",
        "confidence": "medium",
        "note": "Flagged for proper look because savings-bank ownership feels public; legally the owners are private foundations, so none rather than concern. Not listed (no IPO; the foundations' reserve funds keep it unlisted)."
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
        "sponsorId": "lexware",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "haufe-group-se",
            "name": "Haufe Group SE (Haufe-Lexware)",
            "type": "private-company",
            "country": "DE",
            "note": "Privately held, family-controlled group; ~500 staff at Lexware, part of Haufe Group SE."
        },
        "claim": {
            "text": "Lexware is the accounting-software brand of Haufe-Lexware GmbH & Co. KG, whose parent is the family-owned Haufe Group SE of Freiburg (HRA 4408). Haufe Group is described as a family-managed German B2B technology/publishing group - no state or fund ownership.",
            "short": "Lexware is the accounting-software brand of Haufe-Lexware GmbH & Co.",
            "source": {
                "name": "Haufe-Lexware fact sheet 2024; Handelsregisterauszug HRA 4408 (Haufe-Lexware GmbH & Co. KG)",
                "date": "2024",
                "url": "https://www.lexware.de/fileadmin/pressematerial/factsheet_lexware_2024.pdf"
            }
        },
        "verdict": "Owned by Haufe Group SE (Haufe-Lexware). Nothing found.",
        "confidence": "high",
        "note": "Privately held, family-controlled group; ~500 staff at Lexware, part of Haufe Group SE."
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
        "sponsorId": "matthaei",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "matthaei-gruppe",
            "name": "Matthaei Gruppe (Matthaei Holding)",
            "type": "private-company",
            "country": "DE",
            "note": "Family/mittelstand building group; ownership not unit-listed, no state stake found."
        },
        "claim": {
            "text": "Matthaei is a German road-building/construction contractor headquartered in Verden (Aller) that became SV Werder Bremen's main and shirt sponsor from 2023/24; it is a privately held mittelstand group with no disclosed state participation.",
            "short": "Matthaei is a German road-building/construction contractor headquartered in Verden (Aller) that became SV Werder Bremen's main and shirt sponsor from 2023/24; it….",
            "source": {
                "name": "Matthaei official press release announcing the Werder Bremen main sponsorship; Matthaei group site",
                "date": "2023-02-10",
                "url": "https://www.matthaei.de/news/2023/matth%C3%A4i-wird-neuer-haupt-und-trikotsponsor-des-sv-werder-41657"
            }
        },
        "verdict": "Owned by Matthaei Gruppe (Matthaei Holding). Nothing found.",
        "confidence": "medium",
        "note": "Family/mittelstand building group; ownership not unit-listed, no state stake found."
    },
    {
        "sponsorId": "mk-tiyu-news",
        "tier": "unrated",
        "ownership": "owned",
        "owner": {
            "id": "mk-sports-news",
            "name": "mk体育 / MKSPORTS News (mktynews.com)",
            "type": "unknown",
            "country": "CN",
            "note": "Honest unrated: the sponsor is real and named, but ownership is opaque and no reliable primary source identifies the ultimate owner club or whether any Chinese state entity is involved."
        },
        "claim": {
            "text": "Deportivo Alaves' Asian main sponsor, now branded 'MK体育NEWS (mktynews.com)' after a 2026 rebrand, is a Chinese sports-media/marketing platform. Its corporate owner could not be pinned down reliably: mktynews.com is a WordPress sports-news site and the many 'mk体育' Chinese portals give conflicting corporate narratives (founded 2010 vs 1995/1996 vs 2012, Nanning vs Chengdu vs Guangdong), with no registry-level shareholder disclosure.",
            "short": "Deportivo Alaves' Asian main sponsor, now branded 'MK体育NEWS (mktynews.com)' after a 2026 rebrand, is a Chinese sports-media/marketing platform.",
            "source": {
                "name": "Deportivo Alaves official club news on the sponsor rebrand; mktynews.com",
                "date": "2026-07",
                "url": "https://deportivoalaves.com/noticias/el-patrocinador-principal-del-deportivo-alaves-renueva-su-marca-para-la-proxima-temporada"
            }
        },
        "verdict": "Deportivo Alaves' Asian main sponsor, now branded 'MK体育NEWS (mktynews.com)' after a 2026 rebrand, is a Chinese sports-media/marketing platform.",
        "confidence": "low",
        "note": "Honest unrated: the sponsor is real and named, but ownership is opaque and no reliable primary source identifies the ultimate owner club or whether any Chinese state entity is involved."
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
        "sponsorId": "pamesa-ceramica",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "pamesa-grupo-empresarial",
            "name": "Pamesa Grupo Empresarial (Fernando Roig)",
            "type": "private-company",
            "country": "ES",
            "note": "Family/owner-controlled Castellon ceramics group (~EUR 1.2bn revenue). Roig's Villarreal link is separate."
        },
        "claim": {
            "text": "Pamesa Ceramica states it is the parent company of Grupo Pamesa, the Castellon ceramic-tile group; the group is controlled by Spanish billionaire Fernando Roig Alfonso (also owner/president of Villarreal CF) and is privately held with no state or fund shareholder.",
            "short": "Pamesa Ceramica states it is the parent company of Grupo Pamesa, the Castellon ceramic-tile group; the group is controlled by Spanish billionaire Fernando Roig….",
            "source": {
                "name": "Pamesa Ceramica official corporate page ('Pamesa Ceramica is the parent company of the Pamesa Group'); Focus Piedra interview with Fernando Roig",
                "date": "2021-2024",
                "url": "https://www.pamesa.com/en/CORPORATIVO.html"
            }
        },
        "verdict": "Owned by Pamesa Grupo Empresarial (Fernando Roig). Nothing found.",
        "confidence": "high",
        "note": "Family/owner-controlled Castellon ceramics group (~EUR 1.2bn revenue). Roig's Villarreal link is separate."
    },
    {
        "sponsorId": "plenitude",
        "tier": "concern",
        "ownership": "owned",
        "owner": {
            "id": "eni-spa",
            "name": "Eni S.p.A. (Plenitude S.p.A. subsidiary)",
            "type": "listed-company",
            "country": "IT",
            "note": "Flagged for proper look: the Italian state stake in Eni sits below 50% and via a listed parent, so concern rather than serious. Claims of Eni human-rights/environmental harm (Niger Delta, OPL 245) are contested and partly settled, supporting concern not serious."
        },
        "claim": {
            "text": "Plenitude is Eni's retail/renewables division; Eni is listed on Borsa Italiana and NYSE but the Italian Ministry of Economy and Finance plus CDP S.p.A. together hold 33.09% of its share capital, i.e. a state link at the owner. Eni is restructuring/deconsolidating Plenitude with Ares (20%) and EIP (10%), leaving Eni around 65%.",
            "short": "Plenitude is Eni's retail/renewables division; Eni is listed on Borsa Italiana and NYSE but the Italian Ministry of Economy and Finance plus CDP S.p.A.",
            "source": {
                "name": "Eni official shareholder-structure page (MEF + CDP = 33.09%); Eni press release on deconsolidation of Plenitude",
                "date": "2026-03-19",
                "url": "https://www.eni.com/en-IT/governance/shareholding-structure.html"
            }
        },
        "verdict": "Plenitude is Eni's retail/renewables division; Eni is listed on Borsa Italiana and NYSE but the Italian Ministry of Economy and Finance plus CDP S.p.A.",
        "confidence": "high",
        "note": "Flagged for proper look: the Italian state stake in Eni sits below 50% and via a listed parent, so concern rather than serious. Claims of Eni human-rights/environmental harm (Niger Delta, OPL 245) are contested and partly settled, supporting concern not serious."
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
        "sponsorId": "raisin",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "raisin-gmbh",
            "name": "Raisin GmbH (Raisin DS)",
            "type": "private-company",
            "country": "DE",
            "note": "Bank investors are minority VC/strategic stakes, so the owner stays private-company with no state link (Orange Ventures is Orange SA, itself only partly French state-owned - not counted)."
        },
        "claim": {
            "text": "Raisin (Weltsparen) is a Berlin fintech formed by the 2021 merger of Deposit Solutions and Raisin GmbH; it is privately held and VC-backed by investors including Goldman Sachs, Deutsche Bank, Index Ventures, Kinnevik, PayPal Ventures and Thrive Capital. No state or sovereign-fund shareholder.",
            "short": "Raisin (Weltsparen) is a Berlin fintech formed by the 2021 merger of Deposit Solutions and Raisin GmbH; it is privately held and VC-backed by investors including….",
            "source": {
                "name": "Fintech Consult company profile listing Raisin's investor base; Raisin corporate (XING/Lusha) company description",
                "date": "2026",
                "url": "https://fintech-consult.com/europe/germany/fintech/raisin/"
            }
        },
        "verdict": "Owned by Raisin GmbH (Raisin DS). Nothing found.",
        "confidence": "medium",
        "note": "Bank investors are minority VC/strategic stakes, so the owner stays private-company with no state link (Orange Ventures is Orange SA, itself only partly French state-owned - not counted)."
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
        "sponsorId": "reuter",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "reuter-gruppe",
            "name": "REUTER Gruppe (Reuter family)",
            "type": "private-company",
            "country": "DE",
            "note": "Group HQ Moenchengladbach; expansion into Italy in 2024. No state or fund ownership."
        },
        "claim": {
            "text": "REUTER is Germany's largest online bathroom-products retailer, a family-run business founded by craftsman Bernd Reuter, who turned his trade business into an online shop in 2004; it became Borussia Moenchengladbach's main sponsor from 2024/25 and remains privately owned.",
            "short": "REUTER is Germany's largest online bathroom-products retailer, a family-run business founded by craftsman Bernd Reuter, who turned his trade business into an….",
            "source": {
                "name": "REUTER official company history page ('The family-run company is Borussia Moenchengladbach's new main sponsor'); LogInfo24 on founder Bernd Reuter",
                "date": "2024",
                "url": "https://www.reuter.com/company/about-us/our-history.html"
            }
        },
        "verdict": "Owned by REUTER Gruppe (Reuter family). Nothing found.",
        "confidence": "high",
        "note": "Group HQ Moenchengladbach; expansion into Italy in 2024. No state or fund ownership."
    },
    {
        "sponsorId": "rewe",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "rewe-group",
            "name": "REWE Group (REWE cooperatives eG)",
            "type": "private-company",
            "country": "DE",
            "note": "Type stays private-company because the owner list only allows state/state-fund/listed/private/unknown and an eG is private. (Note: country set DE - see note.)"
        },
        "claim": {
            "text": "REWE Group is a German retail and travel group organized as a two-tier cooperative: it is owned by six regional cooperatives (eG) including Hungen eG, West eG, Sued/Suedwest eG, Nord/Ost eG and Dortmund eG, plus Fuer Sie Handelsgenossenschaft eG. Cooperative members - independent retailers - are the owners; no external shareholder or state stake.",
            "short": "REWE Group is a German retail and travel group organized as a two-tier cooperative: it is owned by six regional cooperatives (eG) including Hungen eG, West eG,….",
            "source": {
                "name": "REWE Group official 'Cooperative' page and investor presentation (REWE COOPERATIVES / six owner cooperatives)",
                "date": "2024-07",
                "url": "https://www.rewe-group.com/en/cooperative/"
            }
        },
        "verdict": "Owned by REWE Group (REWE cooperatives eG). Nothing found.",
        "confidence": "high",
        "note": "Type stays private-company because the owner list only allows state/state-fund/listed/private/unknown and an eG is private. (Note: country set DE - see note.)"
    },
    {
        "sponsorId": "sabor-a-malaga",
        "tier": "concern",
        "ownership": "owned",
        "owner": {
            "id": "diputacion-de-malaga",
            "name": "Diputacion Provincial de Malaga",
            "type": "state",
            "country": "ES",
            "note": "Sub-national government owner (not a sovereign state, not a state fund) maps to concern as a lesser link. Currently front-of-shirt sponsor of Malaga CF (since 2021)."
        },
        "claim": {
            "text": "Sabor a Malaga is not a company but a promotional quality brand owned and run by the Diputacion Provincial de Malaga, the provincial public administration; the brand is used by the Diputacion to promote the province's agri-food products and licenses its use to producers. The owner is therefore a public body - a lesser/sub-national state link.",
            "short": "Sabor a Malaga is not a company but a promotional quality brand owned and run by the Diputacion Provincial de Malaga, the provincial public administration; the….",
            "source": {
                "name": "Sabor a Malaga official site (a brand of the Diputacion de Malaga); Diputacion de Malaga trademark-use resolution",
                "date": "2026",
                "url": "https://www.saboramalaga.es/en/news/blog/sabor-a-malaga-proud-official-sponsor-of-malaga-cf-since-2021-p54384"
            }
        },
        "verdict": "Sabor a Malaga is not a company but a promotional quality brand owned and run by the Diputacion Provincial de Malaga, the provincial public administration; the….",
        "confidence": "high",
        "note": "Sub-national government owner (not a sovereign state, not a state fund) maps to concern as a lesser link. Currently front-of-shirt sponsor of Malaga CF (since 2021)."
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
        "sponsorId": "sesame-hr",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "sesame-hr-sl",
            "name": "Sesame HR (Sesame HR S.L.)",
            "type": "private-company",
            "country": "ES",
            "note": "BBVA Spark is a bank lending facility, not equity, and BBVA has no state stake - so owner remains private-company, tier none."
        },
        "claim": {
            "text": "Sesame HR is a Valencia-based HR-software scale-up founded 2015 and held privately/VC-backed: Series A led by PSG Equity, a later EUR 23m round led by GP Bullhound with PSG, and a EUR 50m debt facility from BBVA Spark. No state or sovereign-fund shareholder.",
            "short": "Sesame HR is a Valencia-based HR-software scale-up founded 2015 and held privately/VC-backed: Series A led by PSG Equity, a later EUR 23m round led by GP Bullhound….",
            "source": {
                "name": "PSG Equity press release on Sesame's EUR 23m round; GP Bullhound Fund VI announcement",
                "date": "2024-05-08",
                "url": "https://psgequity.com/news/sesame-closes-new-investment-round-of-23m-to-continue-its-investment-in-ai-and-accelerate-international-expansion"
            }
        },
        "verdict": "Owned by Sesame HR (Sesame HR S.L.). Nothing found.",
        "confidence": "high",
        "note": "BBVA Spark is a bank lending facility, not equity, and BBVA has no state stake - so owner remains private-company, tier none."
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
        "sponsorId": "spotify",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "spotify-technology-sa",
            "name": "Spotify Technology S.A.",
            "type": "listed-company",
            "country": "SE",
            "note": "Flagged for proper look: the Tencent (~8%) stake is the only non-Western notable holder and Tencent itself is not state-controlled - so none, not concern."
        },
        "claim": {
            "text": "Spotify is listed on the NYSE (SPOT); it has a dual-class structure with a large free float and no single controlling shareholder (founder Daniel Ek holds supervoting shares; Tencent holds ~8%, institutions ~67%). No state or sovereign-fund control - Longbridge's holder breakdown puts state-owned-enterprise holdings at well under 1%.",
            "short": "Spotify is listed on the NYSE (SPOT); it has a dual-class structure with a large free float and no single controlling shareholder (founder Daniel Ek holds….",
            "source": {
                "name": "Spotify Technology S.A. SEC ownership filings (CIK 0001639920); Spotify 2025 annual filing",
                "date": "2026",
                "url": "https://www.sec.gov/cgi-bin/own-disp?CIK=0001639920&action=getissuer&sortid=type-of-owner-DESC"
            }
        },
        "verdict": "Owned by Spotify Technology S.A.. Nothing found.",
        "confidence": "high",
        "note": "Flagged for proper look: the Tencent (~8%) stake is the only non-Western notable holder and Tencent itself is not state-controlled - so none, not concern."
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
        "sponsorId": "tecnocasa-group",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "tecnocasa-holding-spa",
            "name": "Tecnocasa Holding S.p.A.",
            "type": "private-company",
            "country": "IT",
            "note": "Private Italian holding, founding-franchise structured; not listed, no state capital found."
        },
        "claim": {
            "text": "Tecnocasa Group is an Italian real-estate and credit brokerage franchisor operated by Tecnocasa Holding S.p.A. (Rozzano, Milan), privately held and unlisted; it runs franchise networks across Italy, Spain, Hungary and beyond, with no disclosed state or fund ownership.",
            "short": "Tecnocasa Group is an Italian real-estate and credit brokerage franchisor operated by Tecnocasa Holding S.p.A.",
            "source": {
                "name": "Tecnocasa Group official corporate site (Tecnocasa Holding Spa, P.IVA 08365140154)",
                "date": "2026",
                "url": "https://www.tecnocasagroup.com/"
            }
        },
        "verdict": "Owned by Tecnocasa Holding S.p.A.. Nothing found.",
        "confidence": "medium",
        "note": "Private Italian holding, founding-franchise structured; not listed, no state capital found."
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
        "sponsorId": "tm-real-estate-group",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "tm-grupo-inmobiliario",
            "name": "TM Grupo Inmobiliario (Serna family)",
            "type": "private-company",
            "country": "ES",
            "note": "Not related to the unrelated US 'TM Real Estate Group LLC'. Family-held Alicante developer operating in Spain and Mexico."
        },
        "claim": {
            "text": "TM Real Estate Group is the Alicante-based resort developer TM Grupo Inmobiliario, described on its own site as a family company set up by Jose Luis Serna Almodovar; it is family-owned private capital with no state or fund shareholder.",
            "short": "TM Real Estate Group is the Alicante-based resort developer TM Grupo Inmobiliario, described on its own site as a family company set up by Jose Luis Serna….",
            "source": {
                "name": "TM Grupo Inmobiliario official 'About us' page (family company, Alicante)",
                "date": "2026",
                "url": "https://www.tmgrupoinmobiliario.com/en/about-us"
            }
        },
        "verdict": "Owned by TM Grupo Inmobiliario (Serna family). Nothing found.",
        "confidence": "high",
        "note": "Not related to the unrelated US 'TM Real Estate Group LLC'. Family-held Alicante developer operating in Spain and Mexico."
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
    },
    {
        "sponsorId": "wwk",
        "tier": "none",
        "ownership": "owned",
        "owner": {
            "id": "wwk-lebensversicherung-ag",
            "name": "WWK Lebensversicherung a.G. (WWK Versicherungsgruppe)",
            "type": "private-company",
            "country": "DE",
            "note": "Founded 1884 in Munich; 140-year mutual insurer with a real-estate subsidiary. No state or listed-shareholder ownership."
        },
        "claim": {
            "text": "WWK Versicherungen is a Munich mutual insurance group in which WWK Lebensversicherung a.G. is the mutual parent company owning WWK Allgemeine Versicherung AG, WWK Pensionsfonds AG and WWK Investment SA; as a Versicherungsverein a.G. it is owned by its members, not shareholders or the state.",
            "short": "WWK Versicherungen is a Munich mutual insurance group in which WWK Lebensversicherung a.G.",
            "source": {
                "name": "WWK insurer profile (WWK Lebensversicherung a.G. as mutual parent); WWK corporate history",
                "date": "2026",
                "url": "https://boleron.eu/en/germany/insurer/wwk"
            }
        },
        "verdict": "Owned by WWK Lebensversicherung a.G. (WWK Versicherungsgruppe). Nothing found.",
        "confidence": "medium",
        "note": "Founded 1884 in Munich; 140-year mutual insurer with a real-estate subsidiary. No state or listed-shareholder ownership."
    }
]
