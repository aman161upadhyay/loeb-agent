# Building an investor-persona agent: literature and practice survey

**Research date: 2026-10-25.** Objective: reproduce Ackman's **decision and documented contemporaneous drivers**, not maximize backtest returns or imitate his voice. Read alongside `lookahead_and_evaluation.md`. Numbers below are authors' reported results, not independently reproduced. Recommendations are project design proposals, not claims that the literature has validated an Ackman clone. Source dates and URLs are in the source register; `[A#]` references apply to the preceding claim/table row.

## 1. The central distinction

Four different achievements are frequently conflated:

1. **Stylistic resemblance:** sounds like a famous investor.
2. **Doctrine implementation:** applies rules attributed to that investor.
3. **Behavioral resemblance:** chooses the same action on the same information.
4. **Reasoning fidelity:** chooses it for the investor's documented reasons, respects exclusions, and changes course when the investor's actual process would.

GuruAgents demonstrates doctrine-conditioned strategies, not trade-by-trade cloning. TradingAgents, FinMem, FinAgent, FINCON, and FinRobot primarily study trading capability or workflow architecture. Newer InvestLogicBench and InvestPhilBench move closer to process measurement, but neither establishes that an off-the-shelf prompt faithfully reproduces Bill Ackman's historical investment process. This distinction follows from their tasks and evaluation designs, not from their headline returns. [A2–A9, A20–A22]

**Our recommended unit of implementation:** an evidence-backed decision program: dated principle → eligibility gate → load-bearing drivers → variant perception → valuation/scenario calculation → feasible action/catalyst → disconfirmation/exit rule → portfolio fit → concise cited decision. Voice is optional; sources and gates are not.

## 2. Source audit: `virattt/ai-hedge-fund`

### 2.1 Version provenance matters

At retrieval on **2026-10-25**, GitHub API reported **64,231 stars; 11,265 forks**. These are a dated popularity snapshot, not validation. The README describes a proof of concept for educational/research purposes, not real trading/investment advice; no guarantees, no liability for losses, and past results do not imply future results. Its current installation is `aihf`, with paper-trading/backtesting interfaces. The README also says the system does not actually make trades. [A1]

**Important discovery:** the requested `main/src/agents/bill_ackman.py`, `warren_buffett.py`, and `charlie_munger.py` raw URLs returned **404**. Repository history shows a 2026-08-02 migration, “Make 2.0.0 the default,” commit `a7a99e5b4cbbe789f4e16bd02d794e86a2a3a3d2`. The current tree contains `hedge_fund/signals/buffett.py` and `munger.py`, but no filename containing `ackman`. Do not silently describe the old source as current `main`. [A1]

**Actual historical source fetched and inspected:** commit **`bffa661bb0372be4c3ee2661f525bf162e8d6da0`**, **2025-07-28**, the last content-changing commit returned before the deletion/migration for the requested Ackman path:

- Ackman: https://raw.githubusercontent.com/virattt/ai-hedge-fund/bffa661bb0372be4c3ee2661f525bf162e8d6da0/src/agents/bill_ackman.py
- Buffett: https://raw.githubusercontent.com/virattt/ai-hedge-fund/bffa661bb0372be4c3ee2661f525bf162e8d6da0/src/agents/warren_buffett.py
- Munger: https://raw.githubusercontent.com/virattt/ai-hedge-fund/bffa661bb0372be4c3ee2661f525bf162e8d6da0/src/agents/charlie_munger.py

All descriptions in §§2.2–2.5 refer to that **pinned historical version**, not the rewritten package. [A1]

### 2.2 Ackman: data flow and exact score logic

For each ticker, the agent obtains **five annual** financial-metric observations and five annual observations for `revenue`, `operating_margin`, `debt_to_equity`, `free_cash_flow`, `total_assets`, `total_liabilities`, `dividends_and_other_cash_distributions`, and `outstanding_shares`, using `end_date`; separately obtains market capitalization. It assumes newest-first ordering. There is **no news, filing text, peer set, management biography, activist campaign, portfolio exposure, or options data input** in this function. Intangible assets are commented out. [A1]

| Component | Implemented rule | Points |
|---|---|---:|
| Business quality: growth | With ≥2 nonmissing revenue values, oldest and newest truthy and newest > oldest: cumulative `(newest-oldest)/abs(oldest)` >50% | +2 |
| Same, modest growth | Positive cumulative growth ≤50% | +1 instead |
| Quality: margins | Strict majority of available operating margins >15% | +2 |
| Quality: cash | Strict majority of available FCF values >0 | +1 |
| Quality: ROE | Latest metric's ROE truthy and >15% | +2 |
| Discipline: leverage | Strict majority of available debt/equity observations <1.0 | +2 |
| Leverage fallback | Only if **no** D/E values: strict majority of computable liabilities/assets <50%; denominator for majority is length of computed ratios | +2 instead |
| Discipline: distributions | Strict majority of nonmissing distributions **negative**, following the API cash-outflow sign convention | +1 |
| Discipline: repurchases | ≥2 nonmissing share counts; newest < oldest | +1 |
| “Activism potential” | ≥2 revenues and any margins; cumulative growth >15% **and** arithmetic mean operating margin <10% | +2 |
| Valuation | Positive latest FCF and market cap not `None`; modeled upside >30% | +3 |
| Same, weaker discount | Modeled upside >10% but ≤30% | +1 instead |

