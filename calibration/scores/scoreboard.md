# Scoreboard — replay of Third Point / Dan Loeb decisions (prompts v1.5, model: Replit internal current model)

> **Read this first.** These runs use the *current* internal model, which has training data that may include the outcomes of
> every calibration trade and most hold-out trades. They measure **prompt compliance and process plausibility** — whether the
> gate chain produces Loeb-shaped decisions and reasons from a point-in-time pack — not true out-of-sample fidelity. Fidelity
> evidence requires re-running `tools/run_agent.py` with the pre-dated Llama 3.1 8B (data to Dec 2023) on the Mac Mini: for
> every pack dated 2024-2026 that model cannot know the answer. The **masked** runs (company, ticker and aliases replaced by
> "the Company") are the closer proxy here; where named and masked disagree, memory is suspected.

Generated 2026-10-25. Scores: `calibration/scores/` (calibration + controls) and `calibration/scores/holdout/` (sealed set,
run once after the prompt freeze; prompts were never edited from hold-out results — `prompts/CHANGELOG.md`,
`calibration/PROMPT_HASHES_v1.5.txt`). Iteration-phase runs (v1.1-v1.5) are archived in `calibration/prefreeze/`. Grader:
`prompts/10_grader.md`; grounding share and the state rule (direction MATCH and k ≥ ⌈0.75·N⌉) are computed in code; the Gate 1
hard-fail flag is recomputed in code from the criteria scores and enforced (a BUY/SHORT after a hard fail becomes PASS).

## Summary (95% Wilson intervals)

| Set | n | Direction MATCH | Direction PARTIAL | Direction MISS | State MATCH | State PARTIAL | Driver overlap k/N (scorable keys) | Grounding (mean share) | Leakage flags |
|---|---|---|---|---|---|---|---|---|---|
| calibration named | 47 | 38 (81% [67%, 90%]) | 2 | 7 | 18 (38% [26%, 53%]) | 22 | 93/161 (58% [50%, 65%]) | 0.50 | 1 |
| calibration masked | 47 | 37 (79% [65%, 88%]) | 4 | 6 | 15 (32% [20%, 46%]) | 26 | 81/161 (50% [43%, 58%]) | 0.46 | 0 |
| discipline controls named (10 PASS keys) | 10 | 10 (100% [72%, 100%]) | 0 | 0 | 0 (0% [0%, 28%]) | 10 | – | 0.47 | 0 |
| discipline controls masked, majority of 3 | 10 | 9 (90% [60%, 98%]) | 0 | 1 | 0 (0% [0%, 28%]) | 9 | – | 0.60 | 0 |
| hold-out named | 11 | 5 (45% [21%, 72%]) | 1 | 5 | 0 (0% [0%, 26%]) | 6 | 7/38 (18% [9%, 33%]) | 0.49 | 0 |
| hold-out masked | 11 | 5 (45% [21%, 72%]) | 0 | 6 | 0 (0% [0%, 26%]) | 5 | 6/38 (16% [7%, 30%]) | 0.39 | 0 |

**Baselines (added after the adversarial review).** A mode-only baseline that answers BUY to every new-idea pack, ESCALATE to
every existing position and REDUCE_GROSS to every regime pack scores **41/47 (87%)** on calibration direction — above the
chain's 81% / 79% — and **0/10 on the controls**; a "BUY everything" baseline scores 30/47 and 0/10. The direction rate on a
set that is mostly things Loeb did is therefore not the evidence; the controls, the driver overlap and the state rule are. Read
the calibration direction column as "does the chain avoid saying no to Loeb's own trades", and the control column as "does it
say no to the rest".

Definitions: *direction* = same action as Loeb (BUY≈ADD; TRIM vs SELL = PARTIAL; regime labels ADD_RISK / REDUCE_GROSS / HEDGE /
NO_CHANGE must match; BUY with materially smaller size or a different instrument = PARTIAL); *state* MATCH = direction MATCH and
≥75% of the stated drivers reproduced; *driver overlap* = Loeb's stated reasons (letters, 13D letters, decks, interviews, in the
answer key) that the agent independently gave, pooled over keys with ≥3 stated drivers and calibration_eligible ≠ false
("scorable"). Four keys are inferred from 13F changes without a stated rationale (2016 energy shorts, 2022 Intel exit, 2023
Disney exit, 2023 AI basket; calibration_eligible = false) and are graded on direction only. Controls are "never held"
names with no stated reason, graded on direction only.

