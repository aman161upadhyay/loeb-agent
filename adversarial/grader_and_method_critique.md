# Grading, arithmetic and experimental method

## 1. Separate the quantities currently called “accuracy”

The current direction rubric mixes the discrete action with conviction, size and instrument. A BUY can be PARTIAL because it buys the wrong claim or is supposedly too small. That may be useful as trade fidelity, but it is not pure directional accuracy.

Direct counts from keys and saved final actions:

|Metric|Named|Masked|Comparator|
|---|---:|---:|---|
|Published direction MATCH, all calibration|38/47|37/47|Includes size/instrument penalties|
|Literal exact action, all calibration|**40/47**|**40/47**|Mode-only modal policy **41/47**|
|Published direction MATCH, removing four explicitly ineligible keys|36/43|35/43|Still selected/tuned cases|
|Literal exact action, same eligible subset|**38/43**|**38/43**|Mode-only modal policy **39/43**|
|Holdout exact action|5/11|5/11|BUY on every new-mode case, no exact matches elsewhere, also 5/11|
|Published full state MATCH, holdout|0/11|0/11|Mechanism fidelity substantially weaker than action recall|

The mode baseline uses BUY for new, ESCALATE for existing, REDUCE_GROSS for hedge. Its 41 exact matches are 30 + 7 + 4. The eligible-subset figure is 29 + 7 + 3. This is a **descriptive in-sample modal baseline**, not an independently tuned strategy or a fair same-metric 87%-versus-81% statistical contest. On exact actions it beats the chain by one case, not the apparent six-percentage-point headline gap. It nevertheless shows how little company analysis is necessary to get a high number here.

Additional baselines to preregister:

- Always BUY among new ideas **including untouched negative candidates**.
- HOLD existing positions until an independently documented trigger, then follow the registered trigger.
- Public announced-event screen with valuation/liquidity thresholds, no Loeb persona.
- Same model and facts with a generic event-investor prompt.
- Identical staged model without named historical examples.

Report action confusion matrices, buy precision/recall, sell/trim/add/escalation recall, abstention coverage, instrument fidelity and reason fidelity separately. Do not conflate a successful decision with subsequent investment profit.

## 2. Ineligible keys are not merely “direction-only”

The scoreboard describes four excluded-reason keys as inferred from 13F changes, but that is not an accurate collective description:

- **2016 energy cover:** retrospective letter explicitly dates the reversal to mid-February, not requested January; an exact-date mismatch, not simply 13F absence.
- **Intel:** common line disappears Q4 2021, later bullish letter contradicts assumed thesis-break economic exit.
- **Disney:** public common absence, unknown derivative unwind and stated sale rationale.
- **AI basket:** a synthesized multi-name thematic basket, not a verified simultaneous April transaction.

Eligibility false should exclude the affected claim from the corresponding strict denominator. Preserve separate descriptive panels for disclosure proxies, counterfactual fresh capital and synthetic theme tests. Greece also has a severe June-versus-Q3 mismatch even though it lacks the same explicit eligibility flag. Do not mechanically equate a boolean with a full date-quality audit.

## 3. Size schema is dimensionally unsafe

`size_pct_nav` is often free text containing:

- issuer ownership percentage;
- number of common shares;
- gross dollars at a filing mark;
- firm AUM;
- unknown fund NAV;
- thematic allocation or peak ownership.

The grader then compares it with `target_size_pct_nav`, a numeric proposed portfolio weight. Herbalife's **8.24% issuer ownership versus 5% NAV** and Sotheby's **9.3% ownership versus 5% NAV** are concrete erroneous penalties. Chrysler both runs recommend 3%, yet the scoreboard claims smaller size explains only the named PARTIAL.

Use distinct typed fields: issuer economic ownership, voting ownership, market value, cost, fund NAV, firm AUM, portfolio delta, initial/peak/current dates and instrument. Compute NAV weight only with a valid matched numerator/denominator. If actual size is unknown, fidelity is **unscorable**, not low conviction or a mismatch.

## 4. The grading payload does not contain the evidence it purports to check

`prompts/10_grader.md` asks for document support and post-cutoff leakage, with a `{{pack_index}}` placeholder. The shipped `grade.py` fills only date, key and agent final output; it never fills that placeholder and supplies no documents.

Consequences:

1. A citation's existence and support cannot be verified reliably.
2. The answer key's later dates can be mistaken for proof that a true old pack fact is leakage.
3. A plausible familiar claim may be labeled supported from grader memory.
4. A fictitious D110 may be treated as `cannot_tell` instead of nonexistent.

The Flex masked score illustrates the last failure. The Vistra named leakage flag illustrates confusion between a factual date slip and use of future information: calling a March 2023 acquisition March 2024 in an April 2024 memo is incorrect, but both dates precede the desk cutoff. “Wrong date” and “post-cutoff knowledge” are different labels.

The saved scores contain fields such as `run`, `key_driver_count` and `reasoning_scorable`, while the shipped grader writes `run_file`, `model_run`, `grader_model` and `graded_at`. This does not prove scores are fraudulent. It means the exact score-producing harness and payload are not reproduced by the checked-in script. Archive that harness instead of claiming code-level reproducibility from a similar implementation.

