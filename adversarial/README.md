# Adversarial review of the Loeb agent

## Verdict

**Useful event-investing research scaffold; not a validated replica of Loeb's decisions, and not execution-safe.** The frozen chain's reported 81%/79% calibration direction scores obscure a highly favorable task distribution: every one of its 30 new-position calibration labels is BUY. A mode-only policy scores 41/47 exact actions (87%), without reading a company. On the eleven holdouts, buying all five new ideas reproduces the chain's five exact matches; neither version gets any of the other six actions exactly right. The 16–18% holdout driver overlap is a more informative warning than purchase accuracy. However, several purported sell failures are forecasts made before the information that explains the eventual sale, so they do not establish that a contemporaneous investor should have sold. Serious arithmetic, grading and claim-grounding defects coexist with impressive archival work. Fix measurement and the executable decision contract before adding more investor-specific exceptions.

This is a **static independent review**, not a new model tournament. No production prompts, packs, keys, scores or tools were changed. No API/model calls or fresh agent runs were made. Manual untuned predictions below are explicitly forecasts of the chain, not experimental results.

## Ranked findings by likely effect on the scoreboard

Ranking reflects breadth of affected observations and confidence in the diagnosis, not a fabricated estimate of the improvement obtainable by tuning.

|Rank|Finding|Scoreboard consequence / evidence|
|---|---|---|
|1|Selection and mode reveal most labels.|Calibration keys: new 30 BUY; existing 7 ESCALATE, 3 SELL, 2 TRIM, 1 HOLD; hedge 4 REDUCE_GROSS. Choose each mode's modal action: **41/47** exact. This exceeds both headline directional MATCH rates, although their rubric additionally penalizes size. Holdout new-mode BUY alone gives **5/11**, exactly the observed match count.|
|2|The claimed exit test frequently withholds the event that makes exiting rational.|Soho cutoff August 15 precedes August 18 transaction; CoStar December 31 precedes first-quarter governance developments; Kenvue and risk decisions use January 30 before February factor rotation; mortgages February 27 precedes March financing. Score anticipation separately from response to observed evidence. Four calibration keys explicitly mark themselves ineligible yet remain in the headline directional denominator.|
|3|The grader cannot reliably establish what its claimed evidence supports.|`tools/grade.py` does not fill `pack_index` or supply documents. The citation statistic checks syntax, not entailment. Flex masked invents D110/D116/D221 and a 50x multiple; its score still records direction MATCH. Unit-confused sizing penalties turn correct BUY actions into PARTIAL.|
|4|The model habitually manufactures attractive asymmetry.|Baxter: $1.50 EPS ×20 becomes a $55 target; CoStar masked: ~$56 arithmetic becomes $125; Hertz masked: ~$411m residual equity becomes $8/share rather than ~$2.89 on the pack-implied shares. Endo annualized return and Block's “hard floor” also fail scrutiny. These are action-enabling errors, not cosmetic prose.|
|5|The frozen chain is much less successful at reproducing mechanisms than actions.|Calibration driver overlap 93/161 named, 81/161 masked; holdout 7/38 and 6/38. Block becomes an activist margin-gap trade, not the key's consumer underwriting/network economics. Ebara becomes a generic conglomerate repair; Hynix a run-rate multiple exercise.|
|6|Several published divergence explanations contradict the saved runs.|Campbell named **passes** the floor and fails edge/route; CoStar named does not mention D.E. Shaw; Baxter masked has four FAILs, not six UNSUREs; Shell masked identifies E1. Tuning against the prose diagnosis would repair the wrong failure.|
|7|Discipline rules are both overfit and economically overbroad.|“Someone else's fight” conflicts with InterCept/JANA and BindView/Chapman collaboration; quality only from 2016 excludes Roper 2015. Forced PASS after a long-floor failure can suppress a legitimate SHORT. Endo and Hertz nonetheless escape the intended safeguards in some masked runs.|
|8|Masking is not a controlled memory test.|Aliases and tickers are replaced, but distinctive economics, executives and URLs remain. Masked Greece explicitly identifies Greek debt; Colgate names Colgate; Disney names Disney. One named/masked pair confounds stochastic variance, compression and identity. No causal “memory effect” is established.|
|9|Portfolio constraints are acknowledged but not usable.|D08 repeatedly supplies stale April 2025 gross/net and firm AUM, not current fund NAV, target attainment, liquidity, expected returns of alternatives or private liabilities. L4 is therefore usually untestable; L5 can become indefinite patience. Size recommendations remain falsely precise.|
|10|Reproducibility is weaker than a matching prompt seal suggests.|All **18** entries in `PROMPT_HASHES_v1.5.txt` match current bytes. That is good integrity evidence, not proof of execution chronology. The seal excludes tool code, schemas, pack/key versions, backend checkpoint and grader inputs; saved score fields differ from the shipped grader's output fields. Staged and one-shot policies are also different.|

