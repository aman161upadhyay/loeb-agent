# loeb-agent — a process-faithful Dan Loeb / Third Point decision agent

Built 2026-10-25 for Aman Upadhyay (HBS Seminar in Investing, Fall 2026; sponsor Laurion Capital), as the third of three
investor agents (ackman-agent, buffett-agent, loeb-agent) produced with the same loop: research and archive → trade compendium →
agent specification and prompt chain → calibration replay with grading → prompt freeze → sealed hold-out → forward prediction →
adversarial review. Goal: an LLM agent that reproduces **how** Loeb decides — the event, the edge, the route, the floor, the skew,
the letter — graded trade by trade against what he actually did and said, with a hold-out firewall and tooling to run offline
on a Mac Mini with Llama 3.1 8B (training data to Dec 2023).

## Repository map

| Path | What it is |
|---|---|
| `AGENT.md` | The agent specification: the era switch 1995-2026 (A small-cap event-driven and the letters; B credit cycle and large-cap constructivism; C quality, inflection, Japan, venture; E the current book), the five gates (event and edge → why mispriced → valuation and skew → catalyst and Third Point's role → risk and sizing), situation types E1-E7, sell rules L1-L5 and the ESCALATE rule, the hedge/regime rule, output contract, exemplars (calibration trades only), and the amendments made during calibration (each tied to its motivating case). |
| `prompts/` | Staged chain `00_system` → `01_fact_sheet` → `02`-`06` gates → `07_decision_memo` (new ideas), `08_sell_hold` (existing positions), `09_hedge` (regime), `10_grader`, `11_leakage_check`, `12_forward_next_trade`; `one_shot_full.md`; `CHANGELOG.md` (every prompt change v1.0→v1.5 with the calibration case that motivated it); `era_e_update_for_forward_runs.md` (2025-26 addendum, forward runs only). |
| `tools/` | `run_agent.py` (Ollama / any OpenAI-compatible endpoint; `--mask`, `--one-shot`; recomputes and enforces the Gate 1 hard fail), `grade.py`, `scoreboard.py` (Wilson CIs), `canary.py`. |
| `calibration/` | 68 point-in-time data packs (`data_packs/<id>/docs/D01..`, `meta.json`): 47 calibration decisions 2003-2025, 10 controls, 11 sealed hold-outs 2025-26; answer keys (`answer_keys/`, sealed set in `answer_keys/holdout/`); runs and scores for the frozen v1.5 chain (`runs/`, `scores/`, `scores/holdout/`), the iteration-phase runs in `prefreeze/`; `scores/scoreboard.md`; manifests; `HOLDOUT_SEALED.md`; `PROMPT_HASHES_v1.5.txt`. |
| `compendium/` | 253 trade dossiers 1995-2026 (`trades/`), `all_positions_index.md` (54 quarters of 13F issuer rows), indexes by era, `SCHEMA.md`. Each dossier: dates, size, thesis at the time, how it was decided, Loeb's own words (letters, 13D letters, decks, X), public discussion, outcome, lessons, sources. |
| `archive/` | Loeb profile, investment principles, reasoning patterns, letters / interviews guides, `x_posts/` and `forums/` (what the public said at the time). |
| `investor_profiles/` | Investor profiles, `what_makes_a_great_investor.md`, `loeb_vs_peers.md`. |
| `research/` | Best practices for investor-persona agents, look-ahead/evaluation design, `prompt_critique_and_optimization.md` (where "the exact same loop" had to change for an activist/event-driven multi-strategy book, and why). |
| `forward/` | Frozen evidence pack (F01-F06, as of 2026-10-25) and `next_trade_prediction.md` / `.json`. |
| `adversarial/` | Independent adversarial review (seven reports: verdict, predicted decisions on 15 untuned cases, divergence causes, hold-out critique, eight red-team packs, grader/method critique, v1.6 plan). Its headline findings — a mode-only baseline beats the chain on calibration direction; every hold-out match is a new-position BUY; some sell keys need information the pack cannot contain; controls tuned in calibration are not independent validation; two control D09 docs carried post-cutoff sentences (fixed, logged) — are accepted and reflected in the scoreboard. Read it before trusting the numbers. |
| `run_log.md`, `RESEARCH_GUIDE.md` | What was done, by whom, with what evidence; how to extend the research. |

## Results in one paragraph
On 47 calibration decisions (2003-2025) the frozen v1.5 chain, run on Replit's current internal model, matched Loeb's
**direction in 81% (named) / 79% (masked)** and reproduced **58% / 50% of his stated reasons**; it said PASS to **10/10
discipline controls named and 9/10 masked by majority (27 of 30 runs)** — Best Buy 2012, Endo 2015, Groupon 2016, GE 2018,
Newell 2019, Hertz equity 2020, GameStop/AMC 2021, Vroom 2022, First Republic 2023, Boeing 2024 — but only after the v1.5
discipline tests: under the earlier prompts **six of ten controls came back BUY**, which is the activist chain's natural failure
mode (a fixable problem in every cheap under-earner) and the most useful thing the loop found. The 11 sealed hold-outs
(disclosed after 1 Aug 2025) came back **5/11 on direction both named and masked: all five new purchases matched (Ebara, SK
Hynix, SK Square, Block, Flex), none of the five sells and trims** (the chain holds every exit) — the same buy/sell asymmetry
the Ackman chain showed, with driver overlap falling from 50-58% in calibration to 16-18% on the sealed set. Where the
calibration misses, it misses on the boundaries of its own new rules (Massey 2005 and Campbell 2018 read as melting ice cubes;
CoStar 2025 read as someone else's fight), on keys inferred from 13F absence with no stated rationale (Intel 2022, Disney 2023),
and on run-to-run variance (Baxter 2015 masked, Shell 2021 masked). Full numbers, intervals, the divergence table and the
hold-out reading: `calibration/scores/scoreboard.md`. These runs measure prompt compliance on a model that may remember the
outcomes; the fidelity test is the Llama 3.1 8B replay below.

## What changed from the Ackman and Buffett loops (details in `research/prompt_critique_and_optimization.md`)
- Gate 1 asks "what is the event and what is our edge", not "is this a great business": Third Point's book spans 13D activism,
  post-reorg equity and credit, risk arbitrage, sovereign bonds, quality compounders at inflections, venture and shorts, so the
  chain classifies the situation (E1-E7) first and scores the six criteria by type (credit scores the claim; the Era A/B activist
  writes the plan himself; the squeeze long is E2, not a short).
- Six discipline tests (melting ice cube, someone else's fight, unknowable liabilities, leverage on a shrinking base, the
  adjusted-earnings roll-up, the multi-year turnaround as the only lever) are what separate Third Point's 13Fs from a value
  screen; they were written from the first control run, not from any hold-out.
- ESCALATE is a first-class action for existing positions (the Era A/B 13D letters; the Era C deck after private engagement is
  ignored), and regime decisions are scored on gross exposure (ADD_RISK / REDUCE_GROSS / HEDGE / NO_CHANGE).
- The Gate 1 hard-fail flag is recomputed in code from the criteria scores (the model set hard_fail = false on a FAILed floor).

## Run it on the Mac Mini (offline)
```bash
ollama pull llama3.1:8b
python tools/canary.py --model llama3.1:8b                      # should answer "unknown" to post-2023 canaries
python tools/run_agent.py --model llama3.1:8b --pack calibration/data_packs/2024_vst_buy --mask
python tools/grade.py calibration/runs/<run>.json calibration/answer_keys/2024_vst_buy.json
for p in calibration/data_packs/202[4-6]_*; do python tools/run_agent.py --model llama3.1:8b --pack $p --mask; done
python tools/scoreboard.py calibration/scores > calibration/scores/scoreboard_llama.md
```
`run_agent.py` also takes `--base-url` / `--api-key` for any OpenAI-compatible server and `--one-shot` for larger models.
Keep prompts frozen while scoring hold-outs; log any change in `prompts/CHANGELOG.md` with the calibration case that motivated it.

## The firewall
Calibration = decisions disclosed up to 1 Aug 2025 (47 used; the 1995-2002 cases live in the compendium only, the packs start
with Potlatch 2003). Sealed hold-out = Ebara, SK Hynix, SK Square, Block, Flex, the CoStar addition and sale, the Soho House
sale, the Kenvue/Kimberly-Clark sale, the mortgage-book trim and the 2026 gross reduction. `AGENT.md` and the prompts cite no
hold-out specifics; the era-E addendum is appended only for forward runs. Prompts were frozen (`PROMPT_HASHES_v1.5.txt`) before
the hold-out packs were opened and were not edited afterwards; the hold-outs ran once.

## Forward prediction (scored 25 Jan 2027 for actions; 16 Feb 2027 13F for positions)
`forward/next_trade_prediction.md` — regime, ranked candidates with 90-day probabilities, names the chain passes and why,
expected changes to existing positions, the single most likely next disclosure, a separately labelled principal's
reconciliation (which lowers the chain's Solstice call: Starboard's fight), and the scoring plan.

## Licence / provenance
All source material is public (SEC filings, Third Point letters and 13D letters, decks, interviews, X posts, press, forums).
Every compendium entry and pack document carries its sources and dates; gaps are marked rather than filled. Prepared with
Replit Agent.
