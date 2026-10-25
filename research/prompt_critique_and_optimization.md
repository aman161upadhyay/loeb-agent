# Critique and optimisation of the project instructions — Loeb edition (for Aman)

The brief is "run the exact same loop as for Ackman, for Dan Loeb". Loeb is the closest of the three investors to
Ackman in form (hedge fund, activism, public letters) and the furthest in substance (multi-strategy, across the capital
structure, hundreds of positions, a portfolio that is hedged and traded). The loop transfers; the unit of decision and
the grading do not transfer unchanged. This document says what changed and why. Read with
`../ackman-agent/research/prompt_critique_and_optimization.md` for the shared machinery.

## 1. What "the same loop" means for Loeb, and what I changed

| Your instruction | What transfers from Ackman | What had to change for Loeb, and why |
|---|---|---|
| "All of his trades" | Dossiers with dates, size, thesis, own words, outcome, sources (`compendium/`, 1995-2026; 54 quarters of 13F rows, 676 distinct instruments in `all_positions_index.md`). | **Third Point holds 40-120 reported equity lines a quarter plus credit, structured, private and short books that never appear in a 13F.** Most lines have no stated rationale. The compendium therefore has two classes — annotated decisions (letter, 13D, X post or interview explains it) and disclosure-only records — and only the first is scorable. The Loeb record also has a documented *hidden* half (credit, shorts, hedges) that the agent is told about in `D08_fund_context` but that cannot be graded line by line. Honest coverage: every annotated decision, every 13F line indexed, credit/shorts at the letter level. |
| "Since the start of his career" | Era switch. | Three eras (small-cap letters 1995-2008; credit cycle and large-cap constructivism 2009-15; constructivism at scale, quality and hedging 2016-25) plus the sealed Era E. The behavioural change is larger than Ackman's: the 2005 Star Gas letter and the 2017 Nestlé letter are different instruments used by the same man. The agent's Gate 3 (plan and role, P0-P5) makes the era explicit; a public-ridicule 13D in 2019 is a defect, a polite private approach in 2005 is also a defect. |
| "Judge trade by trade with pre-trade data" | Pack → chain → grade → revise; masking; controls; sealed hold-outs. | **Three Loeb-specific grading problems.** (1) *Instrument matters*: Delphi was DIP paper and post-reorg equity; Nestlé included options; Fannie/Freddie were preferreds; Capital One/Discover was an arb pair. A BUY in the wrong instrument is PARTIAL. Every key and output carries `instrument`. (2) *Portfolio-level decisions* (cut gross in 2008, Q1 2020, 2022; the energy-short book in 2016) are among his most important and are not single-name trades; the `hedge` mode here is a *portfolio regime* decision (ADD_RISK/REDUCE_GROSS/HEDGE/NO_CHANGE), graded against the letter's exposure table. (3) *Short/long asymmetry*: he rarely names shorts; keys for shorts exist only where he did (Herbalife-adjacent, energy 2015, growth 2022) and are flagged as lower-confidence. |
| "Predict his next trade in the next two months" | Ranked, conditional watchlist; Brier-scored against the Q3-2026 13F (16 Nov) and Q4-2026 letter. | Third Point turns over more of the book than Pershing, so the base rate of "a new top-10 position within two months" is high and uninformative. The forward deliverable is split: (a) new *engagements* (13D/letter/public campaign) — rare, informative, scored on filings; (b) new top-10 equity positions — a ranked list with probabilities; (c) the regime call — gross/net and the AI-book share, scored on the Q4-2025/Q1-2026 letters' exposure tables. Name-the-one-trade is not attempted. |
| "Use X posts, Reddit, forums" | Forums as inputs to packs (the bear case). | X is primary for Loeb from 2020 (@DanielSLoeb1 explains positions, markets and politics there before letters, and deletes some); the archive authenticates each post. Reddit/VIC rarely contain his reasoning but do contain the *crowd's* view that he trades against (Herbalife 2013, meme stocks 2021), which belongs in `D05_market_worries`. |
| "A series of prompts and an AGENT.md" | Staged chain, JSON contracts, grader, leakage check, runner. | Added: situation types E1-E7 (event taxonomy before quality), Gate 3 roles P0-P5, sell rules L1-L5 + ESCALATE, portfolio decisions; `instrument` and `plan` in the schema; the quarterly-letter voice in the memo; and the lesson table (2008, Herbalife, Sony I, energy, Nestlé, Campbell, Q1 2020, Intel, growth/SPACs, Disney II, TPIL) as dated rule changes. |
| Rubric | Unchanged. | Direction MATCH requires the same decision *and* a compatible instrument; the ≥75%-of-drivers state rule and the grounding share are computed in code (`tools/grade.py`) after the Ackman adversarial review showed the LLM grader drifting. ESCALATE vs HOLD is graded as direction, because the public step is the decision in a constructivist process. |

## 2. The three failure modes this agent is most exposed to

1. **Activist caricature.** A model that has read about Loeb writes a poison-pen letter in every memo. In the 2016-25
   record the public letter is the exception; most engagements are private, most outcomes are settlements, and many of the
   largest positions (Danaher, Microsoft, Nvidia, Vistra) involved no activism at all. The controls include quality
   compounders where the "right" answer is a quiet BUY (E4) and governance messes where he passed because there was no
   route. The Gate 3 role field exists so that this failure is visible in the scoreboard, not hidden inside a BUY.
