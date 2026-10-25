# L7 — control-pack financial and valuation enrichment

## Scope and controls

Enriched D02, D03, D04 and D06 in all ten assigned control packs: 40 documents. Original Title and cutoff Date headers are retained; original source URLs remain in the Source headers, with numerical-source extensions where required. Existing underwriting prose is retained except for statements contradicted by recovered data or an incorrect enterprise-value bridge.

No answer keys, manifests, grades, metadata, predictions, application code or scores were changed. No new subject brand, product or executive was introduced, so aliases required no additions. Peer companies are comparison subjects, not new aliases for the case company. No application or workflow was run.

## Coverage

| Pack | D02 financial record | D03 latest results | D04 / D06 numerical additions |
|---|---|---|---|
| ctl_2012_best_buy_pass | FY2007–11 sales, operating margins, NI/EPS, shares, dividends, debt/book, return proxy and four years of cash investment/FCF | Q3 FY2012 plus December trading and January 6 guidance | February 1 close/range, cap/EV, trailing/guidance P/E, book/yields, Treasury/S&P; Walmart, Target and Amazon valuations; retail financial comparisons |
| ctl_2015_endo_pass | FY2010–14 predecessor/current issuer record; acquisition/disposal perimeters distinguished | Q4 FY2014, reported/adjusted EPS and 2015 guidance | March 2 close and 52-week closing range, current share denominator, dated EV, book/yields; Teva, Perrigo and Pfizer; branded/generic/device revenue mix |
| ctl_2016_groupon_pass | FY2011–15 operating record, EPS/shares, common book and investment/FCF | Q2 2016 with GAAP/non-GAAP distinctions and annual guidance | October 10 close/range, convertible/net-cash bridge, book and yields; eBay, Amazon and TripAdvisor; industry operating comparisons |
| ctl_2018_ge_pass | FY2013–17 consolidated and industrial definitions, NI/EPS/dividends, book, returns, borrowings and cash investment | Q2 2018 and October 1 superseding guidance warning | October 1 close/range, dated debt including nonrecourse borrowing, book/dividend; Honeywell, 3M and Emerson; industrial segment scale/growth/margins |
| ctl_2019_newell_pass | FY2014–18 financial record with original versus restated continuing-perimeter caveats | Q4 FY2018 plus explicit 2019 sales/EPS/CFO outlook | February 22 close/range, average-share cap proxy, net debt/EV, book/dividend/FCF; Church & Dwight, Clorox and Spectrum; consumer-product comparisons |
| ctl_2020_hertz_equity_pass | FY2015–19 rights-adjusted EPS/shares, debt/book, fleet depreciation and three-year fleet-inclusive FCF | Q1 2020, utilization and bankruptcy chronology | June 8 old-common close, cap and dated funding bridge; Avis, Ryder and AMERCO; rental utilization/fleet comparisons |
| ctl_2021_gme_amc_pass | Separate five-year records for both companies, with fiscal-year, preferred-claim and goodwill distinctions | Last reported 2020 quarter for each; January 27 completed AMC offering | Original-unit prices/ranges; GME cap and AMC pro-forma 402.4m-share denominator; dated EV/book; Cinemark, Best Buy and IMAX; retail/exhibition comparisons |
| ctl_2022_vroom_pass | Five-year column layout; FY2018–21 flow record recovered, FY2017 flows explicitly missing; pre-IPO common-equity limitations | Q2 2022; sequential and annual comparisons separated | November 4 close and closing-price range; floorplan plus securitization debt included; book/FCF; Carvana Class A, CarMax and AutoNation; operating comparisons |
| ctl_2023_frc_pass | FY2018–22 bank record, NII, EPS/dividends, book/TBV and available capital/provision/quality ratios | Q4 2022 plus March 16 funding-rate, liquidity and dividend update | March 16 close/range, common cap, P/E and P/B/TBV; bank EV not treated as industrial EV; JPMorgan, Bank of America and Western Alliance; bank profitability/capital comparisons |
| ctl_2024_ba_pass | FY2018–22 operating record, common/tangible book, debt/cash and FCF | Q3 2023; old cash guidance explicitly not post-incident reaffirmation | January 8 close/range, cap/net-debt/EV and historical FCF yield; Lockheed, Northrop and General Dynamics; segment revenue/margin/backlog comparisons |

