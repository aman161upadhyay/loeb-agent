# Proposed v1.6: repair measurement before adding examples

**Status:** recommendations only. No production file was modified by this review. The current v1.5 scores and forward forecast must remain immutable. The holdouts and fifteen manually reviewed cases are now development material for anyone using this report; none can become a new untouched v1.6 test.

## Priority 0 — make a recommendation safe to consume

### A. Typed, validated executable decisions

**Target:** `tools/run_agent.py`, decision schemas and downstream interface.

Proposed exact decision contract:

> Preserve the original model output as `draft_final`. Construct `executable_decision` only after schema, source, arithmetic and policy validation. An invalid stage or missing mandatory input yields `REQUEST_DATA`, not a silent PASS or an executable BUY. PASS and REQUEST_DATA have `target_size_pct_nav = 0`. Retain the drafted size/memo only in the audit object. Record each validator failure and original value.

Required separate fields:

- `recommended_action`, `instrument_id`, `legal_entity_id`, `position_before`, `position_after`;
- `economic_exposure_change`, `campaign_action`, `financing_action`—do not overload one enum;
- conviction in mechanism versus confidence in the factual inputs;
- target NAV weight versus issuer ownership/votes;
- thesis horizon, expected catalyst date, next evidence date and kill threshold;
- no-trade/research status and missing mandatory inputs.

**Acceptance tests:** malformed G1 is rejected; hard-failed BUY cannot leave nonzero executable size or an initiating memo; a valid short is not rejected by a long-floor check; no nonexistent citation reaches an executable recommendation. Retain every raw artifact.

### B. Deterministic valuation and exposure calculator

**Target:** prompts 04/06/07 plus a validation module.

Proposed addition:

> All target, floor, skew and annualized-return claims must reference a machine-readable calculation. Identify source inputs, assumptions, units, date, accounting perimeter, security denominator, senior claims, taxes/fees, dilution and cash required until realization. A qualitative asset description is not a numerical floor. Use null when data cannot support a result; do not infer zero downside from the current share price.

Compute:

- EV-to-equity bridge with explicit net debt/minorities/pensions/leases where applicable;
- target/base/stress per-share values from the same share basis;
- upside `(target/price)-1`, downside `1-(stress/price)` and ratio only when downside >0;
- cash-flow IRR or clearly labeled price-only annualization, not conflated with total return;
- credit waterfall and recovery at the **purchased legal claim**;
- short carry/borrow/recall and worst-case or option-defined loss;
- before/after long, short, net, gross, credit and delta exposures.

**Acceptance tests:** Baxter $1.50×20 returns $30; Hertz ~$411m divided by ~142.3m returns ~$2.89; Endo's two-year $113.75/$87.32 return is ~14.1%; selling longs and adding index shorts do not produce the same gross change. Outputs may choose different assumptions, but must expose and justify them.

**Expected scoreboard effect:** safer recommendations may initially lower BUY recall. That is not a reason to waive validation.

## Priority 1 — repair the label and grading system

### C. Split the key into observations and explanations

**Target:** answer-key schema, not historical key facts.

Proposed fields:

> `action_observed`, `instrument`, `action_window_start/end`, `first_disclosure_date`, `information_cutoff`, `observation_type`, `exact_action_scorable`, `reason_scorable`, `size_scorable`, and `reason_provenance`.

For each driver:

> `investor_stated | third_party_reported | evaluator_inferred`; original publication date; evidence span; availability at cutoff; whether a reasonable inference or private/later information.

Separate actual trade, public campaign, reportable common-stock change and economic-exposure change. Store an unknown date as null plus a bounded window, not a fabricated day. Do not put issuer ownership in a NAV field.

**Immediate historical corrections to publish in a separate errata panel:**

1. Four explicitly ineligible keys leave strict relevant denominators; report their proxy tests separately.
2. Greece June/Q3 mismatch gets explicit exact-action ineligibility.
3. Holdout exit count corrected to three SELL plus one TRIM; ADD is separate.
4. Herbalife/Sotheby's size fidelity marked unscorable pending actual comparable NAV evidence.
5. Campbell, CoStar, Baxter, Shell, BBWI and Massey divergence descriptions replaced with stage-supported diagnoses.
6. Do not silently overwrite old grades; identify original and corrected evaluator versions.

### D. Rebuild evidence-aware grading

**Target:** `tools/grade.py`, prompt 10 and aggregator.

Proposed exact grading instruction:

> Grade exact action first, without considering size or eloquence. Then grade instrument, exposure magnitude, campaign action and mechanism separately. Use only supplied source spans for grounding and date availability. A reference absent from the pack is INVALID_REFERENCE. An unsupported assumption is not a source fact. Future ownership observations are labels, not causal drivers. If a dimension is unknown in the key, mark UNSCORABLE.