## 5. Citation share is not grounding

The deterministic metric splits prose into sentences and looks for `\[D\d\d\]`. It:

- misses compact forms such as `[D02, D04]` and `[D02; D03]`;
- can count a bare valid-looking label even if the source does not support the claim;
- treats memo/driver repetition as extra observations;
- does not confirm the document exists;
- misses unsupported precise valuations attached to a source that merely reports revenue.

A high citation share is a formatting metric. A lower score can result from honest multi-document citation style. Rename it citation-format coverage and add:

1. reference existence;
2. atomic claim-to-span entailment;
3. unit/date/perimeter match;
4. fact versus assumption labeling;
5. arithmetic reproducibility;
6. source availability at cutoff.

Unsupported calculations should not become “supported” because one of their inputs occurs in D03. They need a source-to-assumption-to-formula bridge.

## 6. Reasoning overlap has both false positives and false negatives

**False-positive examples**

- Herbalife 15x a different EPS numerator credited as the same valuation mechanism as 10–12x $55–68.
- Chrysler SPV first lien credited as coverage of the actual purchased loan.
- Shell generic split credited despite different assignment of LNG assets.
- A four-quarter hold narrative credited as an immediate analyst-day technical rerating.

**False-negative/availability concerns**

- Hynix's HBM3E/product demand may partially overlap differentiation even when it does not reproduce all later qualitative detail.
- Flex's integrated infrastructure description overlaps part of product integration, though it omits the richer TPU/800V mechanism.
- Block's key requires an approval/economic detail expressly unrecovered in D07.
- Future CoStar/Soho share-count changes are counted as missing “reasons.”

Use atomic pre-registered mechanism rubrics, distinguish exact/partial/no match, and mark each driver stated by investor versus evaluator inference. Two blinded graders should adjudicate a stratified sample plus every disagreement; publish inter-rater agreement and disagreements, not just an LLM's aggregate count.

Do not reward future-outcome recall, penalize a valid independently derived investment reason as intrinsically wrong, or treat same-topic vocabulary as mechanism equivalence. Investor fidelity and economic validity are separate axes.

## 7. State logic and label inconsistencies

- Prompt 10 says ESCALATE must equal ESCALATE, yet Nestlé ADD is PARTIAL.
- Portfolio labels must match exactly, yet named HEDGE receives PARTIAL for REDUCE_GROSS while masked HEDGE is MISS.
- The state prompt does not fully define direction PARTIAL with low overlap; `grade.py` deterministically makes all non-MISS nonqualified outputs PARTIAL.
- With zero key drivers, `ceil(0.75*N)` is zero; code can assign state MATCH to an exact action despite having **no reasoning evidence**. Saved control scores instead show PARTIAL/NA-style handling, another sign of a different grading path.
- Controls have no documented manager rejection reason, so `discipline` should be an independently specified normative test, not “the reason Loeb gave.”

Make `reason_score=null` when N=0. Derive action and state categories in code from a fully specified table; preserve raw grader judgments separately.

## 8. Arithmetic failures that should block recommendation issuance

|Artifact|Observed failure|Required check|
|---|---|---|
|Baxter named|$1.50 ×20=$30 becomes $55; two-year $55/$42.13 described as 25% IRR|Every valuation contribution and timing explicit; annualized price return ~14.3% absent dividends|
|CoStar masked initiation|~$56/share calculation becomes $125 target; $75 floor exceeds modeled base|Reconcile growth premium, revenue guidance and scenario ordering|
|Endo masked r2|$4.55×25=$113.75 from $87.32 over two years called ~25% IRR|Price-only annualized return ~14.1%; “conservative” multiple is an assumption|
|Hertz masked r3|~$411m fleet residual called ~$8/share|At $787m cap/$5.53, ~142.3m shares; $411m/142.3m ≈$2.89|
|Hertz masked r3|45% upside versus 55% downside described as 2:1|Ratio ~0.82:1, not 2:1|
|Shell masked|Net debt subtracted from equity market cap; net debt reused as floor|EV = equity + net debt, then subtract claims to return to equity|
|Block named|Cash and modest consolidated net debt asserted to imply $45 floor|Lending/customer funds/warehouse liabilities and cash burn require a claim-level model|
|Flex masked|50x multiple/targets rely on nonexistent D110+ citations|Reject nonexistent references and unsupported target decomposition|

Recurring FCF or net cash can support a downside scenario; neither supplies a **hard** market-price floor. Current price as floor implies zero downside by construction and must fail validation.

## 9. Executable contract and staged-policy defects

The runner recomputes G1 hard fails from six criteria, a sensible safeguard. It then completes all later calls and, if final action is BUY or SHORT, flips it to PASS. It retains original bullish memo, nonzero size and potentially inconsistent `gate1_hard_fail` in the final object.

Observed examples: Greece named retains 3% and initiating language; GE masked r2 retains 4%; Hertz masked r2 originally SHORT is changed to PASS with residual short sizing. The audit trail should remain, but not in the field a downstream consumer treats as an executable memo.