## What deserves credit

- The compendium distinguishes issuer ownership, fund NAV, filing marks, actual execution and realized returns more carefully than many investment datasets.
- Numerous keys acknowledge retrospective explanations, unknown transaction dates and inferred motives rather than fabricating certainty.
- Holdout results are disclosed despite being poor, and hard-fail overrides retain the original memo for audit.
- The design recognizes creditor rights, sovereign process, E2 technical trades, operating inflections and different activist roles. The problem is reliable application and evaluation, not absence of a useful conceptual vocabulary.
- Controls have dated negative cases and multiple masked runs. These are valuable stress observations, though “not observed in a 13F” is not a documented investment-committee rejection.

## Contents

1. [Untuned manual predictions](predicted_decisions_untuned.md): fifteen additional real decisions, explicitly separated from blinded empirical performance.
2. [Divergence analysis](divergence_analysis.md): every row in the published divergence table, all holdout nonmatches and mechanism failures.
3. [Holdout critique](hold_out_critique.md): seal, chronology, information availability, pack framing and leakage.
4. [Eight red-team pack designs](red_team_packs.md): falsifiable paired tests, not invented historical data.
5. [Grader and method critique](grader_and_method_critique.md): action baselines, denominator corrections, arithmetic and executable-policy audit.
6. [Proposed v1.6 plan](improvement_plan_v1_6.md): exact rule edits, acceptance tests and prospective January–February 2027 protocol.

## Audit scope and evidence conventions

Read the main README, AGENT, every Markdown prompt, calibration README/scoreboard/seal/manifest, research critique, forward prediction and run log; inspected the runner, grader and aggregator; sampled the archival principles/patterns and sibling adversarial work. Examined named/masked artifacts for all fourteen published divergence rows, eleven holdouts and Endo, GE, Newell and Hertz controls, including repeat control runs. Read the corresponding keys, fifteen additional compendium dossiers, and substantive pack evidence across Massey, Campbell, CoStar initiation, Greece, Ebara, Block and Endo, plus holdout chronology/context documents. Repeated generic pack paragraphs were compared rather than treated as new source evidence.

All paths in the reports are relative to `loeb-agent/`. For a calibration ID `x`, `R(x,N)` means `calibration/runs/x__current__named.json`; `R(x,M)` is the masked counterpart; `K(x)` is `calibration/answer_keys/x.json`; `P(x,Dnn)` is that document in `calibration/data_packs/x/docs/`. Holdout keys and scores are in their `holdout/` subdirectories; holdout runs remain in the ordinary runs directory. Control repetitions use the saved repeat suffixes. Quoted run language identifies what the artifact says, not a verified company fact.

Limitations: no fresh external-source authentication, no blind second human grading, no replay at a fixed model checkpoint, no causal ablation. Some source periods are recovered from later databases and reports. This review can establish internal inconsistencies and observable failures; it cannot certify that the supplied historical dataset is exhaustive or that any proposed revision improves unseen investment performance.
