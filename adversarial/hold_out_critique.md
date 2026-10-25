# What the sealed holdout does and does not establish

## 1. Integrity versus independence

I recomputed SHA-256 for every non-comment entry in `calibration/PROMPT_HASHES_v1.5.txt`: **all 18 entries match** the current AGENT and Markdown prompts. Preserve this evidence. The seal is dated October 25, 2026, 19:38Z, and the run log says holdouts ran after the freeze.

This establishes present-byte agreement with the manifest, **not an independently authenticated chronology** of who viewed the keys before writing the prompts. It also does not hash:

- `tools/run_agent.py`, `tools/grade.py`, aggregation code or JSON schemas;
- pack bytes, source extracts, answer keys, evaluator instructions or candidate-selection history;
- actual rendered requests, context truncation, backend checkpoint, sampling parameters or grader payloads.

The runner's saved model is “current,” not an immutable checkpoint identity. The scoreboard responsibly warns that its backend may know both calibration and holdout outcomes. Freezing prompts after assembling the whole archive is a tuning holdout, not a training-data holdout.

The forward-only Era E addendum contains post-boundary lessons, including CoStar's later exit. It is included in the hash list but the shipped staged historical runner does **not** append it. Its existence is therefore not proof that historical runs consumed holdout answers. Conversely, an operator using the addendum for historical replays would contaminate them. The forward workflow must record rendered inputs to demonstrate the separation.

AGENT also contains later institutional history such as the 2025 TPIL/Malibu conversion; a one-shot historical run consumes AGENT, whereas a staged run does not. A generic claim that “the same frozen agent” generated both policies is too broad.

## 2. Boundary selection and composition

Eligibility uses **first public disclosure after August 1, 2025**, not first trade. CoStar's Q2 add qualifies because it is disclosed August 14 even though the underlying original thesis was publicly known in April. This is clearly documented and defensible as a disclosure test; it is not a pre-action timestamp.

Composition is **five BUY, one ADD, three SELL, one TRIM, one REDUCE_GROSS**. There are **four** sells/trims, not five. The scoreboard's “0/5 sells and trims” wording appears to absorb the missed ADD into an exit denominator. Both runs have five exact actions out of eleven, all new-position purchases; neither matches any of the remaining six.

No rejected new idea is in this holdout. All five new-mode cases are buys, selected from disclosed holdings. Therefore:

- a new-mode-always-BUY strategy has 100% purchase recall;
- the holdout cannot estimate new-idea precision or false-positive rate;
- already-tuned controls do not supply a clean post-freeze negative set;
- thematic clustering—Ebara, Hynix, SK Square and Flex share AI/semicap infrastructure—reduces the independent diversity of eleven observations;
- two CoStar observations are dependent on the same campaign;
- Hynix and SK Square contain shared look-through economic exposure.

A broad archive is not a random opportunity set. To test selection skill, sample investable candidates before learning which ones were owned, including attractive nonholdings and unattractive actual holdings.

## 3. Action time is not explanation time

|Case|Desk information boundary|Later information in key|What can fairly be tested|
|---|---|---|---|
|CoStar ADD|June 30, possibly after actual additions|August share-count increase; rationale explicitly inferred|Forecast an undisclosed increase, not reconstruct a proven investment rationale|
|Soho SELL|August 15|August 18 event; August 20 zero-share filing|Before-event anticipation; a separate post-announcement response test is needed|
|CoStar SELL|December 31|Q1 failed remedy, entrenchment and reporting changes; April exit explanation|Precommitted thesis-risk monitoring, not reaction to as-yet-unseen refusal|
|Kenvue/KMB SELL|January 30|February factor rotation and economic-successor sale|Exposure/valuation forecast with uncertain instrument history|
|Mortgages TRIM|February 27|March term financing and >$300m risk sold|Financing-option analysis, not execution of unavailable terms|
|Portfolio REDUCE_GROSS|January 30|February targets/rotation, later retrospective letter|Risk budget sensitivity; actual gross/net path unavailable|
|Ebara/Hynix/Square BUY|June 30 before Q3 entry|October diligence/valuation descriptions|Mechanism inference from available issuer evidence|
|Block BUY|March 31 before Q2 entry|July own-bank/Borrow reasoning|Only the mechanisms supported by pre-cutoff public evidence|
|Flex BUY|June 30 inside entry quarter|July investor explanation/forecasts|Post-May separation underwriting; not necessarily pre-first-fill foresight|

