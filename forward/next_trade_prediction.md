# Forward prediction — what Third Point discloses in the next 60-90 days (as of 25 Oct 2026)

Produced by the frozen v1.5 chain with the era-E addendum (`prompts/era_e_update_for_forward_runs.md`) on the frozen forward
pack `forward/pack/F01-F06` (latest 13F and September exposures, 2026 letters and X posts, a 37-name candidate library with
prices and peer gaps, the activism and deal landscape with nomination windows, market regime, the credit book). Prompt:
`prompts/12_forward_next_trade.md`. The chain was run four times with coverage instructions (overview; existing portfolio;
the E1 activist lane; the E2-E7 event, credit and inflection lanes); the tables below merge those runs and the last section
is the principal's reconciliation. Raw JSON: `forward/next_trade_prediction.json`. **Nothing here is investment advice; it is
a test of the agent, to be scored against 13F/13D filings, letters and posts after 25 January 2027.**

## Regime
Runs: run1 = REDUCE_GROSS, run2 = NO_CHANGE, run3 = NO_CHANGE, run4 = NO_CHANGE. Expected new positions in 90 days (chain estimates):
run1 1.5, run2 1.5, run3 1, run4 2. Three of four runs say **NO_CHANGE** to gross; the overview run
says REDUCE_GROSS on the valuation and crowding observations in F05 (index multiples, AI/Korea momentum, dealer depth). Read
together: a book that keeps its gross roughly flat, adds one or two event names and trims momentum winners rather than hedging.

## Most likely single disclosed action
**A new position in post-separation Honeywell** (NEW_BUY, p = 0.65 in the event/inflection run, 0.5 in the existing-portfolio
run; E2/E4; 3% of NAV; 9x trailing EV/EBITDA on optical pro-forma accounts that the chain wants rebuilt [F03]). Second: **an E1
engagement at 3M** around the 25 Nov - 25 Dec nomination window (p 0.2-0.45 across three runs). The chain's overview run put
Solstice Advanced Materials first (p 0.6); the principal's reconciliation below lowers it.

## Ranked candidates — purchases, additions and deals (merged over the four runs; p = highest run)
| # | Company | Action | p(90d) | per run | Template | Instrument / size | Valuation [F03] | Trigger |
|---|---|---|---|---|---|---|---|---|
| 1 | Honeywell | NEW_BUY | 0.65 | run2:0.5, run4:0.65 | E4 | Common Equity 3% | Skew > 2:1; rebuild pro-forma earnings to avoid 9x optical traps; trading at 9.00x EV/EBITDA [F03] | Post-separation earnings reality check following June aerospace spin; focus on automation and portfolio simpli |
| 2 | Solstice Advanced Materials | NEW_BUY | 0.6 | run1:0.6, run3:0.5 | E1 | Common Equity 3% | 120bp margin gap vs Eaton peer [F03]; 3:1 skew to SOTP intrinsic value. | Starboard activist agenda [E2] provides platform for SOTP value capture in refrigerants/nuclear; nomination wi |
| 3 | FedEx | NEW_BUY | 0.45 | run1:0.45 | E2 | Common Equity 4% | 132bp operating margin gap vs UPS [F03]; 2.5:1 skew. | Residual parcel company post-freight spin [E4] showing operational margin gap; upcoming earnings review [F03]. |
| 4 | 3M | NEW_BUY | 0.45 | run1:0.35, run3:0.2, run4:0.45 | E1 | Common Equity 2% | Skew 2.5:1; target valuation based on successful Solventum-like simplification and margin-gap closur | Upcoming ordinary nomination window Nov 25–Dec 25, 2026 [F04] |
| 5 | Telephone & Data Systems | ADD | 0.4 | run1:0.4 | E2 | Common Equity 2% | SOTP discount vs peers; opportunistic entry. | Ongoing SOTP value unlocking; spectrum sale completed, tower/fiber remains [E7]. |
| 6 | Flex | ADD | 0.3 | run1:0.3 | E2 | Common Equity 3% | Mix transition potential; 2:1 skew. | Innovation Day Nov 10; Q1 2027 spin-off catalyst [F04]. |
| 7 | Bausch Health | NEW_BUY | 0.25 | run1:0.25 | E3 | Corporate Bonds 2% | Pricing discount to recovery value; 3:1 skew. | Complex capital structure following divestitures [F06]. |
| 8 | Unum | TRIM | 0.2 | run1:0.2 | E4 | Common Equity -1% | Margin parity; target price hit. | Strong performance, valuation target reached [F02]. |
| 9 | Norfolk Southern | TRIM | 0.2 | run1:0.2 | E2 | Common Equity -2% | 722bp margin gap; downside risk increases with STB delay. | Merger spread compression; STB uncertainty [F04]. |

