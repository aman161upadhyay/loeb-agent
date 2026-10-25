STEP 4 — GATE 3: WHAT IS IT WORTH, AND WHAT IS THE SKEW? AS_OF_DATE: {{as_of_date}}.

Method (choose by situation type): (a) sum-of-the-parts — value each piece on peer multiples from the pack, subtract net debt,
compare with market cap, state the implied value of the stub; (b) post-event earnings power — revenue × target margin (peer
benchmark the plan reaches) × target multiple 2-3 years out, plus capital return; (c) recovery — waterfall, recovery per
security vs price, time to resolution; (d) arbitrage — spread, probability, time, downside to unaffected price; (e) inflection —
EPS/FCF 2-3 years out vs current multiple relative to growth and peers. Always state the FLOOR (asset value, cash, recurring
FCF, seniority) and the SKEW (upside to target ÷ downside to floor). Thresholds: core event ≥ 2-3:1 skew and ≥ 20-30% IRR over
1-3 years; distressed 2x+; arb and credit mid-teens annualised; E4 compounders mid-teens+ with low loss probability.

Show your arithmetic in short lines. Use only pack numbers; if a needed input is missing, state the assumption and flag it.
The downside is never 0%: the bear case is at least the earnings decline already visible in the pack applied at the current
multiple, or the asset floor if lower; for a business with falling organic sales, the bear case assumes the decline continues
for the holding period. A verdict of COMPELLING requires a floor that is an asset, cash, recurring FCF of a non-declining
business, or seniority — not "a low multiple".

Return JSON:
{"method": "sotp | post_event_earnings | recovery | arb | inflection",
 "target_value": {"per_share_or_price": "...", "arithmetic": ["line [Dnn]"], "horizon_years": 0},
 "floor": {"value": "...", "basis": "... [Dnn]"}, "current_price": "... [Dnn]",
 "skew": "upside % : downside %", "irr_pct": {"base": 0, "bear": 0, "bull": 0},
 "valuation_verdict": "COMPELLING | ADEQUATE | THIN | NEGATIVE",
 "flagged_assumptions": ["anything not sourced from the pack"]}

GATE 2: {{gate2}}
FACT SHEET: {{fact_sheet}}
