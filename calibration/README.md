# Calibration and hold-out harness

## Layout
- data_packs/<trade_id>/meta.json — { id, company, ticker, aliases[], as_of_date, mode: new|existing|hedge, fund_aum_usd_bn, notes }
- data_packs/<trade_id>/docs/D01_*.md … — point-in-time documents; each begins with Title / Source / Date lines; Date ≤ as_of_date
- answer_keys/<trade_id>.json — { id, actual_decision, conviction, size_pct_nav, first_action_date, disclosure_date,
  reason_class (for sells), drivers: [{driver, source, quote}], outcome_note, sources[] }  (NEVER shown to the agent)
- runs/ — agent outputs (JSON) ; scores/ — grader outputs + scoreboard.jsonl
- HOLDOUT_SEALED.md — the firewall list; pass_cases.md — discipline tests

## Protocol (what the team's rubric requires)
1. Freeze prompts (git tag) before running any hold-out.
2. For each trade: run named; run masked (--mask); run on the pre-dated model (Llama 3.1 8B) and on a current model;
   plant a canary (tools/canary.py plant) so grounding can be verified.
3. Grade with prompts/10_grader.md using a strong model, then a human spot-check of every MATCH (the grader is generous
   with paraphrase); record disagreements.
4. Report counts with Wilson intervals (tools/scoreboard.py), never bare percentages; report divergences as prominently
   as matches; separate "model quality" misses (pre-dated model fails on a current model's pass) from "leakage"
   (current model passes only because it remembers).
5. States: MATCH = same decision and ≥3 of 4 drivers; PARTIAL = same decision with fewer drivers, or reverse; MISS = opposite decision.

## Running locally (Mac Mini, Ollama)
  brew install ollama && ollama pull llama3.1:8b
  python tools/run_agent.py --pack calibration/data_packs/2025_uber_buy --model llama3.1:8b
  python tools/grade.py --run calibration/runs/<file>.json --key calibration/answer_keys/2025_uber_buy.json --model llama3.1:8b
  python tools/scoreboard.py
Context: use num_ctx 16384 (8B q4 fits on 16 GB); packs should stay under ~10k tokens for the 8B model — the fact-sheet
stage exists so later stages never see the raw pack.