Further defects:

- E7 SHORT is subjected to the same **long floor** veto; absence of long-equity recovery should not itself prohibit a short.
- No mandatory schema validation; `parse_json` can return `_raw`, and malformed stage objects may bypass fail checks.
- G2 NO_EDGE and G3 unsupported/weak valuation are not enforced by a deterministic decision table.
- Gate 1 sees the compressed fact sheet, not original docs. An omitted coalition or qualifier is unavailable to all downstream stages.
- The staged chain does not load AGENT; one-shot does. Existing and hedge modes bypass the multi-gate path entirely.
- OpenAI-compatible requests ignore `num_ctx` as an API parameter; actual backend context/truncation is not measured in the run.
- Forward prompt 12 does not rerun complete G1 discipline, allowing Solstice to be proposed despite the historical policy.

Keep `draft_final` and stage history for audit, but construct a separately validated `executable_decision` with zero position for PASS/invalid outputs, explicit conditionality and a reason code.

## 10. Controls and variance

Ten named PASSes and 27/30 masked PASSes are useful robustness observations, not an estimate of avoiding all bad investments. Controls were selected because they look like familiar traps; v1.5 was explicitly tuned after six initially bought. GE/Newell received D09 additions after omitted facts were diagnosed. Those are development improvements, not untouched validation.

The current D09 repairs themselves need a point-in-time audit. GE's October 1, 2018 packet contains an October 2 downgrade and a 2019 settlement; Newell's February 22, 2019 packet mentions a March retirement announcement. Explicitly labeling those facts later does not remove them from the model's context. Newell D09 also disagrees with D02/D03 on organic/core-sales decline figures without reconciling scope. Do not attribute the full control improvement to better rules until clean, content-hashed pack versions separate prompt changes from evidence changes. These observations establish defects in the present files, not which precise revision produced an un-hashed saved run.

Endo is bought twice masked; Hertz once. Hertz's erroneous residual valuation shows the danger of focusing on majority vote rather than unsafe tail outputs. One SHORT forcibly changed to PASS should not be credited as recognizing the expected no-equity-purchase discipline without separately recording its economic intent.

Absence from a reported long book does not establish never-held across swaps, shorts, intraperiod trades or non-reportable claims. An Endo score requesting acknowledgement of nonholding asks the agent to know a label, not underwrite public financials.

One named run versus three masked repeats also creates unequal selection/variance exposure. Use equal replication, paired randomization and report every output, not only majority results. Repeat means do not create additional independent historical decisions.

## 11. Intervals and aggregation

Wilson intervals quantify binomial sampling uncertainty under assumptions; they do not fix tuned selection, correlated cases, stochastic grading or model memory. Driver fractions pool correlated statements within a case and repeated themes across cases, so a Wilson interval over 161 “drivers” is not a valid independent-trial fidelity interval.

Use cluster bootstrap at campaign/decision-family level for exploratory summaries, with the small-sample limitation explicit. Report uncertainty for action sampling, repeat variance and grader disagreement separately. Named and masked outputs are paired, not independent datasets.

`tools/scoreboard.py` groups appended JSONL by model and a filename suffix; it does not recreate the rich reported scoreboard's eligibility filtering, holdout/control stratification or majority votes. Regrading appends duplicates; `__masked__r2` conventions can evade a simple suffix check. Require unique experiment/pack/version/seed IDs, explicit group metadata and a deterministic, idempotent rebuild.

## 12. Forward report is a different experiment

The forward table uses the **maximum probability across four coverage runs**, then a human reconciliation changes probabilities. That is not a calibrated ensemble. Honeywell moves from max .65 to .50; Solstice from .60 to .15. Both raw and human products should be scored separately, not whichever looks better afterward.

Specific defects:

- TDS ADD confirmation is an issuer asset-sale 8-K; Flex ADD confirmation is Innovation Day/registration statements; Bausch NEW_BUY confirmation is a refinancing. These establish company catalysts, **not Third Point trades**.
- Bausch is also described as an existing core credit HOLD in another run; an issuer label alone cannot distinguish a genuinely new security from existing exposure.
- Reconciliation says FedEx freight spin is in Q2 2027 “in F04”; **current F04 says distributed June 1**, and warns not to use old upcoming calendars. This is an internal source contradiction in the human reconciliation.
- Some HOLDs are assigned L4 or L1 even where the text means thesis intact, not opportunity-cost rotation or catalyst monetization.
- A post-cutoff filing can reveal a position acquired **before** the forecast date. Discovery of disclosure is not proof of economic action in the window.
- “60–90 days” to January 25 from October 25 is 92 elapsed days. Name the calendar endpoint rather than implying a different horizon.

The claim that forward buys are the “better-calibrated half” is not supported by five positive-only holdout buys. Calibration means probabilities agree with frequencies over a defined opportunity set, not that all preselected known purchases receive BUY.

The prospective protocol in the improvement plan resolves labels, dates, security identity and confirmation. It cannot retroactively turn this forecast into a fully preregistered unbiased test.