Supply the actual pack documents or lossless retrieved claim spans, populated index, key, rendered model input and validated output. Fail if any template placeholder remains. Make `reason_score=null` for zero eligible drivers.

Proposed aggregation:

- one immutable row per experiment/pack/version/checkpoint/seed/mask;
- explicit development, control, holdout and prospective partitions;
- exact action and full trade fidelity side by side;
- original all-driver and available-driver mechanism denominators;
- campaign-cluster uncertainty, repeat distributions and grader agreement;
- no appended duplicate counting or filename-based inference of condition.

**Acceptance tests:** Nestlé ADD cannot become exact ESCALATE; HEDGE cannot become exact REDUCE_GROSS; D110 in an eight-document pack is invalid; `[D02, D04]` is parsed correctly; zero-driver controls cannot claim full mechanism success.

## Priority 2 — replace narrow historical exceptions with causal rules

The text below is proposed replacement language, not a case-name patch list.

### E. G1: scope discipline by security and opportunity

**Target:** `prompts/02_gate1_business_quality.md`.

Replace the universal long-floor interpretation with:

> First select the claim and side. For a long, assess stressed value reaching that claim after senior obligations and required funding. For a short, assess adverse upside, financing/borrow and catalyst timing. For sovereigns, use explicit default/restructuring/redenomination scenarios and legal process; absence of corporate collateral is not automatic failure. For financing trades, assess retained risk and liquidity as well as assets sold.

Replace “someone else's fight” with:

> Another activist is evidence about route, competition and price discovery, not an automatic veto. Require a distinct economic or implementation advantage: different security, incremental proposal, credible coalition, different time horizon or price. If the same asks are already fully priced and no incremental edge remains, fail edge. Verify actual standstill, controller and voting constraints; do not infer them from affiliation.

Replace the unconditional Japan/default-register exceptions with:

> Governance feasibility must follow dated ownership, voting rights, board/nomination rules, coalition incentives and legal authority. Geography and index ownership are priors, not proof of receptivity. If those facts are missing, mark UNSURE and identify the required evidence.

Replace the rigid quality date gate with:

> E4 is available whenever contemporaneous evidence establishes durable economics and a specific mispriced earnings/cash-return mechanism. Historical era changes prior probabilities, required expertise and sizing, not logical eligibility. Excellent existing management may be the mechanism; do not invent activism to qualify an investment.

Revise the melting-business test:

> Distinguish secular impairment from cyclical trough, accounting changes and discretionary growth capex. A floor can come from independently monetizable assets only after liabilities, costs and time-to-realization. A named buyer or announced gross proceeds alone is insufficient. A one-quarter decline does not meet a multi-year secular-decline test.

Revise the squeeze exception:

> Technical catalysts do not waive solvency, legal or product-safety risk. Require independent evidence on allegations, dated positioning, realizable liquidity and a bounded loss budget. If tail loss cannot be bounded for common equity, consider a defined-loss expression or decline. Specify monetization after repricing at entry.

Revise the Intel rule:

> A management-dependent turnaround requires observable milestones, funding runway, downside at the purchased price and an executor with relevant evidence. An unproven roadmap lowers permitted risk or blocks investment if survival depends on it. It does not categorically prohibit every new-CEO situation; separable asset value and security choice may change the result.

**Acceptance tests:** InterCept/BindView collaborations are not excluded solely for cooperation; Roper 2015 can qualify E4 without invented event; an unrelated creditor cannot inherit a secured floor; a cyclical producer is not labeled secular solely from negative FCF. These are regression tests, not fresh accuracy claims.

### F. G2/G3: do not manufacture market disagreement

**Target:** prompts 03/04.

Proposed insertion:

> Distinguish an observed market belief from analyst inference. Specify the evidence for price-implied expectations or a documented competing thesis. A bear-case paragraph written by the pack author is not proof of market consensus. A peer margin gap is not automatically controllable; reconcile mix, accounting, investment phase and competitive position. If valuation is unquantified, the action must remain conditional or below a separately registered research-risk cap.

No exact default 2:1 skew, 25% IRR, 5% NAV or historical multiple should appear merely because the schema expects a number. Preserve qualitative ranking when inputs are insufficient.

### G. Existing positions: structured state transition, not default patience

**Target:** prompt 08 and pack D08.

Proposed opening:

> Reconstruct the original security, thesis, target, time budget and kill criteria using only pre-cutoff evidence. For each driver mark supported, weakened, broken, realized or unknown. Separately evaluate (1) security economics, (2) catalyst state, (3) legal trading ability, (4) portfolio opportunity cost and risk. A board seat is not an instruction to hold indefinitely. If original criteria are missing, do not invent them; state what would make a future change observable.