“Strict majority” is `count >= floor(number_available/2)+1`; only the fallback leverage implementation compares its numerator to the number of computed ratios. Quality and discipline return zero immediately if either metrics or line items is empty; activism and valuation have their own missing-input branches. Missing data therefore depresses scores rather than representing uncertainty separately. [A1]

**DCF, exactly:** let latest FCF be \(F\). Growth =6%, discount =10%, horizon =5 years, terminal multiple =15× year-5 FCF:

`V = Σ[t=1..5] F*(1.06)^t/(1.10)^t + 15*F*(1.06)^5/(1.10)^5`.

The code calls `(V-market_cap)/market_cap` “margin_of_safety.” This is upside relative to price, **not** `(V-price)/V`; the two should not be interchanged. If latest FCF is missing or ≤0 it returns zero valuation points and no intrinsic value. No debt/cash bridge, maintenance/growth capex separation, scenario range, or security-specific valuation is implemented. Market cap zero is not guarded before division. [A1]

**Combination:** `total = quality + discipline + activism + valuation`. The literal `max_possible_score = 20`; bullish if ≥14, bearish if ≤6, neutral otherwise. **Actual component maxima are 7+4+2+3=16, not 20.** Thus the bullish bar is 14/16=87.5% of achievable points. Moreover, a positive-growing company that earns the activism bonus for mean margins <10% may conflict with earning the quality-margin bonus, depending on the distribution of annual margins. This is not a principled calibrated probability. [A1; arithmetic from source]

The numeric signal and all component details are placed in `analysis_data[ticker]`; a separate LLM then issues the final signal. The prompt receives the **whole accumulated `analysis_data` dictionary**, including previously processed tickers, not just the current ticker. The final signal need not equal the deterministic signal; no reconciliation check is implemented here. The final ticker-keyed object is emitted as a named `HumanMessage` and stored in `state["data"]["analyst_signals"][agent_id]`. [A1]

### 2.3 Ackman prompt and output contract

The following is the pinned source's system prompt, reproduced for reproducibility under the repository's MIT license; indentation normalized, words retained. [A1, 2025-07-28]

```text
You are a Bill Ackman AI agent, making investment decisions using his principles:

1. Seek high-quality businesses with durable competitive advantages (moats), often in well-known consumer or service brands.
2. Prioritize consistent free cash flow and growth potential over the long term.
3. Advocate for strong financial discipline (reasonable leverage, efficient capital allocation).
4. Valuation matters: target intrinsic value with a margin of safety.
5. Consider activism where management or operational improvements can unlock substantial upside.
6. Concentrate on a few high-conviction investments.

In your reasoning:
- Emphasize brand strength, moat, or unique market positioning.
- Review free cash flow generation and margin trends as key signals.
- Analyze leverage, share buybacks, and dividends as capital discipline metrics.
- Provide a valuation assessment with numerical backup (DCF, multiples, etc.).
- Identify any catalysts for activism or value creation (e.g., cost cuts, better capital allocation).
- Use a confident, analytic, and sometimes confrontational tone when discussing weaknesses or opportunities.

Return your final recommendation (signal: bullish, neutral, or bearish) with a 0-100 confidence and a thorough reasoning section.
```

Human template:

```text
Based on the following analysis, create an Ackman-style investment signal.

Analysis Data for {ticker}:
{analysis_data}

Return your output in strictly valid JSON:
{
  "signal": "bullish" | "bearish" | "neutral",
  "confidence": float (0-100),
  "reasoning": "string"
}
```

The braces in actual LangChain template text are escaped as `{{`/`}}`. The Pydantic class is `BillAckmanSignal`: `signal: Literal["bullish","bearish","neutral"]`, `confidence: float`, `reasoning: str`. **0–100 is a prompt instruction, not a validated numeric range** in this class. There are no citations, driver IDs, information-date fields, actions/sizing, falsifiers, or distinction between sell and initiate-short. `call_llm` receives a fallback factory returning neutral, confidence 0.0, reasoning `"Error in analysis, defaulting to neutral"`. Thus implementation failure can masquerade as a substantive neutral opinion unless separately recorded. [A1]

### 2.4 Buffett and Munger: what the adjacent implementations add

| Feature | Buffett pinned source | Munger pinned source |
|---|---|---|
| Inputs | 10 TTM metrics/line-item observations: capex, D&A, net income, shares, assets/liabilities/equity, distributions/equity issuance, gross profit, revenue, FCF | 10 annual observations including ROIC, margins, R&D, goodwill/intangibles, cash/debt; up to 100 insider trades and 100 news items |
| Analysis functions | Fundamentals; consistency; moat; pricing power; book-value growth; management quality; intrinsic value | Moat; management; business predictability; valuation; news sentiment |
| Design choices | ROE >15%, D/E <0.5 among fundamental rules; circle of competence explicitly delegated to LLM; owner-earnings-oriented valuation and multiple quality signals | Weighted score: moat .35, management .25, predictability .25, valuation .15; bullish ≥7.5/10, bearish ≤4.5, neutral between |
| Prompt emphasis | Circle of competence, durable moats, management, value; also asks for folksy voice | Inversion, mental models, quality/ROIC, patient concentration; direct voice |
| Shared limitation | Same three-field signal/confidence/reasoning contract; neutral/0 fallback; LLM synthesis is not an audited deterministic execution | Same; comments claim two-year insider/one-year news windows but calls use `start_date=None` and limits, not enforced fixed windows |