## Sources and point-in-time treatment

Primary sources are contemporaneous issuer releases and SEC annual/interim filings, with SEC companyfacts used to retrieve historical values whose filing dates precede the relevant cutoff. First Republic filed its annual report with the FDIC; its February 13, 2023 report was recovered through the Yale financial-stability archive, not fabricated from unavailable SEC companyfacts.

Historical Yahoo OHLC uses the units trading at each cutoff, reversing later split adjustments where necessary. Endo and Vroom ranges are explicitly **closing-price** ranges, not intraday extremes. Hertz's old-common June 8 close is a historical observation from the contemporaneous session report, whose page was subsequently updated; no later restructuring outcome is used. Treasury observations are dated FRED DGS10 values; Groupon uses October 7 because October 10 was a bond-market holiday. S&P P/E is a reconstructed historical reference for the last completed month, not future consensus.

Peer P/E generally uses the latest completed fiscal year's reported EPS, not a synchronized TTM or forward estimate. Historical DPS yields are labelled as such; suspended current dividends are not represented as payable. Estimated caps identify last-reported or average-share denominators. TripAdvisor uses an explicitly diluted-average-share cap proxy. Carvana's Class A cap/book comparison excludes the other economic ownership interests and is not presented as a whole-company equity value.

AMC's January 27 noon offering release is inside the cutoff and adds 63.3m shares to the January 22 A+B denominator. First Republic's March 16 update is after the regular close but on the cutoff date; this timing is explicit, including its common-dividend suspension. Borrowing-funded cash and the $30bn term deposits are not equity.

## Corrections and unresolved fields

- Corrected Endo's original acquisition-debt bridge: debt is added from equity value to EV and deducted from operating value to equity.
- Replaced superseded “cutoff price not recovered” statements where the new dated tables recover that price. Retained uncertainty over consensus, fully diluted claims and current fair-value/liquidation bridges.
- Distinguished Vroom's annual versus sequential growth, per-unit profit and net-loss comparisons. Its EV includes $422.452m vehicle floorplan funding as well as current/noncurrent securitization and other debt.
- GE's debt bridge includes separately classified nonrecourse borrowings. Annual segment/corporate operating proxies are not relabelled consolidated industrial GAAP EBIT.
- Exact five-year tangible-capital returns, some early cash-flow/debt components and synchronized forward consensus remain missing. Negative-equity return ratios are NM rather than mechanically meaningful positive ratios.
- Three-source attempts for gaps: BBY/Endo/GE/Newell/Hertz/GME/AMC/Boeing used SEC history, issuer annual/results archives and Macrotrends history; Groupon/Vroom used SEC filings, issuer releases and StockAnalysis history; First Republic used the FDIC-filed report, issuer releases and AnnualReports archive. Hertz's old-ticker range additionally failed recovery from Yahoo, issuer history and an Exa historical-series request.
- Hertz's 52-week range, BBY FY2007 cash-flow detail, Hertz FY2015–16 fleet cash-capex bridge, Vroom FY2017 flows and parts of First Republic's older ratio/book series remain explicit gaps. No placeholders were substituted.

## Static verification

All ten metadata JSON files parse. All 40 target documents retain the three-line header structure and their case cutoff dates, have numeric tables and remain within 300–1,100 words. Each D04 opens with a dated key-figures table and contains at least three external valuation peers. D02 contains the historical record; D03 the latest reported quarter; D06 a numeric comparison. Every complete pack remains below 48KB. Temporary research scripts were removed. No scoring or application execution was performed.