**Two clocks are required:** a decision forecast frozen before an action window, and a response test supplied the public facts that later made that action sensible. Do not move the cutoff after seeing a miss and silently replace the old score. Keep both as different estimands.

Kenvue's exact successor mechanics and mortgage pool economics remain unresolved. Scoring a public common-equity proxy as the complete economic trade would compound the timing error.

## 4. Driver availability and post-cutoff vocabulary

Keys often honestly identify later explanations, but grading still treats their full content as an achievable denominator. Examples:

- Block D07 expressly says nationwide bank-origination approval details were not recovered. The key requires own-bank nationwide Borrow economics.
- CoStar exit D07 expressly excludes the later governance dispute and reporting change, while those are central key drivers.
- Hynix's **7x 2026 earnings versus peers 10–12x** is an October retrospective estimate, not a June quote.
- Ebara's pricing/cost-base and metal-CMP share diligence is not equivalent to a generic peer-margin table.
- CoStar ADD and Soho SELL count **future observed ownership changes** among their drivers. Those are labels, not contemporaneous causal explanations.

These limitations do not excuse the model's fabricated targets or invented activism. Report two separate rates: overlap with **all stated eventual reasons**, and overlap with **reasons supported or reasonably inferable from the allowed pack**. Have blinded reviewers assign the latter before seeing model outputs.

A related semantic leakage concern is future-window framing. Mortgage D07 says “cutoff before the potential March financing window”; masked output repeats that March execution has not yet been seen. Even without importing an actual result, an evaluator can telegraph which future event matters by choosing a narrow window around it. Negative statements such as “no subsequent exit statement included” may reveal the outcome category. Replace them with neutral document-availability notes.

## 5. D05 length: the measurable claim is not “controls have longer bears”

Whitespace word counts of the complete D05 files, including headers and URLs:

|Group|Number of packs|Median D05 words|Range|
|---|---:|---:|---:|
|47 calibration decisions|47|390|375–416|
|Discipline controls|10|360|351–377|
|Holdout|11|361|351–370|

**Controls are not longer on this measure.** A claim that their high PASS rate is caused simply by longer D05 documents is unsupported and has the sign wrong. The run log records a roughly 350–420-word construction requirement for the later packs; length looks template-driven.

The substantive concern is **density and framing**, not raw length. D05 commonly begins with one issuer-specific paragraph followed by repeated instructions about claim priority, risk, valuation and observable checks. This:

1. consumes context without adding independent evidence;
2. creates uniform “bear case” salience even where actual public skepticism is thin;
3. gives the analyst/evaluator control over which economic risk is foregrounded;
4. lets generated conditional analysis masquerade as multiple independent source confirmations when repeated across documents.

A fair ablation holds factual content constant, then compares neutral ordering, matched-length bull/bear summaries and raw source extracts. Measure changes in actions **and grounded mechanisms**. No such ablation was run here.

## 6. D08 fund context is stale and often outcome-shaped

Holdout D08 repeats the April 2025 report: **$19.3bn firm AUM**, 98.1% equity long, 51.7% short, 46.4% net and 34.6% credit net. These are explicitly labeled stale, which is good. They nevertheless provide weak capacity information at January–June 2026.

Missing items include current fund NAV, unrestricted cash, gross financing commitments, sector/AI correlations, option deltas, specific opportunity costs, position targets, stop/kill thresholds and legal trading constraints. AUM is not capital available to the strategy. Combining a firm-wide AUM with one feeder's exposures and a 13F common-stock baseline does not produce a coherent risk budget.

Some D08 additions are economically sensible but case-targeted: Block consumer-finance risk, Flex compute-capex correlation, CoStar engagement restrictions, Kenvue successor mechanics. Their quality varies with how much the pack author knows about the eventual action. A standardized context snapshot built independently of the chosen answer would be less vulnerable to label-dependent framing.

For a sell test, include comparable alternatives at the same cutoff. Otherwise L4 “better use of capital” is largely unobservable. For gross reduction, include actual long/short and financing vectors, not a company memo.