These are **actual source inspection findings**, not evidence that either reproduces its named investor. Reuse modular analysis and structured output; do not transplant style adjectives or arbitrary weights as ground truth. Buffett's score normalization also deserves auditing: total includes consistency while the stated denominator components do not explicitly allocate it. [A1]

### 2.5 Why this is not yet an Ackman process model

**Business quality is not ROE >15%.** Ackman's stated Netflix exit ties predictability directly to concentrated ownership: “We require a high degree of predictability in the businesses in which we invest due to the highly concentrated nature of our portfolio.” He sold despite allowing that Netflix could still be successful and a good investment. This is a process distinction between *good asset*, *predictable thesis*, and *appropriate concentrated position* which the score cannot express. [A10, 2022-04-20]

| Missing mechanism | Consequence | Proposed implementation |
|---|---|---|
| Specific activism/catalyst | Growing revenue + low margin says nothing about a fix, authority, successor, votes, timing, or costs | Require feasible intervention, responsible actor, control/board constraints, peer gap, milestones; allow passive ownership where no activism is needed |
| Concentration and opportunity cost | “Concentrate” is in the prompt but no current positions, liquidity, correlated exposure, or alternatives enter | Separate security attractiveness from portfolio action; conviction must survive predictability and downside gates |
| Hedging/security choice | No credit, options, duration, premium, convexity, hedge-notional/payoff fields | Separate macro-hedge and equity modules; evaluate carry, loss budget, triggers and portfolio protection, not equity DCF |
| Economic moat | Accounting margins/ROE are proxies, not evidence of pricing power, customer behavior, replicability, franchise durability or disruption | Evidence checklist for business model, recurring demand, switching/franchise advantages, reinvestment economics and external risks |
| Pass discipline | Low quality, unavailable data, no catalyst, expensive price, and deliberate pass collapse toward bearish/neutral | Explicit pass reasons and unknowns; bearish thesis ≠ instruction to short |
| Exits and reversals | Snapshot has no original thesis or updated uncertainty | Maintain thesis state; distinguish valuation achieved, thesis broken, predictability lost, and opportunity-cost sale |
| Historical process changes | One timeless persona cannot represent evolving mandate/process | Dated principles and case-based exceptions; only retrieve rules known at replay date |
| Evidence grounding | Prompt requests brand/catalyst analysis absent from inputs | Evidence IDs compulsory; unsupported catalyst = unknown, not invention |
| Causal reasoning | LLM can narrate a favorable ratio as a moat | Require mechanism, magnitude and falsifiable condition for each driver |

These are code-to-objective gaps. They are not a claim that Ackman always follows one invariant rule or that every investment is activist. The source archive must supply actual dated rules and exceptions; Netflix is a verified example of an exit principle, not a universal inferred policy. [A1, A10]

## 3. Research architectures and what to borrow

### 3.1 GuruAgents — Kim, Lee, Kim & Lee, 2025-10-02

Five GPT-4o agents encode **Benjamin Graham, Warren Buffett, Joel Greenblatt, Joseph Piotroski, and Edward Altman**. Prompts combine role/creed/quotes, allowed tools, metric definitions, eligibility, scaling/scoring, tie-breaks, portfolio weights, missing-data rules and a strict output table. Tools calculate finance metrics; prompts prescribe a nominally deterministic reasoning/ranking pipeline. This is much more concrete than “be Buffett,” but “deterministic” in prompt text does not prove deterministic LLM execution. [A2]

Example Buffett encoding: 5th–95th percentile winsorization and min–max scaling; valuation subscore `.55*FCFYield + .25*(1-PB) + .20*(1-PE)` using scaled ratios; bonuses for ROE ≥15% with D/E ≤0.5, coverage ≥10 and margin ≥15%; penalties for leverage, high valuation and nonpositive FCF. Base weights and quality additions are hand-specified. Output is ticker/score/whole-percent weight/one-sentence reason; include eligible names and normalize to 100%. This is **the authors' engineering interpretation**, not a recovered Buffett policy. [A2, appendix A]

**Backtest:** NASDAQ-100, Q4 2023–Q2 2025, quarterly rebalance, reported transaction cost 0.01% of gross turnover per quarter. [A2]

| Agent/benchmark | CAGR % | Annualized Sharpe | Max drawdown % |
|---|---:|---:|---:|
| Graham | 28.74 | 1.01 | -23.89 |
| Buffett | 42.23 | 1.40 | -22.34 |
| Greenblatt | 19.38 | 0.87 | -20.74 |
| Piotroski | 30.93 | 1.14 | -23.07 |
| Altman | 25.74 | 0.96 | -21.71 |
| NASDAQ-100 | 29.36 | 1.32 | -22.77 |
| S&P 500 | 26.31 | 1.47 | -18.76 |

**Interpretation/caveats:** Buffett's CAGR leads, but S&P 500's reported Sharpe is higher. Short, tech-heavy sample is not an all-regime test. Universe membership/availability must be independently checked for survivorship and filing-date leakage. Authors say their window is beyond GPT-4o's knowledge cutoff, but a family name without exact snapshot/training audit does not establish this for every tested observation; verify the precise model version and post-training provenance. They do not grade agreement with gurus' actual contemporaneous trades/drivers; philosophical-alignment metrics are future work. A one-sentence reason is not a reasoning check. Prompted accounting formulas may drive differences without any true investor simulation. [A2; critique of design]

**Borrow:** explicit tools, missingness rules, gates, deterministic arithmetic, fixed output contract. **Reject as evidence:** returns → persona fidelity; quote inclusion → recovered decision process.

