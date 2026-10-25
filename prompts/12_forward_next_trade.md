FORWARD — WHAT DOES THIRD POINT DO IN THE NEXT 60-90 DAYS? AS_OF_DATE: {{as_of_date}}.

Inputs: (a) Third Point's current portfolio, exposures, credit book, recent letters and X posts, open engagements and
settlements (pack); (b) a candidate list of companies with Third Point-type set-ups — conglomerate/sum-of-parts discounts,
margin gaps vs peers, lazy balance sheets, governance problems with open nomination windows, announced spins/deals, post-reorg
equities, distressed capital structures, quality names at inflections — with price, valuation vs peers, holder base and
catalyst calendar (pack); (c) market/regime context: rates, spreads, volatility, M&A and activism activity (pack).

Method:
1 Regime first (prompt R logic): decide whether the book is adding risk, reducing gross or hedging; that sets how many new
  events to expect.
2 Rank candidates by the Third Point trigger: Gate 1 PASS (event + edge + route + floor + size), skew ≥ 2-3:1, a catalyst or
  nomination window inside 2-4 quarters, and fit with recent letter themes. Separate activist (E1) candidates from E2-E5.
3 Existing positions: flag likely ESCALATE (private engagement ageing, window opening), ADD (skew improved), TRIM/SELL (L1-L5).
4 Output a ranked list with a probability that the action is disclosed within 90 days (13F, 13D, letter, press), the expected
  action, instrument and size, and a one-paragraph thesis in letter voice. Probabilities should sum to a realistic expected count
  (Third Point discloses 1-3 new top positions and 0-2 public engagements per quarter).

Return JSON:
{"as_of_date": "...", "regime_decision": "ADD_RISK|REDUCE_GROSS|HEDGE|NO_CHANGE", "expected_new_positions_next_90_days": 0.0,
 "candidates": [{"rank": 1, "company": "...", "ticker": "...", "action": "NEW_BUY|NEW_SHORT|ADD|TRIM|SELL|ESCALATE", "probability_90d": 0.0,
   "template": "E1|E2|E3|E4|E5|E6|E7", "instrument": "...", "trigger": "why now [Dnn]", "valuation": "skew, target [Dnn]",
   "size_pct_nav": 0, "thesis_paragraph": "letter voice, cited", "what_would_confirm": "what filing/letter/post would reveal it"}],
 "existing_position_changes": [{"company": "...", "action": "...", "probability_90d": 0.0, "reason_class": "L1..L5|ESCALATE", "why": "..."}],
 "uncited_claims": ["..."]}

PACK:
{{pack}}
