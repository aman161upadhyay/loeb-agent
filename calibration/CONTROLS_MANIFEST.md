# Controls manifest — common-stock discipline tests

Archive audit: 2026-10-25. The request says nine controls but enumerates nine plus the additional bankrupt-equity control: **ten packs** are supplied. PASS is an observational calibration label for a reportable common-stock opportunity, not a claim that Loeb published a rejected-idea memo. None of these controls establishes absolute economic nonownership across swaps, shorts, intra-quarter transactions, offshore instruments or credit. This limitation is in every key.

|trade_id|as_of_date|mode|era|actual decision|one-line basis|grade|
|---|---|---|---|---|---|---|
|ctl_2012_best_buy_pass|2012-02-01|new|B|PASS|Replacement after original issuer/instrument found in history; replacement absent in audited tables.|C|
|ctl_2015_endo_pass|2015-03-02|new|B|PASS|Replacement after original issuer/instrument found in history; replacement absent in audited tables.|C|
|ctl_2016_groupon_pass|2016-10-10|new|C|PASS|Replacement after original issuer/instrument found in history; replacement absent in audited tables.|C|
|ctl_2018_ge_pass|2018-10-01|new|C|PASS|No reportable holding in audited window; no named rejection invented.|C|
|ctl_2019_newell_pass|2019-02-22|new|C|PASS|Replacement after original issuer/instrument found in history; replacement absent in audited tables.|C|
|ctl_2021_gme_amc_pass|2021-01-27|new|C|PASS|No reportable holding in audited window; no named rejection invented.|C|
|ctl_2022_vroom_pass|2022-11-04|new|C|PASS|Replacement after original issuer/instrument found in history; replacement absent in audited tables.|C|
|ctl_2023_frc_pass|2023-03-16|new|C|PASS|No reportable holding in audited window; no named rejection invented.|C|
|ctl_2024_ba_pass|2024-01-08|new|C|PASS|No reportable holding in audited window; no named rejection invented.|C|
|ctl_2020_hertz_equity_pass|2020-06-08|new|C|PASS|Legacy common absent only in 2020 window; credit/other periods explicitly excluded.|C|

## Candidate corrections — why five were replaced

|Requested id|Replacement id|Verified contradictory history|
|---|---|---|
|ctl_2012_jcp_pass|ctl_2012_best_buy_pass|The complete Q2 2012 primary 13F reports PENNEY J C INC, CUSIP 708160106, puts on 9,000,000 shares, value 6480 in the $000 column. The filing's option valuation convention is unresolved; no premium or risk estimate is inferred.|
|ctl_2015_vrx_pass|ctl_2015_endo_pass|Valeant common reported Q1 2014; peak reported value $32.958M. Replaced conservatively despite being outside the proposed 2015 date.|
|ctl_2016_twtr_pass|ctl_2016_groupon_pass|Twitter common reported Q3 2022, $241.120M; later ownership makes issuer-wide never-held wording false.|
|ctl_2019_kraft_heinz_pass|ctl_2019_newell_pass|Kraft Heinz common reported Q3 2015–Q1 2016; peak reported value $582.285M.|
|ctl_2022_cvna_pass|ctl_2022_vroom_pass|Carvana common reported Q1 2021, $104.960M. The April 2025 manager report also names Carvana among YTD detractors despite no later row in the 13F index, illustrating why a negative 13F cannot exclude non-reportable exposure.|

### Original JCP primary-source audit

Full texts were retrieved, not inferred from the 2013-onward index. Q3/Q4 2011 and all four 2012 original tables plus the Q2 amendment were checked. Best Buy does not appear in any. JCP is absent Q3/Q4 2011 and Q1/Q3/Q4 2012 but present through puts in Q2 2012. Sources:
- 2013-02-14; period 2012-12-31: https://www.sec.gov/Archives/edgar/data/1040273/000108514613000612/thirdpoint4q2012.txt
- 2012-11-14; period 2012-09-30: https://www.sec.gov/Archives/edgar/data/1040273/000108514612001484/thirdpoint3q2012.txt
- 2012-10-02; period 2012-06-30: https://www.sec.gov/Archives/edgar/data/1040273/000108514612001179/thirdpoint2q2012a1.txt
- 2012-08-14; period 2012-06-30: https://www.sec.gov/Archives/edgar/data/1040273/000108514612001123/thirdpoint2q2012r5.txt
- 2012-05-15; period 2012-03-31: https://www.sec.gov/Archives/edgar/data/1040273/000108514612000807/thirdpoint1q2012.txt
- 2012-02-14; period 2011-12-31: https://www.sec.gov/Archives/edgar/data/1040273/000108514612000452/tpt4q2011.txt
- 2011-11-14; period 2011-09-30: https://www.sec.gov/Archives/edgar/data/1040273/000108514611001255/tpt3q2011.txt

### Remaining controls and instrument scope

- All replacement issuers, GE, GME, AMC, FRC and Boeing were searched against the complete 54-quarter issuer/instrument ledger, not a top-holdings page: [all_positions_index.md](../compendium/all_positions_index.md). Its linked source register preserves the underlying quarterly filings and repaired pagination. Manager history cross-check: https://13f.info/manager/0001040273-third-point-llc. Absence is evidence about reportable quarterly observations only.
- Hertz is **not** a never-held issuer. It is retained only because the requested case is specifically the May–June 2020 legacy bankrupt common, absent in that window. The index documents common in 2013–14, reorganized common 2021–23 and later warrants. The October 15, 2020 letter documents **pre-bankruptcy vehicle ABS**. That does not establish common ownership. Source: https://a.storyblok.com/f/166217/x/d9fcfd4dd1/third-point-q3-2020-investor-letter-tpoi.pdf. A grader requiring issuer-wide never-held controls must exclude this id, not mislabel the ABS holding.
- The February 10, 2021 Loeb comment on avoiding modest-liquidity/high-short-interest shorts is in the GME/AMC **key only**, clearly retrospective. It is not falsely dated January 27 and is not represented as a named long-stock rejection. Source: https://www.foxbusiness.com/markets/third-points-dan-loeb-talks-short-selling-madness.
- Silent cases say no attributable public comment **recovered**, not that an exhaustive search of every historical letter or X post proves silence. No fictional manager reasons, quotations or exact non-trade dates are supplied.

## Quality and data gaps

All ten controls are grade C: a genuine favorable event case and strong skeptical case are supplied, but exact cutoff closes, full peer tables and independently recovered firm/fund AUM are mostly missing. Metadata uses **null** for unrecovered control AUM as an explicit numeric-schema exception rather than fabricating assets or substituting 13F value. Eight documents each contain at least 300 words, with case-specific recovered evidence separated from conditional underwriting work. Header Date denotes the desk-date compilation; cited material must predate it. Research remains unsuitable for claiming measured entry IRRs or an exhaustive private-position audit.