### 3.2 TradingAgents — Xiao, Sun, Luo & Wang

First posted **2024-12-28**; latest inspected version **v7, 2025-06-03**. Analyst lanes cover fundamentals, news, sentiment and technicals; bull and bear researchers debate the case; a manager/facilitator synthesizes; trader proposes a plan; risky/neutral/conservative risk agents challenge it; final portfolio-level approval follows. Structured reports plus natural-language discussion limit information loss; quick-thinking GPT-4o-mini/GPT-4o and deeper o1-preview split retrieval/summarization from difficult judgments. [A3]

**Version caution:** v1 reports a June–November 2024 simulation; v7 evaluates January 1–March 29, 2024. Do not combine dates from one version and performance from another. V7 table includes AAPL, GOOGL and AMZN, while dataset discussion also names other large tech companies. For AAPL the v7 table reports 26.62% cumulative return, 30.5% annualized return, Sharpe 8.21 and 0.91% drawdown. Authors caution that unusually high Sharpes reflect the short test period/few pullbacks; budget limits constrain longer evaluations. These results are not robust evidence of deployable alpha. [A3]

**Cost per decision: unverified, not numerically reported in inspected v1/v7 text.** No defensible universal dollar figure was located. The paper discusses API-credit/budget limits; do not turn a later implementation's price into a paper result. A separate 2026 community reproduction search result reports ~$3.70 for 13 decisions (~$0.285 each), but that is its particular 104-deep/39-quick-call configuration, not Xiao et al.'s measured cost. Treat it as low-grade operational context only. Our runner must measure input/output tokens, retrieval fees, elapsed time and retries per decision; calculate cost with frozen dated model prices. Local inference has time/energy/opportunity cost, not zero cost. [A3, A23]

**Caveats:** no trade-driver agreement rubric; no guarantee debates eliminate confirmation bias; repeated correlated model voices are not independent analysts; more turns increase latency and permit persuasive unsupported narratives. Point-in-time text filtering cannot remove pretrained knowledge. Borrow a **single short disconfirming-evidence pass**, not a full desk simulation, unless calibration shows a fidelity gain per unit cost. [A3; project interpretation]

### 3.3 Related agent systems

| Work, date | Mechanism and reported evidence | Value / limitation for this project |
|---|---|---|
| **FinMem**, Yu et al., 2023-11 arXiv; 2024 AAAI spring symposium | Profiling, memory, decision modules; shallow/intermediate/deep memory. Retrieval blends recency, relevance and importance with layer-specific decay; important/repeatedly accessed events can move deeper. Inspected experiments span 2021-08-15–2023-04-25. [A4] | Separate stable principles from recent thesis facts; date-aware memory. Character/risk settings are not validated imitation of a named investor. Reward-labeled training episodes must not enter held-out replay. |
| **FinAgent**, Zhang et al., 2024-02-28, revised 2024-06-28 | Multimodal market intelligence; vector memory; low-level price/news reflection; high-level decision/outcome reflection; tool-augmented decision. Six datasets, including ETHUSD; June 2022–January 2024, latter part testing; abstract reports >36% average improvement and 92.27% return on one dataset. [A5] | Provenance-aware evidence pipeline useful. Chart/image/reward reflection adds complexity and could change the persona toward a generic profitable trader. Headline one-dataset return is not fidelity evidence. |
| **FINCON**, Yu et al., 2024-07, NeurIPS 2024 | Manager–analyst hierarchy; risk control; working/procedural/episodic memories; conceptual verbal reinforcement (CVRF) modifies beliefs/prompts from training-episode performance. Inspected test window 2022-10-05–2023-06-10; COIN example >57% return, Sharpe .825. [A6] | Hierarchical evidence compression is useful. Optimizing beliefs against P&L selects a new strategy, not Ackman's process; never perform reward-based reflection using hold-out outcomes. |
| **FinRobot**, Yang et al., 2024-05-23 arXiv | Four layers: financial agents; financial algorithms; LLMOps/DataOps; multiple foundation models. Financial CoT, scheduling and tool/data routing; qualitative forecasting/report demonstrations. [A7] | Useful infrastructure ideas, not a validated named-investor clone or proof of return performance. Require the same citation/date controls for every routed source. |
| **InvestorBench**, Li et al., ACL 2025 | Benchmark for LLM financial decision-making agents. [A8] | Useful capability baseline; action/P&L evaluations do not establish agreement with one person's actual reasons. |
| **Long-run investing evaluation**, arXiv 2505.07078, inspected v4 2025-11-25 | Broader comparison including FinMem/FinAgent and rule-based strategies; concludes LLM investors are not universally superior even in preferred setups. [A9] | Stress-test generalization claims; our target remains fidelity rather than a leaderboard of returns. |

### 3.4 Specific-investor reasoning and persona research, 2025–2026

Broad searches included “LLM agent replicate investor decision process,” “persona fidelity evaluation LLM,” “digital twin investor,” “point-in-time backtest LLM,” and Buffett/Munger/Ackman persona terms. Results must be separated into validated benchmarks, conceptual papers and GitHub wrappers; absence from this survey is not proof that a work does not exist.