2. **Event-blindness.** The opposite failure: the model buys "cheap and good" with no event, which is Buffett's process, not
   Loeb's. Gate 1 hard-fails when no event or inflection can be named; the code enforces the hard fail regardless of what
   the memo step wants to say.
3. **Hidden-book leakage.** Credit, shorts and hedges are not in the 13F, so a pack built from 13Fs understates what Third
   Point was doing (e.g. Q2 2009 looked like a small equity book while the credit book was the fund). D08 carries the
   letter's exposure table for the quarter before as_of; keys for portfolio-level packs are built from letters, not 13Fs.
   Where neither exists the pack says "not in pack" and the key is marked C-quality.

## 3. What is novel here (lean into it)

- **The constructivist arc** (letters → settlements → quiet exits) is the clearest documented example of an investor
  changing *method* while keeping *philosophy*. A spec with a date switch that reproduces both ends is a result about
  activism as a tool rather than an identity — directly comparable to the Ackman repository's 2018 "quiet activism" turn.
- **Cross-capital-structure decisions** (Delphi, Chrysler Finco, Greece, PG&E, Fannie/Freddie) test whether an LLM agent
  can choose the *instrument*, which neither the Ackman nor the Buffett loop exercises.
- **Portfolio-regime decisions** are gradeable from letters; Loeb is the only one of the three who publishes gross/net
  exposure, so the hedge-mode result is a real measurement rather than a guess.

## 4. The optimised one-page brief (use this with any model or person)

> Build an agent that decides as Dan Loeb/Third Point decided, era by era (1995-2008 small-cap letters; 2009-15 credit
> cycle and large-cap constructivism; 2016-25 constructivism at scale, quality and hedging), from point-in-time packs only.
> Classify the event first (E1-E7), value it the way the letters do (sum-of-the-parts, post-event earnings, recovery, arb,
> inflection), choose the role (P0-P5) and the instrument, size it, and state the kill criteria. Grade against Third Point's
> annotated decisions — those with a dated, stated rationale — on direction (including instrument and role), reasons,
> discipline and grounding; index everything else. Seal decisions disclosed after 1 August 2025; freeze the prompts before
> opening the seal; replay masked on a pre-dated model with controls. For the forward test, predict new engagements, new
> top-10 positions and the regime call with probabilities, pre-registered against the Q3-2026 13F and the next two letters.
> Report misses first.

## 5. Things I deliberately did not do

- No single "Loeb number" (one hit rate across eras and strategies). The scoreboard reports by era, by mode and by
  situation type because a blended rate would hide that credit and arb are easier to reproduce than activism timing.
- No reconstruction of undisclosed shorts or private marks from secondary gossip. If Third Point did not say it, the key
  does not claim it.
- No composite activist. Loeb's role choices are graded against *his* record, not against what Ackman or Icahn would have
  done in the same seat; the comparison lives in `investor_profiles/loeb_vs_peers.md`.
- No fine-tuning; no returns in the grader; no invented discount rate (same as the sibling repositories).

## 6. Timeline fit (your deck: v1 by 28 Oct, blind test to 11 Nov, basket to 25 Nov, final 2 Dec)

- v1 (28 Oct): this repository as pushed.
- Blind test (to 11 Nov): `tools/run_agent.py --mask` across the hold-out set with Llama 3.1 8B after `tools/canary.py`.
- Basket (to 25 Nov): the Q3-2026 13F (16 Nov) scores the forward list; the Q4-2025 letter (if public) scores the regime call.
- Final (2 Dec): scoreboard by era/mode/type, the divergence table, the adversarial report; headline = masked pre-dated result.


## Postscript after the calibration loop (2026-10-25)
What the loop found that the design did not anticipate:
1. **An event-driven Gate 1 needs an explicit business-quality brake.** Making Gate 1 ask "what is the event and what is our
   edge" (right for Loeb) and scoring it by situation type (needed for Era A/B activism and for credit) removed the implicit
   quality test that a Buffett-style Filter 1 provides. The first control run returned BUY on six of ten never-held names.
   The fix was six discipline tests written from Third Point's own record (melting ice cube, someone else's fight, unknowable
   liabilities, leverage on a shrinking base, the adjusted-earnings roll-up, the multi-year turnaround), applied before the
   hard-fail test. Lesson for the next loop: write the controls' discipline tests into the first prompt version, from the
   compendium's "never held" names, before the first calibration run.
2. **Rule boundaries become the new misses.** After v1.5 the remaining calibration misses sit on the boundaries of the new
   rules (Massey 2005 and Campbell 2018 read as melting ice cubes despite the asset / named-buyer exception; CoStar 2025 read
   as someone else's fight although Loeb ran his own slate). That is the expected cost of a rule-based brake and is reported,
   not tuned away.
3. **The hard-fail flag must be computed, not asked for.** The model set hard_fail = false on a FAILed floor; the harness
   now recomputes it from the criteria.
4. **Sells need the portfolio.** 5/5 hold-out buys and 0/5 hold-out sells: Third Point's exits are comparative (a better use
   of capital, a widened distribution, a lost argument), and a one-company pack does not contain the comparison. The
   existing-position prompt should take the book's current top positions and the candidate pipeline as inputs (v1.6 plan).
5. **Control packs can be wrong in the direction of the key.** Two control packs omitted the public facts that kept Third
   Point out (another activist already seated; an unbounded liability). A control is only a test of discipline if the pack
   contains what a diligent analyst would have known.