## By era (calibration, n = 47)

| Era | n | Direction MATCH named | Direction MATCH masked | State MATCH named | State MATCH masked |
|---|---|---|---|---|---|
| A 1995-2008 small-cap event-driven & the letters | 7 | 6 | 6 | 1 | 2 |
| B 2009-2015 credit cycle & large-cap constructivism | 16 | 13 | 13 | 10 | 9 |
| C 2016-mid 2025 quality, inflection, Japan, venture | 24 | 19 | 18 | 7 | 4 |

## By mode

| Mode | n | Direction MATCH named | Direction MATCH masked | State MATCH named | State MATCH masked |
|---|---|---|---|---|---|
| existing | 13 | 11 | 10 | 6 | 5 |
| portfolio regime (hedge) | 4 | 4 | 4 | 0 | 1 |
| new | 30 | 23 | 23 | 12 | 9 |

## Per-decision results — calibration

| id | company | as of | era | mode | key | named: decision / direction / state k/N | masked: decision / direction / state k/N | instrument / role / flags |
|---|---|---|---|---|---|---|---|---|
| 2003_potlatch_escalate | Potlatch Corporation | 2003-05-01 | A | existing | ESCALATE | ESCALATE / MATCH / MATCH 3/4 | ESCALATE / MATCH / PARTIAL 2/4 |  |
| 2005_ligand_buy | Ligand Pharmaceuticals Incor | 2005-09-30 | A | new | BUY | BUY / MATCH / PARTIAL 2/4 | BUY / MATCH / PARTIAL 1/4 | common P2 |
| 2005_massey_buy | Massey Energy Company | 2005-11-15 | A | new | BUY | PASS / MISS / MISS 0/4 | PASS / MISS / MISS 0/4 | common P0 HF |
| 2005_star_gas_escalate | Star Gas Partners L.P. | 2005-02-13 | A | existing | ESCALATE | ESCALATE / MATCH / PARTIAL 1/4 | ESCALATE / MATCH / MATCH 3/4 |  |
| 2007_pogo_escalate | Pogo Producing Company | 2007-01-31 | A | existing | ESCALATE | ESCALATE / MATCH / PARTIAL 2/4 | ESCALATE / MATCH / PARTIAL 2/4 |  |
| 2008_derisk | Third Point portfolio | 2008-09-30 | A | hedge | REDUCE_GROSS | REDUCE_GROSS / MATCH / PARTIAL 2/3 | REDUCE_GROSS / MATCH / MATCH 3/3 |  |
| 2008_pdl_escalate | PDL BioPharma Inc. | 2008-01-31 | A | existing | ESCALATE | ESCALATE / MATCH / PARTIAL 1/4 | ESCALATE / MATCH / PARTIAL 2/4 |  |
| 2009_chrysler_finco_buy | Chrysler Financial | 2009-05-01 | B | new | BUY | BUY / PARTIAL / PARTIAL 1/4 | BUY / MATCH / MATCH 3/4 | bond P0 |
| 2009_delphi_buy | Delphi Corporation | 2009-06-01 | B | new | BUY | BUY / MATCH / PARTIAL 1/4 | BUY / MATCH / MATCH 3/4 | bond P5 |
| 2011_yahoo_buy | Yahoo! Inc. | 2011-09-07 | B | new | BUY | BUY / MATCH / MATCH 3/4 | BUY / MATCH / PARTIAL 1/4 | common P2 |
| 2012_greece_buy | Hellenic Republic post-PSI b | 2012-06-15 | B | new | BUY | PASS / MISS / MISS 1/4 | BUY / MATCH / PARTIAL 1/4 | bond P0 HF enforced |
| 2012_yahoo_escalate | Yahoo! Inc. | 2012-05-03 | B | existing | ESCALATE | ESCALATE / MATCH / MATCH 3/4 | ESCALATE / MATCH / MATCH 3/4 |  |
| 2013_hlf_buy | Herbalife Ltd. | 2013-01-08 | B | new | BUY | BUY / PARTIAL / PARTIAL 4/4 | BUY / PARTIAL / PARTIAL 3/4 | common P0 |
| 2013_hlf_sell | Herbalife Ltd. | 2013-03-01 | B | existing | TRIM | TRIM / MATCH / MATCH 3/3 | TRIM / MATCH / MATCH 3/3 |  |
| 2013_sony_buy | Sony Corporation | 2013-05-13 | B | new | BUY | BUY / MATCH / MATCH 3/4 | BUY / MATCH / MATCH 3/4 | common P2 |
| 2013_sothebys_buy | Sotheby's | 2013-08-26 | B | new | BUY | BUY / MATCH / PARTIAL 3/5 | BUY / PARTIAL / PARTIAL 2/5 | common P2 |
| 2013_yahoo_sell | Yahoo! Inc. | 2013-07-22 | B | existing | TRIM | TRIM / MATCH / MATCH 3/3 | TRIM / MATCH / MATCH 3/3 |  |
| 2014_amgn_buy | Amgen Inc. | 2014-10-21 | B | new | BUY | BUY / MATCH / MATCH 4/4 | BUY / MATCH / MATCH 3/4 | common P1 |
| 2014_dow_buy | The Dow Chemical Company | 2014-01-21 | B | new | BUY | BUY / MATCH / MATCH 3/4 | BUY / MATCH / PARTIAL 2/4 | common P2 |
| 2014_sony_sell | Sony Corporation | 2014-10-20 | B | existing | SELL | SELL / MATCH / MATCH 3/3 | SELL / MATCH / MATCH 3/3 |  |
| 2015_bax_buy | Baxter International Inc. | 2015-08-05 | B | new | BUY | BUY / MATCH / MATCH 3/4 | PASS / MISS / MISS 0/4 | common P1 |
| 2015_fanuc_buy | FANUC Corporation | 2015-02-10 | B | new | BUY | BUY / MATCH / PARTIAL 3/5 | BUY / MATCH / PARTIAL 3/5 | common P1 |
| 2015_seven_i_buy | Seven & i Holdings Co., Ltd. | 2015-10-26 | B | new | BUY | BUY / MATCH / MATCH 3/4 | BUY / MATCH / MATCH 3/4 | common P1 |
| 2016_energy_shorts_cover | Third Point thematic energy  | 2016-01-31 | C | hedge | REDUCE_GROSS | REDUCE_GROSS / MATCH / PARTIAL (0/3, dir-only) | REDUCE_GROSS / MATCH / PARTIAL (0/3, dir-only) |  |
| 2017_hon_buy | Honeywell International Inc. | 2017-04-27 | C | new | BUY | BUY / MATCH / PARTIAL 2/3 | BUY / MATCH / PARTIAL 0/3 | common P1 |
| 2017_nestle_buy | Nestlé S.A. | 2017-06-25 | C | new | BUY | BUY / MATCH / MATCH 4/5 | BUY / MATCH / MATCH 4/5 | common P1 |
| 2018_cpb_buy | Campbell Soup Company | 2018-08-09 | C | new | BUY | PASS / MISS / MISS 0/3 | BUY / MATCH / PARTIAL 2/3 | common P0 HF |
| 2018_nestle_escalate | Nestlé S.A. | 2018-07-01 | C | existing | ESCALATE | ESCALATE / MATCH / MATCH 3/4 | ADD / PARTIAL / PARTIAL 1/4 |  |
| 2018_utx_buy | United Technologies Corporat | 2018-05-04 | C | new | BUY | BUY / MATCH / MATCH 3/3 | BUY / MATCH / MATCH 3/3 | common P1 |
| 2019_sony_buy2 | Sony Corporation | 2019-06-13 | C | new | BUY | BUY / MATCH / MATCH 3/4 | BUY / MATCH / MATCH 3/4 | common P1 |
| 2020_dis_buy | The Walt Disney Company | 2020-10-07 | C | new | BUY | BUY / MATCH / PARTIAL 1/3 | BUY / MATCH / PARTIAL 0/3 | common P1 |
| 2020_intc_buy | Intel Corporation | 2020-12-29 | C | new | BUY | BUY / MATCH / PARTIAL 1/4 | BUY / MATCH / PARTIAL 0/4 | common P2 |
| 2020_pcg_buy | PG&E Corporation | 2020-07-01 | C | new | BUY | BUY / MATCH / PARTIAL 2/3 | BUY / MATCH / PARTIAL 2/3 | common P0 |
| 2020_pru_buy | Prudential plc | 2020-02-24 | C | new | BUY | BUY / MATCH / MATCH 3/4 | BUY / MATCH / MATCH 4/4 | common P2 |
| 2020_q1_derisk | Third Point portfolio pandem | 2020-03-16 | C | hedge | REDUCE_GROSS | REDUCE_GROSS / MATCH / PARTIAL 1/3 | REDUCE_GROSS / MATCH / PARTIAL 0/3 |  |
| 2021_shel_buy | Royal Dutch Shell plc | 2021-10-27 | C | new | BUY | BUY / MATCH / MATCH 3/3 | PASS / MISS / MISS 0/3 | common P2 |
| 2021_venture_book | Upstart Holdings, Inc. post- | 2021-01-31 | C | existing | HOLD | HOLD / MATCH / PARTIAL 1/3 | HOLD / MATCH / PARTIAL 2/3 |  |
| 2022_bbwi_buy | Bath & Body Works, Inc. | 2022-09-30 | C | new | BUY | PASS / MISS / MISS 0/3 | PASS / MISS / MISS 0/3 | common P1 |
| 2022_cl_buy | Colgate-Palmolive Company | 2022-10-31 | C | new | BUY | BUY / MATCH / PARTIAL 2/4 | BUY / PARTIAL / PARTIAL 2/4 | common P1 |
| 2022_dis_buy2 | The Walt Disney Company | 2022-08-15 | C | new | BUY | BUY / MATCH / PARTIAL 3/5 | BUY / MATCH / PARTIAL 0/5 | common P1 |
| 2022_growth_cut | Third Point growth, venture  | 2022-03-31 | C | hedge | REDUCE_GROSS | REDUCE_GROSS / MATCH / PARTIAL 1/4 | REDUCE_GROSS / MATCH / PARTIAL 1/4 |  |
| 2022_intc_sell | Intel Corporation | 2022-01-31 | C | existing | SELL | HOLD / MISS / MISS (0/3, dir-only) | HOLD / MISS / MISS (0/3, dir-only) |  |
| 2023_ai_basket_buy | AI infrastructure and incumb | 2023-04-30 | C | new | BUY | BUY / MATCH / PARTIAL (0/4, dir-only) | BUY / MATCH / PARTIAL (0/4, dir-only) | common P0 |
| 2023_dis_sell2 | The Walt Disney Company | 2023-02-08 | C | existing | SELL | HOLD / MISS / MISS (0/3, dir-only) | HOLD / MISS / MISS (0/3, dir-only) |  |
| 2024_vst_buy | Vistra Corp. | 2024-04-30 | C | new | BUY | BUY / MATCH / MATCH 3/4 | BUY / MATCH / PARTIAL 2/4 | common P0 |
| 2025_csgp_buy | CoStar Group, Inc. | 2025-03-31 | C | new | BUY | PASS / MISS / MISS 1/3 | BUY / MATCH / PARTIAL 2/3 | common P0 HF |
| 2025_shco_buy | Soho House & Co Inc. | 2025-01-28 | C | existing | ESCALATE | ESCALATE / MATCH / PARTIAL 1/3 | ESCALATE / MATCH / PARTIAL 1/3 |  |