- **InvestLogicBench**, Jiang et al., **2026-08-06**, arXiv **2608.06108**: 201,247 documented decisions from 151 investors; **Person → Events → Reasoning → Decision → Outcome** representation; profile-conditioned generation, comprehension and replay. Abstract reports logical plausibility near 4/5 but event grounding only 0.8–2.8/5 across models. Highly relevant: plausible investment prose can be weakly tied to actual evidence; returns and process scores diverge. Its large extracted corpus is not automatically a human-verified ground-truth archive: inspect extraction, event timestamping, rationale provenance and public-selection bias before reusing. [A20]
- **InvestPhilBench**, Chen & Qu, **2026-06-24**, arXiv **2606.25984**: nine canonical investors; 118 primary-source-verified principle cards, 25 framework cards, 243 questions (197 dev/46 test); eight cognitive tiers; closed-book, RAG and oracle-source conditions. Metrics include ordered-gate reconstruction, concept coverage, source attribution and kill-criterion activation. Reported frontier gate-reconstruction accuracy ~.77 on L4 versus .57–.62 on L7; a composite can hide procedural deficits. Authors explicitly call the v0.6 wave preliminary and mixed-judge/confounded; full perturbation, dual-human reliability and a unified leaderboard are deferred. Strong design inspiration, not settled evidence. Embedding-based “investor voice” is less useful to us than gates and citations. [A21]
- **High-Stakes Personalization**, Sawant, **2026-04-05**, arXiv **2604.04300**: practitioner position paper on InvestMate; behavioral memory, living theses, drift, style–signal conflict and evaluation ambiguity. Uses structured thesis states such as CONFIRMED/UNCHANGED/WEAKENED/BROKEN instead of free-floating conviction. No controlled population-level validation reported in inspected text. Borrow stateful thesis tracking, not an efficacy claim. [A22]
- **BehaviorChain**, *How Far Are LLMs from Being Our Digital Twins?*, Findings ACL **July 2025**: evaluates persona-conditioned behavior chains, rather than conversational roleplay alone. Adjacent methodological evidence: a decision sequence is a harder test than a recognizable persona paragraph. Not an investing-specific or Ackman benchmark. [A24]
- **Twin-2K-500**, arXiv **2505.17479**, **2025-05**: over 2,000 people and >500 questions; disclosed held-out personal responses permit behavioral testing. Inspected text reports GPT-4.1-mini text-persona accuracy 71.72%, versus 70.39% when asking for reasoning: more generated reasoning need not improve matching. Survey answers are not capital-allocation decisions and these figures do not transfer directly. [A25]
- **Personas do not improve objective performance**, arXiv **2311.10054**, **2023-11-16**: 162 roles, four model families, 2,410 factual questions; role prompts do not reliably improve accuracy. This does **not** show all persona conditioning is useless; it undermines the assumption that a famous name supplies missing expertise. [A26]

**Finding:** public implementations of “Buffett-in-a-box” are abundant, but the strongest relevant shift in 2026 is toward **source-grounded procedural benchmarks**, not a proven faithful Ackman digital twin. Do not equate a scraped public explanation with the investor's private complete thought process. Our claim should be “fidelity to the documented public decision record,” not mind-reading. [A1, A20–A26]

## 4. Prompting and implementing Llama 3.1 8B

### 4.1 What is documented versus what we must test

Meta's **2024-07-23** model card lists 8B/70B/405B, **128K context**, GQA and **December 2023 pretraining cutoff**. It separately describes instruction/synthetic post-training data; the pretraining date is **not a certificate that all post-training information predates 2024**. The prompt-format guide specifically warns that **8B-Instruct cannot reliably maintain a conversation alongside tool-calling definitions**; use zero-shot tool calling or remove definitions during normal conversation. Guide fetch was blocked, so the exact warning was verified through indexed official-page text; the model card itself was fetched. [A11, A12]

| Proposed practice | Rationale / evidence | Important qualification |
|---|---|---|
| Short staged calls | Extract dated facts → evaluate gates → decide; isolates tasks and keeps evidence near the question | Project hypothesis; benchmark against one-call baseline, since intermediate summaries can lose qualifications |
| Explicit ordered checklist | “Is this predictable enough?” before price; label satisfied/failed/unknown with IDs | InvestPhilBench supports measuring gate order, not our exact gate content. [A21] |
| Schema-constrained JSON | Ollama accepts JSON schema in `format`; llama.cpp supports constrained grammars/schema conversion | Valid JSON ≠ true or cited claims; host validates semantics. [A13, A15] |
| 2–3 short, diverse exemplars | Demonstrate one buy, one pass, one exit/uncertainty case, all calibration-only | Few-shot gains are task-dependent; avoid copying the answer key into held-out context |
| One company/action-date per call | Avoid old source's cumulative multi-ticker context and accidental cross-company claims | Proposed control based on source audit. [A1] |
| Concise evidence-linked reasons | 3–4 drivers, each mechanism + source; avoid unbounded “think like Ackman” essays | CoT mainly helps math/symbolic tasks in a broad study; not universally harmful or helpful at 8B. [A16] |
| Short curated context | Start 4–8K actual tokens with output headroom; retrieve only applicable principle cards and evidence | 128K advertised support is not 128K reliable use or a Mac memory budget. [A11, A14, A17] |
| Arithmetic outside the model | Deterministic valuation/scenario tables with units/date | Prevents fluent arithmetic and denominator errors; source audit shows why. [A1, A2] |
| Fixed low-temperature runs | Start temperature 0; pin model, quantization, template, seed and backend version | Not a guarantee of bitwise repeatability across devices/builds; measure repeats |