## 7. Financial enrichment helps, but retrospective recovery is not proof of availability

The run log documents enrichment of D02/D03/D04/D06. This improves numerical grounding substantially, but current metadata/keys sometimes still claim cutoff prices were not recovered even where enriched D04 supplies them. Massey's contradictory D02/D04 statement is a particularly clear stale-edit example.

Ebara's five-year table is retrieved from a later Integrated Report 2025; market rates can be retrieved from later published tables; peers use mixed fiscal ends and stale shares/debt. A historical period is not itself an availability timestamp. A rigorous ledger needs:

- original publication date and archive retrieval date;
- original versus restated financial values;
- split-adjustment conventions and share classes;
- numerator/denominator periods and currency;
- whether a later database is merely reproducing an already-public value.

Do not call every later retrieval leakage: a later database can faithfully reproduce an old close. Do not assume every old fiscal period was public at the cutoff either. Verify the vintage.

### Direct cutoff violations in the control supplements

The current control supplements provide a stronger finding than a generic concern about retrospective databases. `calibration/data_packs/ctl_2018_ge_pass/docs/D09_governance_and_liabilities.md`, under an **October 1, 2018 cutoff**, explicitly includes the WMC settlement “for $1.5bn in 2019,” the S&P downgrade on October 2, and an investigation expansion described only as “October 2018.” Marking a result “after this date” does **not** make it permissible model-facing evidence. The same document says Power's goodwill “was written off on 1 October,” whereas D02 describes an expected substantial impairment. An announcement, expected charge and booked accounting result must not be collapsed. The full-year-sounding “2018 orders fell 26%” also requires an observation-period and publication-date check; the generic source list does not establish it was public on October 1.

`ctl_2019_newell_pass/docs/D09_other_activists.md`, cut off February 22, explicitly mentions Michael Polk's retirement announcement in **March 2019**. It additionally reports full-year/Q4 core-sales declines of **4.0%/3.7%**, while D02/D03 report **5.2%/1.2%**. Different reporting perimeters might explain those figures, but the supplement does not reconcile them. An inference about secular deterioration must not choose whichever series supports a desired PASS.

These are **current-file defects**, not proof that every saved run received precisely this revision. Saved runs lack input-content hashes sufficient to settle that question. They nevertheless undermine any assertion that all current control evidence is cutoff-clean. D09 was added during control repair; the resulting PASS rates cannot validate either the chronology or the repair independently. Remove post-cutoff outcomes from model-facing documents, retain them only in evaluator notes, reconcile the financial periods, and rerun under a new pack version rather than silently replacing historical inputs. Separately, GE D06 actually lists **24.3% for both Aviation and 3M**: a run using that Aviation margin is not, by itself, evidence that it stole the peer's margin. The demonstrable valuation error is applying earnings multiples directly to segment revenues, not the coincident margin.

## 8. Masking is identity obfuscation, not economic anonymization

`load_pack()` substitutes company/ticker/aliases with one generic string using case-insensitive regexes. It does not create a synthetic economic twin. Unique product combinations, officers, institutions, dates, URLs/CIKs and unusual transaction facts remain identifiable; some aliases are partial and can distort unrelated words. Replacing target and subsidiary names with the same phrase also destroys entity relationships.

Observed masked outputs rediscover Greece, Colgate, Disney and NestléNOW. That can be memory, unremoved tokens, or unique economic inference; the saved pair does not identify which. A mask that removes every economically distinctive fact would itself destroy the investment case.

Use randomized entity IDs consistently across the legal-entity map, strip source-domain identity from model-facing text while retaining evaluator access, and audit leakage separately from citation integrity. Add synthetic **counterfactual mutations** to distinguish genuine reasoning from recalled outcomes. Do not report masked accuracy as an out-of-sample guarantee.

## 9. Bottom line

The holdout is useful as a candid **frozen-prompt stress test on later-disclosed cases**. It is not a clean estimate of autonomous investment selection, pre-action foresight, or causal fidelity to private manager reasoning. Keep its poor scores visible; qualify their estimand; rebuild neither dates nor labels merely to make a new version win. The next untouched prospective tranche must be selected and sealed before observed manager actions, with matched negatives and a documented adjudication protocol.