Replace L5:

> L5 is a legal/governance constraint flag, not a standalone investment thesis. Identify exact contractual or information restrictions and lawful alternatives. A settlement is a means to an operating/financial result; if the precommitted result fails, reconsider exposure even if the relationship continues.

Add:

> ADD requires positive incremental expected-return evidence or a lower price with independently intact value, plus capacity. ESCALATE requires a feasible authority path and incremental benefit net of cost. SELL/TRIM can follow target realization, weaker expected value, changed risk, failed process or superior alternatives without requiring a public admission of failure. REFINANCE/SELL_RISK must describe retained exposure, not be forced into liquidation language.

**Acceptance tests:** three-stage RT7 responds to a real missed milestone; no future action disclosure is needed to trigger a reasoned exit; mortgage refinancing is represented as a financing/risk transition; same-day public campaign is not confused with a new trade.

### H. G4/G5: authority and risk precede rhetoric

**Target:** prompts 05/06/07.

Proposed insertion:

> Name the actor who can implement each step, the investor's actual authority, the permissions/coalition required, evidence due date, cash/time cost and failure route. P0 is a legitimate choice when management or a contractual process supplies the catalyst. Proposed engagement is an intended action, never a claimed existing relationship.

Sizing:

> Use strategy/fund NAV and actual exposure reports, not firm AUM or issuer ownership. Bound expected and stressed loss, liquidity under stress, financing, concentration and factor overlap. If these are missing, supply a conditional range with zero executable authorization until constraints are supplied.

Remove unnecessary “letter voice” pressure from the analytical stages. It encourages confident “we are pushing” claims where only a hypothetical plan exists. Allow the final human-readable memo only after validated analysis.

## Priority 3 — neutral packs and reproducible experiments

1. **Pack provenance:** original publication/vintage/retrieval dates and exact source spans; restore raw facts before adding analyst interpretation.
2. **Entity mapping:** distinct anonymized IDs for issuer, subsidiary, guarantor, controller and security; evaluator retains real source identities.
3. **Content balance:** do not enforce filler word counts. Equalize factual coverage and separately label authored bull/bear interpretations. Test D05 length/content/order as registered factors.
4. **Portfolio state:** dated book exposures, current targets, liquidity, financing and alternatives; otherwise mark portfolio-action dimensions untestable.
5. **Fact-sheet recall:** deterministic check that decisive source facts—Strawbridge alliance, legal seniority, missing price—survive compression.
6. **Execution manifest:** hash tools, schemas, pack/key contents, rendered prompts, model identifier and evaluator; capture parameters, context/token counts, timestamps and failures.
7. **One-shot versus staged:** treat as separate policies until a parity suite establishes equivalent required checks. The forward path must run the same validators.
8. **Models:** compare the current model with a documented pre-dated checkpoint on genuinely later cases. A claimed training cutoff is helpful, not proof of zero contamination; audit finetuning and retrieval too.
9. **Ablations:** generic investor versus persona; case-name examples removed; neutral versus authored pack summaries; calibrated versus uncalibrated sizing; old versus structured exit prompt. Fix the model/checkpoint and sampling plan.
10. **No assumed gain:** publish failures and regression costs. A v1.6 can be safer and more faithful while matching fewer historically aggressive BUYs.

## January–February 2027 forward-scoring preregistration

### 1. Freeze three distinct products

Keep the October 25, 2026 artifacts untouched:

**A. Raw-chain forecast.** Score each of the four original runs separately. Their union/max-probability table is a derived ranking, not a single calibrated probability forecast.

**B. Principal-reconciled forecast.** Register exactly the published human adjustments: Honeywell NEW_BUY .50; Solstice .15; 3M .25; FedEx .25; at least one trim among Nvidia/Unum/UNP .60; public E1 campaign .25; 1–2 new names and 1–2 trims. Preserve other published raw candidate probabilities as raw, not silently upgraded human probabilities.

**C. Future v1.6 forecast.** If issued before outcomes are examined, record a new timestamp, complete finite opportunity universe, all candidate/action probabilities and common validation rules. Do not call it an October 25 prediction. If outcomes were already viewed, the overlapping window is development only and a later untouched window is required.

Correct factual defects in an **errata document**, not by overwriting A/B probabilities. The FedEx reconciliation's Q2 2027 statement conflicts with F04's June 1 distribution; retain original prediction and report the error.

### 2. Fix horizons and observability now

