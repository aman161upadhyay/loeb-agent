STEP 7 — DECISION AND MEMO. AS_OF_DATE: {{as_of_date}}. Company: {{company}} ({{ticker}}).

Decision logic (apply in order; this step may NOT overturn an upstream hard fail). In mode "new" the decision is BUY, SHORT or
PASS (never HOLD); in mode "existing" use the S-prompt; in mode "hedge" use the portfolio prompt.
- gate1.hard_fail = true → PASS, whatever Gates 2-5 said
- gate2.edge_verdict = NO_EDGE → PASS
- valuation_verdict NEGATIVE or THIN → PASS (THIN may be BUY only for arb/credit with a short timetable and a hard floor)
- valuation COMPELLING or ADEQUATE with a plan P0-P5 and a floor → BUY (or SHORT for E7); size from Gate 5; conviction high only
  if the skew ≥ 3:1, the route is open and the floor is hard
- a thesis that depends on an unproven management executing a multi-year roadmap → BUY only as a trade (≤ 3% NAV) or PASS

Then write the memo exactly as a Third Point quarterly letter would introduce the position: 4-8 short paragraphs, first-person
plural, every factual sentence cited [Dnn] — every paragraph carries at least two citations and every sentence with a number
carries one. Paragraph order: (1) what the company is and the one-sentence mispricing; (2) the sum-of-the-parts or post-event
earnings math with the peer benchmark; (3) why the market has it wrong and what changes; (4) the plan — asks, actors, route,
timetable — and our role; (5) risks, floor and what would change our mind; (6) decision, instrument and sizing. No hedging
language, no "it depends".

Return JSON only, matching this schema:
{"as_of_date": "...", "company": "...", "ticker": "...", "decision": "BUY|SHORT|PASS",
 "conviction": "low|medium|high", "target_size_pct_nav": 0, "instrument": "common|options|convert|bond|loan|CDS|SPAC|private",
 "opportunity_template": ["E1"], "catalyst_role": "copy plan_role from Gate 4 (P0-P5)", "gate1_hard_fail": false,
 "valuation": {"method": "...", "target_value": "...", "floor": "...", "skew": "...", "irr_pct": 0},
 "plan": {"asks": ["..."], "actors": ["..."], "governance_route": "...", "timetable_quarters": 0},
 "drivers": [{"driver": "one sentence, the reason as Loeb would state it", "citations": ["D03"]}],
 "kill_criteria": ["..."], "what_would_change_our_mind": "...",
 "memo": "the letter-style memo", "uncited_claims": ["..."]}

Drivers: give 4-5, ordered by importance; these are what the grader compares with Loeb's own stated reasons, so state them
concretely (not "undervalued" but "Alibaba, Yahoo Japan and cash are worth the entire market cap, so the core search and display
business is free"). Third Point letters almost always name the same kinds of reason; cover each when the pack supports it:
(1) the mispricing in one line — the hidden asset, the margin gap or the process the market misprices; (2) the valuation math
with the peer benchmark and the target; (3) the plan and the specific asks (separation, margin target, capital return, board
change) and why management/board can be moved; (4) the catalyst and timetable; (5) the floor and the skew.

Sizing (target_size_pct_nav = intended full position): core event 5-10%; E4 2-6%; credit 1-5%; arb 1-4%; privates ≤ 1-2%;
shorts 0.5-3%. If you choose a size outside these bands, say why in the memo.

GATE 1: {{gate1}}
GATE 2: {{gate2}}
GATE 3: {{gate3}}
GATE 4: {{gate4}}
GATE 5: {{gate5}}
FACT SHEET: {{fact_sheet}}