Thesis paragraphs (chain output, letter voice):
- **Honeywell (NEW_BUY)** — Following the June aerospace separation, Honeywell is an classic E4 earnings-inflection candidate. We are looking past the messy post-spin financials to focus on core margin expansion within the automation and portfolio-focused segments. Unlike the optical 9x EV/EBITDA multiple suggests, our sum-of-the-parts valuation reveals hidden asset power if the board commits to further simplification [F03, F04]. *Confirmed by:* 13F disclosure or private engagement reports surfaced in Q1 2027 filings.
- **Solstice Advanced Materials (NEW_BUY)** — Solstice represents a textbook event-driven setup where a focused activist has identified substantial margin and portfolio optimization potential [F04]. With a pending nomination window and a clear path to rationalizing the refrigerant and nuclear asset mix, the company presents an asymmetric opportunity to address the historical discount and margin gap versus industrial peers [F03]. We will initiate as a core constructivist position, leveraging our experience in spin-offs and asset-heavy industrial turnarounds to force the board's hand. *Confirmed by:* 13D filing or public letter regarding board nominees.
- **FedEx (NEW_BUY)** — Following the freight spin-off, FedEx is now a simplified, pure-play parcel business with significant latent earnings power [F03]. The current valuation fails to credit the company for the potential margin convergence with UPS, which remains obscured by legacy freight complexity and cost structures [F03]. We see a clear catalyst in the upcoming earnings calls where a renewed commitment to asset productivity and disciplined capital allocation should catalyze a re-rating toward peer multiples. *Confirmed by:* 13F disclosure or private engagement dialogue reported in industry notes.
- **3M (NEW_BUY)** — 3M remains a conglomerate with a lazy balance sheet post-Solventum. With the ordinary nomination window opening in late November, there is a clear governance route to demand further operating execution or asset separation [F04]. We see a significant margin gap versus industrial peers and will evaluate the candidate's commitment to unlocking value through rigorous capital allocation [F03]. *Confirmed by:* 13D filing or public letter regarding board nominees.
- **Telephone & Data Systems (ADD)** — TDS remains a compelling SOTP situation where the market continues to undervalue the individual components of the tower, spectrum, and fiber assets [F03]. Following the successful Verizon spectrum sale, management must now focus on further value realization through fiber or tower separation. We are adding to our conviction as the thesis approaches an inflection point, with potential for further capital upstreaming or divestment announcements. *Confirmed by:* 8-K announcement of further asset sale or separation process.
- **Flex (ADD)** — Flex's planned spin-off of its cloud and power infrastructure business is a high-conviction catalyst that remains misunderstood by the market [F04]. The recent acquisition of EPC Power further validates the strategic pivot [F04]. As we approach the Innovation Day, we are adding to our position to capture the valuation unlock of the infrastructure-focused entity, which should command a significantly higher multiple than the legacy EMS operations. *Confirmed by:* Innovation Day presentations or filing of registration statements.
- **Bausch Health (NEW_BUY)** — Bausch Health presents a classic distressed-credit opportunity where the complexity of the capital stack provides a mispricing versus the underlying asset recovery value. We are underwriting the debt with a focus on BLCO stake leakage and litigation resolution [F06]. Our position is sized to conviction, as we expect the company to address maturity walls through restructuring or refinancing, creating a path to 20-30% IRR as the debt recovers toward par. *Confirmed by:* Refinancing announcement or debt exchange offer.
- **Unum (TRIM)** — Unum has performed in line with our expectations as a quality earnings inflection compounder, but the current valuation now reflects much of the upside [F03]. Following the dividend record date and strong quarterly results, we are trimming to lock in gains and rotate capital into higher-conviction event-driven opportunities [F03]. *Confirmed by:* 13F showing reduced position size.
- **Norfolk Southern (TRIM)** — The Norfolk Southern/Union Pacific merger spread has tightened while uncertainty regarding STB approval remains elevated [F04]. Given the current regulatory regime and the slow progress of the merger application, the risk/reward skew has deteriorated [F04]. We are trimming our position to reduce exposure to this specific arb-dependent event while maintaining a smaller core until clearer regulatory signals emerge. *Confirmed by:* 13F reduction or exit announcement.

