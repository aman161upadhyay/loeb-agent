# Prompt change log (every change names the calibration case that motivated it)

## v1.0 — 2026-10-25
- Initial AGENT.md and prompt chain written from the archive (letters, 13Ds, decks, X posts to 1 Aug 2025) before any pack was run.
- Carried over from the Ackman adversarial review (ackman-agent/adversarial/): (a) the fact sheet records document conflicts and
  Gate 1 must resolve them; (b) step 7 may not overturn a Gate 1 hard fail; (c) masked runs are labelled "name-masked", not
  "blind"; (d) controls and sells are run three times and reported by majority.

## v1.1 — 2026-10-25 (carried over from the Buffett smoke tests; before any scored calibration run)
- 08_sell_hold, 09_hedge: require 3-5 drivers ordered by importance (sibling chain returned one or two drivers in these modes).
- AGENT.md Gate 5: added the 2011 allocator-diligence sizing evidence (top longs 5-7%, shorts 2-4%, ~2% probability-weighted downside
  guideline) as dated Era B description, not a cap.
- Calibration packs were found to be thin on prices/multiples (D04); fixed by the numbers-desk enrichment pass (calibration/ENRICHMENT_*.md).
- Smoke tests (2011_yahoo_buy, 2014_dow_buy → BUY but catalyst_role P0; 2013_hlf_buy → PASS as an E7 short): 02_gate1 E2 now names the
  crowded-short squeeze long explicitly; 05_gate4 forbids P0 for E1 and gives the P1-vs-P2 test with dated examples; 07_decision_memo copies
  plan_role from Gate 4 instead of showing a "P0" placeholder the model was echoing.

## v1.2 — 2026-10-25 (after scored calibration batch 1: 2003-2009 packs)
- Motivating cases: 2005_ligand_buy and 2005_massey_buy (Gate 1 hard-failed "edge", "governance route", "downside floor" and
  "management credibility" because the pack held no plan, no settlement precedent and a loss-making year — in Era A/B the plan
  was Third Point's letter and the bad management was the opportunity); 2009_chrysler_finco_buy (credit claim failed "size and
  liquidity" for having no equity denominator and "management credibility" for being run under a government process);
  2003_potlatch_escalate, 2007_pogo_escalate, 2008_pdl_escalate named (HOLD "catalyst in progress" where Loeb wrote the letter or
  nominated a majority).
- 02_gate1: situation-type scoring rules — E1 in Era A/B (the plan is Third Point's to write; entrenched management is
  electable, hence PASS; asset floor at the management discount), E3 credit (score the claim: coverage, buyable size, process);
  missing data is UNSURE, and UNSURE never counts toward a hard fail.
- 08_sell_hold: ESCALATE is the Era A/B default for an underperforming 13D position, with the dated triggers; Era C/E escalation
  only after private engagement was ignored.

## v1.3 — 2026-10-25 (after calibration batch 2-3: 2011-2018 packs)
- Motivating cases: 2013_hlf_sell (HOLD named / ADD masked where Loeb sold most of the position into the Q1 repricing); 2013_hlf_buy
  masked (Gate 1 typed the squeeze long as an E7 short and hard-failed "governance" and "floor" on the pyramid-scheme tail);
  2016_energy_shorts_cover (HEDGE vs REDUCE_GROSS: label semantics).
- 08_sell_hold L1: an E2 technical position is sold/trimmed into the repricing within weeks, whatever the state of the argument.
- 02_gate1: E2 squeeze-long scoring rule (type, technical path as the route, the business as the floor, the tail sized not gated).
- 09_hedge: the label follows gross exposure (covering shorts = REDUCE_GROSS; adding protection = HEDGE).
- Not changed: 2015_bax_buy named PASS (all six criteria UNSURE, Gate 2 NO_EDGE; masked run bought with 3/4 drivers) — run-to-run
  variance, reported.

## v1.4 — 2026-10-25 (after calibration batches 4-5: 2018-2025 packs)
- Motivating cases: 2023_ai_basket_buy (Gate 1 hard-failed an E4 basket on "no governance route" and "crowded consensus");
  2022_cl_buy named (hard fail: "no nomination window, no activist precedent" for a large-cap under-earner; masked run bought
  3/4); 2020_pcg_buy masked (Gate 2 NO_EDGE because of the Fire Victim Trust overhang — the overhang is the mispricing).
- 02_gate1: scoring rules for E4/E5 (no route needed; edge = early and specific; "crowded" needs evidence), E1 in Era C/E large
  caps (route = engagement; edge = the arithmetic), and post-reorg/overhang E2/E3 cases.
- Not changed: 2022_intc_sell and 2023_dis_sell2 (keys inferred from 13F absence, calibration_eligible = false, no stated
  rationale; graded direction-only and reported); 2018_nestle_escalate masked ADD (PARTIAL).

## v1.5 — 2026-10-25 (after the first control run under v1.4: 6 of 10 controls returned BUY)
- Motivating cases: ctl_2012_best_buy_pass (BUY 6%, "80% : 0%" skew on a declining retailer), ctl_2018_ge_pass (BUY with Trian
  already on the board and unbounded insurance liabilities), ctl_2019_newell_pass (BUY in Starboard/Icahn's fight, 6x
  levered), ctl_2024_ba_pass (BUY on a multi-year safety turnaround), ctl_2015_endo_pass, ctl_2016_groupon_pass, ctl_2023_frc_pass
  masked (BUY into a deposit run). The v1.2-v1.4 loosening of Gate 1 for Era A/B activism and E4 had removed the business-quality
  test that keeps most "cheap and under-earning" names out of Third Point's 13Fs.
- 02_gate1: five discipline tests (melting ice cube with the separable-asset/sale exception; someone else's fight; unknowable
  liabilities; leverage on a shrinking base; multi-year operational turnaround as the only lever → trade size or PASS).
- 04_gate3: the downside is never 0%; COMPELLING requires a real floor.
- (v1.5, harness) The Gate 1 hard-fail flag is recomputed in code from the criteria scores (ctl_2019_newell_pass named: FAIL on
  "downside_floor" and "management_credibility" with hard_fail = false from the model); tools/run_agent.py does the same.
- (v1.5, second pass) 02_gate1: sixth discipline test — the adjusted-earnings roll-up is the short template (ctl_2015_endo_pass BUY on
  "AMS divestiture cash as the floor" with GAAP EPS of −$4.91). Packs ctl_2018_ge_pass and ctl_2019_newell_pass gained D09 docs
  (facts on the record the workers had omitted). Prompts frozen after this change.