## Discipline controls (never-held names at value-looking moments)

| id | company | as of | key | named decision (discipline) | masked votes (3 runs) | Gate 1 hard fail (named) |
|---|---|---|---|---|---|---|
| ctl_2012_best_buy_pass | Best Buy | 2012-02-01 | PASS | PASS (NA) | PASS 3/3 | yes |
| ctl_2015_endo_pass | Endo International | 2015-03-02 | PASS | PASS (NA) | BUY 2/3 | yes |
| ctl_2016_groupon_pass | Groupon | 2016-10-10 | PASS | PASS (NA) | PASS 3/3 | yes |
| ctl_2018_ge_pass | General Electric | 2018-10-01 | PASS | PASS (NA) | PASS 3/3 | yes |
| ctl_2019_newell_pass | Newell Brands | 2019-02-22 | PASS | PASS (NA) | PASS 3/3 | no |
| ctl_2020_hertz_equity_pass | Hertz Global Holdings — pre- | 2020-06-08 | PASS | PASS (NA) | PASS 2/3 | yes |
| ctl_2021_gme_amc_pass | GameStop and AMC Entertainme | 2021-01-27 | PASS | PASS (NA) | PASS 3/3 | yes |
| ctl_2022_vroom_pass | Vroom | 2022-11-04 | PASS | PASS (NA) | PASS 3/3 | yes |
| ctl_2023_frc_pass | First Republic Bank | 2023-03-16 | PASS | PASS (NA) | PASS 3/3 | yes |
| ctl_2024_ba_pass | Boeing | 2024-01-08 | PASS | PASS (YES) | PASS 3/3 | yes |