- **Public-disclosure window:** after the October 25, 2026 freeze through **January 25, 2027**, inclusive at a declared timezone. This is a calendar-date window, not exactly 90 elapsed days.
- **Quarter-end holdings endpoint:** Q4 2026 positions measured **December 31, 2026**, adjudicated after the applicable February 2027 13F filing deadline. Use **February 16, 2027 as the planned review checkpoint**, but verify the SEC deadline and actual filings before final adjudication rather than assuming every fund files on one date.
- **Late/amended evidence:** retain an immutable first-pass score and publish a separately versioned amendment panel. A late filing is not retroactively available to an earlier prediction.
- **Economic-action window:** separate from disclosure. If a filing first reveals a holding but cannot date purchase after October 25, grade **newly disclosed exposure** and mark actual within-window trade timing unknown.

### 3. Define actions without post-hoc flexibility

- NEW_BUY: first reportable appearance relative to the frozen latest comparable report, excluding issuer succession, spin distributions and identifier changes; for actual new economic exposure, require dated corroboration if available.
- ADD/TRIM: split/corporate-action-adjusted share or principal change, not market-value change. Register a materiality threshold before outcomes; proposed primary threshold **10%** relative quantity change, with all nonzero changes shown secondarily.
- SELL: reportable line absent/zero, with economic exit separately verified. An absent common line does not prove swaps/credit absent.
- ESCALATE/public E1: dated investor letter, 13D purpose/amendment or actual nominee action attributable to Third Point. Another activist's campaign does not count.
- Credit NEW_BUY: identify exact security/claim and evidence of Third Point ownership. Issuer refinancing is not confirmation.
- Gross/net change: use authenticated manager exposure reports or explicit statements. If unavailable, mark unobservable rather than infer from long-only 13F.
- HOLD: no observable material share change within available filings, with missing/nonreportable exposure caveat. Never treat silence alone as proof of total economic continuity.

Corporate-action corrections and the materiality threshold must be applied symmetrically to all names. Register multiple actions as a vector when add and escalation coexist.

### 4. Confirmation hierarchy

1. Original SEC filings and issuer/investor agreements identifying Third Point and security.
2. Original Third Point letters/exposure reports and dated attributable public statements.
3. Contemporaneous reporting corroborated by primary evidence.

Do **not** count a company catalyst alone as a manager trade: TDS asset-sale 8-K, Flex Innovation Day/Form 10 and Bausch refinancing are catalyst outcomes, not ADD/NEW_BUY confirmations. Score catalyst forecasts in a separate panel.

For each decision create an adjudication row: predicted probability/action/security; original input date; observed source/date; measurement period; quantity before/after; action classification; unknowns; independent reviewer sign-off.

### 5. Score probabilities honestly

- Brier score and log score for every **specified binary event**, with no retroactive probability adjustment. Publish raw per-run and human-reconciled results separately.
- Do not force candidate-event probabilities to sum to one when multiple trades can occur; for mutually exclusive action distributions within one security, require normalization in future forecasts.
- Forecasts that were only a ranked list can receive top-k precision/recall, not a fabricated probability calibration score.
- Include an **OTHER_NEW_NAME** event in future finite-universe forecasts and count all actual new reportable names, so unpredicted purchases affect recall.
- Evaluate “at least one trim” as its registered union event, not a free choice of whichever individual name happens to match. Report individual outcomes too.
- Counts “1–2” receive interval coverage and absolute count error, not an invented likelihood.
- Missing/private-credit evidence is censored/unobservable, not automatically a miss or a success. Report coverage and a conservative observed-only panel.

Use simple preregistered baselines: no new names/no turnover; empirical pre-freeze frequency by action; and existing-book persistence. Do not estimate baseline probabilities from the scored window.

### 6. Audit timetable

|Checkpoint|Required work|Forbidden adjustment|
|---|---|---|
|Before first adjudication|Hash raw runs, human forecast, opportunity universe, scoring spec and source checklist; register independent reviewer|Changing probabilities because a later action is rumored|
|January 25, 2027 close|Capture dated disclosures; classify public actions and unresolved events|Using February filings as if publicly known in January|
|February filing review|Reconcile Q4 reportable positions, splits, distributions and claim identities; label trade timing unknown where necessary|Calling Q4 market-value appreciation an ADD|
|Final February report|Publish all predictions, nonpredictions/OTHER, original versus errata panels, scores and observability|Selecting best of four runs or substituting human judgments for raw failures|
|Subsequent amendments|Append versioned corrections with evidence and timestamps|Overwriting the original adjudication|

### 7. Decision to proceed

Deploy v1.6 as a **research aid** only after all mandatory validation tests pass and new paired red-team failures are disclosed. Do not authorize autonomous trading from a persona memo. Promote claims of predictive fidelity only after the new version beats the mode/persistence/generic-investor baselines on a genuinely untouched, balanced and observable set, with improved mechanism grounding and no hidden increase in unsafe recommendations.