**What fails or needs skepticism:** famous-name-only instructions; requests to invent confrontational tone; unrestricted tools plus multi-turn conversation at 8B; pasting the complete compendium; mixing future outcome passages with contemporaneous evidence; asking for long hidden thought transcripts; treating confidence 90 as a calibrated probability; rewarding verbosity in judging; assuming Q4 and Q8 results are interchangeable. [A1, A11–A17, A26; implementation recommendations]

The 2025 *To CoT or Not to CoT?* study spans 20 datasets and 14 models and finds benefits concentrated in math/symbolic reasoning. It includes Llama 3.1 8B: do not overgeneralize “small models cannot reason” or extrapolate the separate ≤3B long-reasoning-distillation learnability result to every 8B task. Our recommendation is **short auditable rationale**, not suppression of useful reasoning. [A16]

### 4.2 Concrete local setup on a Mac Mini

These are implementation recipes, **not commands executed during this survey**. Apple Silicon/Metal is the intended path; Intel Mac Mini performance is a different case. Unified memory holds weights, KV cache, buffers and the OS. Ollama's listed Llama 3.1 8B Q4_K_M download is about **4.9 GB**; total resident use is higher. A 16GB Apple Silicon machine is a reasonable starting target for short-context Q4; 24/32GB gives more headroom. Actual feasibility depends on context, concurrent apps and backend; no unmeasured tokens/sec claim is warranted. [A14, A15]

**Ollama route** (official macOS app or documented installer; avoid unreviewed third-party scripts):

```sh
ollama pull llama3.1:8b-instruct-q4_K_M
ollama show llama3.1:8b-instruct-q4_K_M
ollama run llama3.1:8b-instruct-q4_K_M
```

For batch replay, call local `http://localhost:11434/api/chat` with `stream:false`, the pinned model name/digest, system/user messages, `format:<JSON schema>`, and `options:{"temperature":0,"seed":42,"num_ctx":8192,"num_predict":1200}`. Specify context explicitly; defaults are version/hardware dependent. Read response token/timing counters and record errors. Schema example: require `action`, `as_of`, `drivers`, `failed_gates`, `unknowns`, `kill_criteria`; each driver requires `claim`, `evidence_ids`, `mechanism`. Keep trusted system rules separate from untrusted retrieved documents. [A13, A14]

**llama.cpp route:** install/build a pinned official release with Metal enabled; obtain a licensed Llama-3.1-8B-Instruct GGUF, record its source and SHA-256; use the model's chat template. Example server command after installation:

```sh
llama-server -m /absolute/path/to/pinned-model.gguf -c 8192 -ngl 99 --port 8080
```

The absolute path is a local setup parameter, not an asset supplied here. Use the OpenAI-compatible chat endpoint, template-aware messages, and the build's documented `response_format`/JSON-schema support; unsupported JSON-schema features must be rejected rather than assumed enforced. llama.cpp's grammar documentation distinguishes syntactic constraints from prompt-level semantic requirements. Keep context + generation within the allocated window. [A15]

**Quantization experiment:** compare Q4_K_M with Q8_0 on the identical calibration pack, judging driver recall, false claims, refusals, JSON validity and gate consistency—not only speed. Choose once before sealing. KV-cache quantization is separate from weight quantization; memory savings can change behavior. A community Apple Silicon benchmark thread is useful for hardware planning but not a controlled quality study; report measured local latency and memory rather than its headline throughput. [A14, A15]

## 5. Practitioner process codification and decision journals

Mauboussin's *More Than You Know* stresses distinguishing process from outcome and identifying the gap between price and business value; his discussion of variant perception requires a **well-founded difference from market consensus**, not merely liking a good company. The CFA Institute's 2015 discussion likewise separates fundamental knowledge from what the market already expects. Decision-journal practice records what one believed **before** the outcome so memory cannot rewrite the thesis; Annie Duke's kill-criteria advice turns vague persistence into precommitted reevaluation conditions. These are general investor-process tools, **not automatically Ackman's stated rules**. [A18, A19, A27, A28]

**Recommended thesis-card fields** (project proposal informed by those practices):

| Field | What must be written before decision |
|---|---|
| Identity and time | Decision timestamp; portfolio state; source publication/access dates; eligible information cutoff |
| Mandate/gates | In/out of competence; predictability; financing/extrinsic risks; explicit pass reason if failed |
| Business quality | Demand/competitive mechanism; cash economics; reinvestment; management incentives; what is and is not knowable |
| Variant perception | Consensus assumption; our different assumption; evidence; why price may not reflect it |
| Drivers | 3–4 load-bearing mechanisms with evidence IDs and magnitude/direction |
| Valuation | Bear/base/bull assumptions; value range; downside; required return; concentration/hedge implications |
| Catalyst/action | Passive recognition or specific feasible intervention, authority, costs and milestones; no invented deadline |
| Falsification | Observable kill criteria; what would cause pass, trim, exit or hedge; uncertainty that cannot be resolved |
| Review | Original card immutable; later evidence appended with time; thesis-state transitions and action rationale |

Maintain two memories: **decision-time belief ledger** and **subsequent outcome/review ledger**. Only the former is replay input. Retrospective Ackman commentary can inform an explicitly later principle revision but must never be smuggled into an earlier thesis. Reviewing losses and passes is essential because direction-only evaluations can reward generic bullishness. [A10, A18–A22; design synthesis]

## 6. Source register

All accessed **2026-10-25** unless otherwise specified; live docs may change. Paper results are attributed, not replicated.