Reading: 10/10 named PASS and 9/10 masked PASS by majority (27 of 30 individual masked runs; Endo 2015 bought in two of three
masked runs on "divestiture cash as the floor", Hertz 2020 equity bought once). Before the v1.5 discipline tests six of ten
controls came back BUY (see CHANGELOG v1.5): the activist chain's natural failure mode is to see a fixable problem in every
cheap under-earner. Two control packs (GE 2018, Newell 2019) had omitted the facts that kept Third Point out (Trian on the board
and the LTC reserve charge; the Starboard/Icahn settlements) and gained a D09 document — a pack defect, logged in run_log.md.

## Divergences (calibration cases where either run missed direction)

| id | what diverged | reading |
|---|---|---|
| 2005_massey_buy | named PASS / masked PASS vs key BUY | PASS both ways in the frozen run (hard fail) although both v1.2 runs bought: the frozen chain reads the 2005 operating record as a "melting ice cube" rather than a management discount on coal reserves — the new discipline test over-fires on a cyclical producer with a cost problem. Variance plus a rule boundary. |
| 2009_chrysler_finco_buy | named BUY / masked BUY vs key BUY | named PARTIAL: right side, smaller size for the first-lien loans. |
| 2012_greece_buy | named PASS / masked BUY vs key BUY | named PASS (hard fail) / masked BUY: with the name the chain treated Greek government bonds as a political binary without a floor; masked it priced the post-PSI bonds against the official-sector path. A memory effect in the wrong direction. |
| 2013_hlf_buy | named BUY / masked BUY vs key BUY | BUY both ways, direction PARTIAL: sizing/conviction below the key (Loeb's 8%+ position vs the chain's trade size for an E2 squeeze). |
| 2013_sothebys_buy | named BUY / masked BUY vs key BUY | masked PARTIAL: sizing/instrument difference. |
| 2015_bax_buy | named BUY / masked PASS vs key BUY | masked PASS: all six Gate 1 criteria UNSURE without the name, Gate 2 NO_EDGE; named run matched 3/4. |
| 2018_cpb_buy | named PASS / masked BUY vs key BUY | named PASS (hard fail: "melting ice cube", 5x levered after Snyder's-Lance) / masked BUY: the separable-asset / named-buyer exception was not applied in the named run although the pack names the strategic buyers. |
| 2018_nestle_escalate | named ESCALATE / masked ADD vs key ESCALATE | masked ADD vs ESCALATE: same side (PARTIAL); without the name the chain added rather than publishing the deck. |
| 2021_shel_buy | named BUY / masked PASS vs key BUY | masked PASS: the sum-of-the-parts (LNG and marketing vs upstream) was not accepted as an event without the name; named run matched 3/3. |
| 2022_bbwi_buy | named PASS / masked PASS vs key BUY | PASS both ways (E4 inflection on a specialty retailer): the chain reads post-separation retail as declining; Loeb bought on free cash flow and buybacks and later pressed on governance. |
| 2022_cl_buy | named BUY / masked BUY vs key BUY | see runs |
| 2022_intc_sell | named HOLD / masked HOLD vs key SELL | HOLD both ways vs a SELL inferred from 13F absence (calibration_eligible = false; no stated rationale). |
| 2023_dis_sell2 | named HOLD / masked HOLD vs key SELL | HOLD both ways vs a SELL inferred from 13F absence (calibration_eligible = false); the chain holds while on the board (L5). |
| 2025_csgp_buy | named PASS / masked BUY vs key BUY | named PASS (hard fail: "someone else's fight" — D. E. Shaw was already engaged) / masked BUY: the discipline test fires on a situation Loeb in fact joined with his own slate; the rule needs the "lead or stay out" qualifier read against the stake size. |

## Hold-out reading (sealed set, run once after the v1.5 freeze)

Eleven decisions disclosed after 1 August 2025: five new positions (Ebara, SK Hynix, SK Square, Block, Flex), the CoStar
addition and later sale, the Soho House sale, the Kenvue/Kimberly-Clark sale, the mortgage-book trim and the 2026 gross
reduction. The frozen chain matched **5/5 purchases both named and masked** — including three Asian names (two Korean, one
Japanese) and a US payments name it had never been tuned on — and **0/5 sells and trims**: it answered HOLD to every exit and
trim (ESCALATE once, masked, on Soho House), and labelled the gross reduction HEDGE (PARTIAL named). Driver overlap on the
sealed set is 16-18%, against 50-58% in calibration: the chain finds the right side of a new idea from a point-in-time pack
but does not reproduce Loeb's stated reasons for it, and it does not sell. The same asymmetry appeared in the Ackman chain
(sells are "comparative" decisions — better use of capital, a widened distribution — that a pack about one company does not
show) and is the first item in the v1.6 plan: the existing-position prompt needs the portfolio context (what else is in the
book, what the new idea is) that Third Point's own sell decisions are made against.

## Per-decision results — hold-out (sealed)

| id | company | as of | era | mode | key | named: decision / direction / state k/N | masked: decision / direction / state k/N | instrument / role / flags |
|---|---|---|---|---|---|---|---|---|
| ho_2025_costar_add | CoStar Group | 2025-06-30 | E | existing | ADD | HOLD / MISS / MISS 2/3 | HOLD / MISS / MISS 1/3 |  |
| ho_2025_ebara_buy | Ebara | 2025-06-30 | E | new | BUY | BUY / MATCH / PARTIAL 1/4 | BUY / MATCH / PARTIAL 1/4 | common P1 |
| ho_2025_sk_hynix_buy | SK hynix | 2025-06-30 | E | new | BUY | BUY / MATCH / PARTIAL 0/4 | BUY / MATCH / PARTIAL 1/4 | common P0 |
| ho_2025_sk_square_buy | SK Square | 2025-06-30 | E | new | BUY | BUY / MATCH / PARTIAL 2/3 | BUY / MATCH / PARTIAL 2/3 | common P1 |
| ho_2025_soho_sell | Soho House & Co | 2025-08-15 | E | existing | SELL | HOLD / MISS / MISS 0/3 | ESCALATE / MISS / MISS 0/3 |  |
| ho_2026_block_buy | Block | 2026-03-31 | E | new | BUY | BUY / MATCH / PARTIAL 0/4 | BUY / MATCH / PARTIAL 0/4 | common P1 |
| ho_2026_costar_sell | CoStar Group | 2025-12-31 | E | existing | SELL | HOLD / MISS / MISS 0/4 | HOLD / MISS / MISS 0/4 |  |
| ho_2026_flex_buy | Flex | 2026-06-30 | E | new | BUY | BUY / MATCH / PARTIAL 1/4 | BUY / MATCH / PARTIAL 1/4 | common P0 |
| ho_2026_kenvue_kmb_sell | Kenvue / Kimberly-Clark even | 2026-01-30 | E | existing | SELL | HOLD / MISS / MISS 0/3 | HOLD / MISS / MISS 0/3 |  |
| ho_2026_mortgage_trim | Discounted first-lien reside | 2026-02-27 | E | existing | TRIM | HOLD / MISS / MISS 0/3 | HOLD / MISS / MISS 0/3 |  |
| ho_2026_portfolio_reduce_gross | Third Point portfolio risk | 2026-01-30 | E | hedge | REDUCE_GROSS | HEDGE / PARTIAL / PARTIAL 1/3 | HEDGE / MISS / MISS 0/3 |  |

## Method notes
- Each calibration pack ran once named and once masked under the frozen v1.5 chain; controls once named and three times masked.
  Run-to-run variance is visible (Massey 2005 bought in both v1.2 runs and passed in both frozen runs) and reported, not averaged.
- Masking replaces the company, ticker and every alias in meta.json with "the Company"; era, dates and figures remain.
- One leakage flag in calibration named (2024_vst_buy; quoted in its score file): The agent's memo references a 'March 2024 Energy Harbor acquisition' while the key and provided documents (D01, D07) identify the deal as occurring in March 2023. — a factual slip by the agent (the deal closed March 2023, as the pack says), not post-cutoff knowledge; recorded as the grader raised it.
- Enforcement artefact: when Gate 1 hard-fails and the decision step still writes BUY, the code flips the decision to PASS and
  prefixes the memo with a bracketed note; the BUY draft is left verbatim for audit.