## Names the chain passes (and why)
| Company | Template | Trigger considered | Valuation | run |
|---|---|---|---|---|
| PepsiCo | E1 | N/A | N/A | run3 |
| Lululemon | E1 | N/A | N/A | run3 |
| Phillips 66 | E1 | N/A | N/A | run3 |
| CoStar | E1 | N/A | N/A | run3 |
| Honeywell | E1 | N/A | N/A | run3 |
| Kraft Heinz | E1 | N/A | N/A | run3 |
| Live Nation | E1 | N/A | N/A | run3 |
| FedEx | E1 | N/A | N/A | run3 |
| Solstice Advanced Materials | E1 | Activist entry by Starboard [F04] | 12.46x EV/EBITDA; margin gap 120bp [F03] | run4 |
| FedEx Freight | E4 | Post-spin standalone economics [F03] | 22.82x EV/EBITDA; gap to peer ODFL is 1,928bp [F03] | run4 |
| Kraft Heinz | E5 | Potential spin restart [F03] | 8.32x EV/EBITDA [F03] | run4 |
| Live Nation | E4 | Cash generation review [F03] | 27.48x EV/EBITDA; high short interest [F03] | run4 |
| Hut 8 | E4 | Infrastructure monetization [F03] | Negative earnings; 18.46% SI [F03] | run4 |
| Wolfspeed | E2 | Post-reorg utilization [F03] | N/M multiples [F03] | run4 |

## Existing positions
| Company | Action | p(90d) | Reason class | Why | run |
|---|---|---|---|---|---|
| Meta | HOLD | 0.5 | L4 | High conviction earnings inflection; holding as core AI compounder [F01, F02]. | run1 |
| Nvidia | HOLD | 0.5 | L4 | Core long in AI infrastructure; awaiting November earnings to validate product cycle [F01, F03]. | run1 |
| CoStar | SELL | 0 | L1 | Thesis break exit completed in April [F02]. | run1 |
| WBD | SELL | 0 | L3 | Deal closed Oct 6; exit complete [F01, F04]. | run1 |
| CRH | HOLD | 0.4 | L4 | Synergy realization from Arcosa integration supports core position [F02, F03]. | run1 |
| Meta | ADD | 0.4 | L4 | Renewed gross long presence in September report suggests high conviction in AI-driven efficiency and ad-spend recovery; requires monitoring of capex v | run2 |
| Nvidia | HOLD | 0.3 | L4 | Top-tier long position as of September; wait for November earnings to validate compute product cycle strength against elevated crowding and supply-sid | run2 |
| Union Pacific | TRIM | 0.3 | L3 | STB process on NSC merger remains in flux; wait for outcome clarity while exposure is significant [F04]. | run2 |
| Bausch Health | HOLD | 0.2 | L1 | Core credit position; remain held pending specific waterfall analysis of legal/litigation priority versus capital structure complexity [F06]. | run2 |
| Meta | HOLD | 0.8 | L1 | Renewed gross long status in September report; conviction remains high on efficiency and AI monetization despite capex spending [F01, F03]. | run4 |
| Nvidia | TRIM | 0.5 | L2 | Scaling back exposure as the AI/Korea momentum unwinds and crowding impacts liquidity [F01, F02]. | run4 |

## Principal's reconciliation (how this will be scored)
1. **Solstice (SOLS)** is Starboard's campaign (F04). Under the frozen v1.5 discipline test "someone else's fight" — Third Point
   leads or stays out — a Third Point 13D on Solstice in the window is unlikely; the overview and activist runs ranked it first
   because the forward prompt does not re-run Gate 1 in full. Scored at **p = 0.15** (a passive position after a Starboard
   settlement is the only plausible route), not 0.6.
2. **Honeywell** is the consensus of the two lanes that looked at it as an E2/E4 (post-aerospace-separation automation stub);
   the activist lane passed it as an E1 because the simplification is already done — consistent with Third Point's 2017
   engagement having been completed. Scored as the **top prediction, p = 0.5**, instrument common equity, size 2-4% NAV,
   confirmation = Q4 2026 13F (mid-February 2027) or a letter mention.
3. **3M**: an E1 candidate with a real window, but the chain's own valuation (15x forward EV/EBITDA, 17 bp margin gap vs Eaton)
   does not give the 2-3:1 skew the process requires; p = **0.25**, more likely a quiet position than a public engagement.
4. **FedEx**: the overview run bought the residual parcel company (E2, p 0.45) and the activist run passed it; the
   post-Freight-spin set-up is a 2027 event (spin dated Q2 2027 in F04), so p = **0.25** for a disclosed position by late January.
5. **Existing book**: Meta HOLD/ADD and Nvidia HOLD/TRIM split across runs; Union Pacific / Norfolk Southern trims around the
   STB process (p 0.2-0.3); Unum trim on valuation (p 0.2). Expected: **one trim among Nvidia/Unum/UNP disclosed in the Q4 13F,
   p = 0.6 for at least one**.
6. Expected disclosed count: **1-2 new reportable names and 1-2 trims**; a public E1 campaign (letter or 13D) in the window:
   **p = 0.25**.

Scoring rule for the test: a prediction counts if the action is disclosed (13F/13D, letter, X post by Loeb, press confirmed by a
filing) by 25 January 2027 for actions, and by the Q4 2026 13F (mid-February 2027) for reportable positions. The hold-out
scoreboard pattern (5/5 buys, 0/5 sells) applies here too: the buy side of this forecast is the better-calibrated half.
