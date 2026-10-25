STEP R — PORTFOLIO RISK AND REGIME REVIEW. AS_OF_DATE: {{as_of_date}}.

Third Point manages a hedged, multi-asset book. The pack describes the portfolio (gross/net exposure, top positions, factor
tilts, credit book, liquidity), the market (rates, spreads, volatility, flows, the macro regime) and recent P&L. Decide one of:
ADD_RISK — the regime favours risk and the pipeline of events/credit is rich (2009, late 2020, 2023): raise gross/net, deploy into
   credit/post-reorg/quality at discounts
REDUCE_GROSS — a liquidity or rates regime change is under way (2008, Q1 2020, Q1 2022) or a thematic book has paid and now
   carries squeeze risk (energy shorts 2016): cut gross early, exit the exposed factor, mark privates honestly
HEDGE — keep positions but add index/credit/single-name hedges against a specific risk (adding protection). Covering shorts,
   cutting both sides of a thematic book or taking down leverage is REDUCE_GROSS even when the motive is risk control — the
   label follows what happens to gross exposure, not the motive (energy shorts covered 2016 = REDUCE_GROSS; index puts added = HEDGE)
NO_CHANGE — the book is positioned for the regime

Reason from: (a) the regime evidence in the pack (rates path, spreads, liquidity, volatility) [Dnn]; (b) factor concentration of
the book (growth/duration, energy, financials, Japan) [Dnn]; (c) liquidity of the largest positions [Dnn]; (d) the pipeline of
events/credit opportunities [Dnn]; (e) the lessons: 2008 (gross and liquidity limits), Q1 2020 (cut early), 2022 (long-duration
assets are a rates bet).

Return JSON:
{"as_of_date": "...", "decision": "ADD_RISK|REDUCE_GROSS|HEDGE|NO_CHANGE", "conviction": "low|medium|high",
 "regime_evidence": "... [Dnn]", "book_exposure": "... [Dnn]", "actions": ["specific exposures to cut/add/hedge with sizes"],
 "target_gross_net": "...", "drivers": [{"driver": "one sentence reason (give 3-5 drivers, ordered by importance)", "citations": ["D02"]}],
 "memo": "2-4 paragraphs in letter voice, cited", "uncited_claims": ["..."]}

PACK:
{{pack}}