- **A1:** virattt, AI Hedge Fund, pinned source **2025-07-28**, three raw URLs in §2.1; repository/README https://github.com/virattt/ai-hedge-fund and https://raw.githubusercontent.com/virattt/ai-hedge-fund/main/README.md ; dated metrics https://api.github.com/repos/virattt/ai-hedge-fund ; path history https://api.github.com/repos/virattt/ai-hedge-fund/commits?path=src/agents/bill_ackman.py&per_page=3 ; current tree https://api.github.com/repos/virattt/ai-hedge-fund/git/trees/main?recursive=1 .
- **A2:** Yejin Kim, Youngbin Lee, Juhyeong Kim, Yongjae Lee, *GuruAgents*, **2025-10-02**: https://arxiv.org/abs/2510.01664 ; full text https://arxiv.org/html/2510.01664v1 .
- **A3:** Yijia Xiao, Edward Sun, Di Luo, Wei Wang, *TradingAgents*, **2024-12-28**, v7 **2025-06-03**: https://arxiv.org/abs/2412.20138 ; https://arxiv.org/html/2412.20138v7 ; historical comparison https://arxiv.org/html/2412.20138v1 ; code https://github.com/TauricResearch/TradingAgents .
- **A4:** Yu et al., *FinMem*, **2023-11-22**, inspected v2: https://arxiv.org/abs/2311.13743 ; https://arxiv.org/html/2311.13743v2 ; symposium publication **2024-05-20** https://ojs.aaai.org/index.php/AAAI-SS/article/download/31290/33450 .
- **A5:** Zhang et al., *A Multimodal Foundation Agent for Financial Trading*, **2024-02-28**, v3 **2024-06-28**: https://arxiv.org/abs/2402.18485 ; https://arxiv.org/html/2402.18485v3 .
- **A6:** Yu et al., *FINCON*, **2024-07-09**, inspected v2: https://arxiv.org/abs/2407.06567 ; https://arxiv.org/html/2407.06567v2 ; https://github.com/The-FinAI/FinCon .
- **A7:** Yang et al., *FinRobot*, **2024-05-23**, inspected v2: https://arxiv.org/abs/2405.14767 ; https://arxiv.org/html/2405.14767v2 .
- **A8:** Li et al., *InvestorBench*, ACL **July 2025**: https://aclanthology.org/2025.acl-long.126/ ; code https://github.com/felis33/INVESTOR-BENCH . Coverage here is benchmark/task-level; no unchecked result numbers used.
- **A9:** *Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?*, arXiv **2025-05**, inspected v4 dated **2025-11-25**: https://arxiv.org/abs/2505.07078 ; https://cdn.arenafi.org/papers/arxiv/2505.07078v4.pdf . Search-indexed text only for conclusion cited here.
- **A10:** Ackman, Netflix sale investor letter, **2022-04-20**: https://assets.pershingsquareholdings.com/2022/04/20183256/Final-Letter-4.20.2022.pdf ; original purchase rationale **2022-01-26** https://assets.pershingsquareholdings.com/2022/01/26170421/Pershing-Square-Capital-Management-L.P.-Releases-Letter-to-Investors-01-26-2022.pdf .
- **A11:** Meta, Llama 3.1 8B-Instruct model card, release **2024-07-23**: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct .
- **A12:** Meta, Llama 3.1 model/prompt-format guide, live undated documentation accessed **2026-10-25**: https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1 ; indexed official mirror https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_1 . Full fetch blocked; warning verified from official indexed text.
- **A13:** Ollama, structured outputs, live docs accessed **2026-10-25**: https://docs.ollama.com/capabilities/structured-outputs ; API https://docs.ollama.com/api/chat .
- **A14:** Ollama model listing, live **2026-10-25**: https://ollama.com/library/llama3.1:8b ; explicit quant https://www.ollama.com/library/llama3.1:8b-instruct-q4_K_M ; context docs https://docs.ollama.com/context-length .
- **A15:** llama.cpp official project and grammar/server documentation, live **2026-10-25**: https://github.com/ggml-org/llama.cpp ; https://github.com/ggml-org/llama.cpp/tree/master/examples/server ; https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md ; community hardware reports (not controlled) https://github.com/ggml-org/llama.cpp/discussions/4167 .
- **A16:** *To CoT or Not to CoT? Chain-of-thought Helps Mainly on Math and Symbolic Reasoning*, arXiv **2024-09**, ICLR **2025**: https://arxiv.org/abs/2409.12183 ; https://arxiv.org/html/2409.12183v1 . Distinguish *Small Models Struggle to Learn from Strong Reasoners*, ACL Findings **July 2025**: https://aclanthology.org/2025.findings-acl.1301/ .
- **A17:** Liu et al., *Lost in the Middle*, **2023-07-06**, TACL **2024**: https://arxiv.org/abs/2307.03172 . General long-context evidence, not a direct Llama 3.1 8B finance experiment.
- **A18:** Michael Mauboussin, *More Than You Know* excerpt, indexed **2009-08-25**: https://www.michaelmauboussin.com/assets/excerpt-more-than-you-know.pdf .
- **A19:** CFA Institute, *The Five Dimensions of Variant Perception*, **2015-11-27**: https://rpc.cfainstitute.org/blogs/enterprising-investor/2015/the-five-dimensions-of-variant-perception .
- **A20:** Jiang et al., *Evaluating Investment Logic in Large Language Models: A Real-World Benchmark Towards Personalzied Financial Agents*, **2026-08-06**: https://arxiv.org/abs/2608.06108v1 ; https://arxiv.org/html/2608.06108v1 .
- **A21:** Chen & Qu, *InvestPhilBench*, **2026-06-24**: https://arxiv.org/abs/2606.25984 ; https://arxiv.org/html/2606.25984v1 .
- **A22:** Yash Ganpat Sawant, *High-Stakes Personalization*, **2026-04-05**: https://arxiv.org/abs/2604.04300v1 ; https://arxiv.org/html/2604.04300v1 .
- **A23:** Community reproduction, live accessed **2026-10-25**, not original paper: https://github.com/Kantamaniprakash/trading-agents-lab . Search-indexed cost statement only; configuration-specific, not independently validated.
- **A24:** *How Far Are LLMs from Being Our Digital Twins?*, Findings ACL **July 2025**: https://aclanthology.org/2025.findings-acl.813/ .
- **A25:** *Twin-2K-500*, **May 2025**: https://arxiv.org/abs/2505.17479 ; https://arxiv.org/html/2505.17479v1 .
- **A26:** *When “A Helpful Assistant” Is Not Really Helpful*, **2023-11-16**: https://arxiv.org/abs/2311.10054 .
- **A27:** Farnam Street, Mauboussin on decision journals/checklists, undated live page accessed **2026-10-25**: https://fs.blog/how-to-improve-the-quality-of-our-decision-making ; decision journal https://fs.blog/decision-journal/ . Secondary practitioner interview/explanation.
- **A28:** PCMA interview with Annie Duke, **2023-05-09**: https://www.pcma.org/annie-duke-quit-book-goals-should-come-with-warning . Practitioner kill-criteria guidance, not investing-specific empirical proof.

