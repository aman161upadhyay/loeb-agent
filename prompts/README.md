# Prompt chain for the Loeb agent

Same architecture as the Ackman and Buffett agents: one decision = 7 short calls for a new idea, each with a JSON output passed
to the next call; one call for an existing position (08) or a portfolio-level pack (09). File names and stage names are
identical so tools/run_agent.py, grade.py and scoreboard.py work unchanged.

| # | file | input | output |
|---|---|---|---|
| 0 | 00_system.md | — | system prompt for every call (identity, rules, era switch) |
| 1 | 01_fact_sheet.md | pack docs | structured, cited fact sheet incl. capital structure, governance, conflicts, Third Point context |
| 2 | 02_gate1_business_quality.md | fact sheet | Gate 1: situation type E1-E7, 6 criteria, hard_fail, edge statement |
| 3 | 03_gate2_why_mispriced.md | fact sheet + G1 | Gate 2: mispricing mechanism M1-M8, variant view, peer benchmark |
| 4 | 04_gate3_valuation.md | fact sheet + G2 | Gate 3: SOTP / post-event earnings / recovery / arb / inflection, floor, skew, IRR |
| 5 | 05_gate4_catalyst_role.md | all prior | Gate 4: plan P0-P5, asks, actors, governance route, timetable |
| 6 | 06_gate5_risk_sizing.md | all prior | Gate 5: kill criteria, portfolio risk, instrument, size, horizon |
| 7 | 07_decision_memo.md | all prior | final JSON (schema_decision.json) + memo in letter voice |
| alt | 08_sell_hold.md | pack for an existing position | HOLD/ADD/TRIM/SELL/ESCALATE with reason class L1-L5 |
| alt | 09_hedge.md | portfolio pack | ADD_RISK / REDUCE_GROSS / HEDGE / NO_CHANGE (mode "hedge" in meta.json) |
| eval | 10_grader.md | agent JSON + answer key | rubric scores |
| eval | 11_leakage_check.md | agent output + as_of | flags post-date facts |
| fwd | 12_forward_next_trade.md | current portfolio + candidate pack | ranked next-action candidates with probabilities |

Conventions: pack documents are labelled D01, D02, ... in the order given; every factual sentence ends with [Dnn].
Temperature 0-0.2. Keep each call's context < 12k tokens for 8B models. The decision step may not overturn an upstream hard
fail (a lesson from the Ackman adversarial review): run_agent.py enforces it in code as well.
