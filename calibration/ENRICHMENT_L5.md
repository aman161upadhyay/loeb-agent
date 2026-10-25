# L5 — historical financial and valuation enrichment

## Scope

Reviewed the 40 D02/D03/D04/D06 documents in the ten assigned packs. Added financial, latest-results, capital-stack/valuation and numeric industry tables where absent; retained the earlier numerical work in Potlatch/Ligand D02/D03 and the 2016/2021 packs rather than duplicating it. Corrected Potlatch FY2002 debt to include notes payable and the 2016 monthly S&P P/E observation.

No answer key, score, manifest, application code, canonical prompt or fund decision was changed. No new identifying target product, executive or subsidiary was introduced; metadata and alias lists were left unchanged.

## Coverage and remaining limitations

| Pack | Financial record | Latest public results | Valuation / comparison coverage |
|---|---|---|---|
| 2003 Potlatch | FY1998–2002; cash flow, capex, debt and equity | Q1 2003; detailed period figures retrieved from later SEC filing | May 1 close, debt/cash bridge, P/B, dividend/earnings yield, three historical peers; proxy industry ROE |
| 2005 Ligand | FY2000–2004 restated archival statements; explicitly not reliable contemporaneous audited accounts | Latest recovered original Q3 2004 release; restatement/delinquency preserved | Unadjusted September quote, approximate share-proxy EV, three stale year-end peer cap/P/B observations |
| 2007 Pogo | FY2002–2006; completed FY2006 retrieved from March filing, labelled archival | Q3 2006, not later fourth-quarter announcement | January close, September balance sheet, gain-distorted trailing P/E and three historical producer/major peers |
| 2008 portfolio | Fund AUM/returns plus five-year commodity/auto-demand context, not invented corporate statements | Q2/first-half fund results and interim July disclosure | Cutoff rates/VIX/index; credit collateral and tangible-book comparators |
| 2008 PDL | FY2003–2007 archival continuing perimeter | Corrected Q3 2007 GAAP results | January close, September balance sheet, P/B and three historical biotech peers |
| 2009 Chrysler Financial | Five-year standalone accounts unavailable; five-year industry-demand table and actual financing terms | Public Q1 funding observations, not fabricated quarterly earnings | Separate Treasury-SPV priority/coupon/maturity comparators; private claim quote remains unavailable |
| 2009 Delphi | FY2004–2008; FY2008 predecessor columns from archival statements, perimeter break labelled | Q1 2009, including nonrecurring reorganisation income and cash flow | A/B/C priority amounts and unresolved $47m repayment obligation; no later loan-entry quote or equity outcome |
| 2012 Greece | FY2007–2011 IMF vintage sovereign equivalents | June 8 Q1 GDP release and separately labelled IMF forecasts | Indicative 10-cent quote, PSI face/coupon/maturity terms and sovereign benchmarks; exact strip YTM unresolved |
| 2016 energy shorts | Existing FY2011–2015 regime record retained | Existing January EIA outlook/fund reporting retained | January 29 market comparators; monthly P/E corrected to 22.18× |
| 2021 venture/Upstart | Existing three prospectus fiscal years retained; five-year private-company history not recovered | Existing Q3 2020 prospectus results retained | Existing January 29 price/IPO bridge, rates/index and three peer multiples retained |

Unresolved cells remain explicit, not zero. Common gaps include early-year cash-flow/debt decompositions, tangible-capital returns, historical forward consensus, exact rolling 52-week ranges, some matched-date peer P/Es/dividend yields and private-credit execution prices. Three source attempts/families are identified beside the relevant unavailable fields. Private-company or portfolio records are not silently replaced with public-equity accounts.

## Source and accounting controls

- Primary SEC reports, corrected issuer releases, Treasury financing documents, GAO, IMF and PDMA support operating/capital-stack figures. Historical reporting periods retrieved from later archives are labelled, with no subsequent investor action or outcome imported.
- Historical unadjusted equity prices and index closes came from dated Exa market-history observations. FRED DGS10/VIXCLS supplied dated market risk/rate observations. Multpl monthly P/E observations are explicitly monthly, using completed earlier months for early-month cutoffs. Historical peer cap/P/B tables are identified as stale year-end CompaniesMarketCap observations, not same-day live multiples.
- FRED CSV observations were parsed and annual means calculated with Python for WTI and total vehicle sales. Direct CompaniesMarketCap HTTP requests returned 403; research-tool archive retrieval supplied the historical rows instead. Old HY-OAS rows were unavailable from the currently restricted FRED history and remain a gap, not an estimated spread.
- PDL commercial-disposal accounting and Delphi predecessor recasts create perimeter breaks; those are called out. Ligand's late archival financials are not represented as having resolved cutoff accounting uncertainty.
- Chrysler finance-SPV funding is not treated as the private claim under review or as automaker collateral. Delphi's $47m item is an unsatisfied repayment obligation, not completed repayment. Greece remains before the June 17 election.

## Static validation

All ten metadata files parse; all 40 target documents retain Title/Source/Date headers with the exact pack cutoff. All contain numeric tables; every D04 begins immediately after its header with the requested Key figures section. Documents remain within 300–1,100 words.

| Pack | D02 / D03 / D04 / D06 words | Entire pack bytes |
|---|---|---:|
| 2003_potlatch_escalate | 756 / 625 / 713 / 478 | 32,423 |
| 2005_ligand_buy | 748 / 650 / 731 / 488 | 32,262 |
| 2007_pogo_escalate | 719 / 513 / 742 / 489 | 30,431 |
| 2008_derisk | 715 / 555 / 702 / 508 | 30,397 |
| 2008_pdl_escalate | 654 / 549 / 707 / 508 | 31,118 |
| 2009_chrysler_finco_buy | 719 / 553 / 723 / 502 | 30,505 |
| 2009_delphi_buy | 792 / 578 / 787 / 554 | 33,479 |
| 2012_greece_buy | 715 / 621 / 810 / 549 | 34,712 |
| 2016_energy_shorts_cover | 668 / 555 / 686 / 597 | 35,923 |
| 2021_venture_book | 664 / 568 / 807 / 556 | 36,041 |

All packs remain below 48KB. No application or workflow was run or restarted; no prediction or scoring run was performed.