## 7. Prioritized design recommendations for the Ackman agent

Ordered implementation backlog; each item includes recommendation, reason and source. These are proposed decisions pending calibration.

| Priority | Recommendation | Why | Source |
|---:|---|---|---|
| 1 | Define fidelity as documented action **and** driver agreement; freeze rubric before tuning | Prevents optimizing a generic profitable/value-investing bot | A2, A20, A21 |
| 2 | Separate answer-key/outcome archive from inference packs physically and by access permissions | The best prose is worthless if the true trade leaked | A10; companion evaluation survey E1–E5 |
| 3 | Build dated principle cards with source passages and explicit exceptions | A timeless “be Ackman” prompt hides process change | A10, A21 |
| 4 | Implement predictability/competence/downside gates before valuation | Cheap is not enough for a concentrated portfolio | A10, A21 |
| 5 | Require 3–4 driver objects with mechanism, evidence IDs and uncertainty | Turns generic slogans into auditable causal overlap | A20, A21 |
| 6 | Add explicit PASS, UNKNOWN and operational ABSTAIN states | Neutral, sell, short and failed inference are different | A1 |
| 7 | Use deterministic tools for financial arithmetic with units, period and filing date | Avoids denominator mistakes and accidental future accounting | A1, A2 |
| 8 | Implement a real catalyst/activism feasibility checklist | Low margins alone do not specify an activist opportunity | A1; §2.5 audit |
| 9 | Separate security thesis from portfolio sizing/concentration decision | Same asset can be attractive yet unsuitable for the portfolio | A10 |
| 10 | Separate macro hedges/shorts/control situations from standard equity DCF | Payoff, carry, catalysts and legal powers differ | A1; §2.5 audit |
| 11 | Persist original thesis and falsifiers; append dated revisions without rewriting history | Enables exits, reversals and honest postmortems | A18, A22, A27, A28 |
| 12 | Represent economic moat with specific business evidence, not ROE alone | Leverage/buybacks can flatter ROE without durability | A1, A10; source-to-objective critique |
| 13 | Start with staged extraction → gates → short decision and one bear challenge | Keeps 8B tasks bounded without costly debate theater | A3, A12, A16 |
| 14 | Use one company/decision per call, with only relevant dated evidence | Prevents cumulative ticker contamination and context bloat | A1, A17 |
| 15 | Enforce JSON schema and semantic citation/date validation outside the model | Syntax constraints cannot establish truth | A13, A15, A20 |
| 16 | Include calibration-only examples of a buy, a disciplined pass and an exit | Counteracts “famous investor means buy quality” stereotype | A10, A26 |
| 17 | Pin exact model weights, quantization, template, backend and prompt hashes | Model-family names and mutable tags are not reproducibility | A1, A11, A14, A15 |
| 18 | Audit pretraining **and** post-training temporal provenance | December 2023 pretraining is not universal non-leakage proof | A11; companion E3–E5 |
| 19 | Compare Q4/Q8 and short/long contexts on fidelity before sealing | Resource settings can change behavior; speed is not sufficient | A14–A17 |
| 20 | Make a failed inference visibly failed; prohibit silent neutral defaults | Operational faults otherwise inflate apparent discipline | A1 |
| 21 | Use human-calibrated judges with driver-by-driver quoted evidence | Plausibility and verbosity can masquerade as grounding | A20, A21; companion E6–E9 |
| 22 | Report passes, losses, exits and counterfactual stress cases, not only famous winners | A useful persona has boundaries and can change its mind | A10, A18, A22 |
| 23 | Budget and log calls/tokens/latency per decision; add debate only if paired calibration helps | Original TradingAgents offers no verified universal cost per decision | A3, A23 |
| 24 | Freeze all design choices before a separately operated sealed test | Prevents repeated “hold-out” inspection becoming training | Companion evaluation protocol |
