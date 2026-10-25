STEP 1 — FACT SHEET. AS_OF_DATE: {{as_of_date}}. Company: {{company}} ({{ticker}}).

Read the pack documents below and produce a structured fact sheet. Copy numbers exactly; attach the document label to every
item. If an item is absent, write "not in pack". Do not add anything from memory. If documents conflict, record both figures
and label the conflict — do not average or pick silently.

Return JSON:
{
 "business_description": "2-3 sentences [Dnn]",
 "segments_and_separable_assets": ["each segment/stake/asset with revenue, EBITDA or value evidence and peer multiples [Dnn]"],
 "economics_vs_peers": ["margins, growth, returns, capital intensity against named peers; the margin gap in bp [Dnn]"],
 "capital_structure": ["debt by instrument, maturities, cash, leverage, credit ratings, where the fulcrum sits, covenants [Dnn]"],
 "price_and_valuation": ["price, market cap, EV, EV/EBITDA, P/E, FCF yield, sum-of-the-parts inputs, drawdown, own history [Dnn]"],
 "management_board_governance": ["CEO/chair tenure and record, board composition, controller/family/government stakes, pill, staggered board, nomination window, prior activist history [Dnn]"],
 "shareholder_base_and_liquidity": ["top holders, index ownership, short interest, average daily volume [Dnn]"],
 "event_or_catalyst_evidence": ["announced or possible events: spin, sale, restructuring, merger, regulatory decision, management change, buyback capacity [Dnn]"],
 "what_the_market_is_worried_about": ["each worry with its source [Dnn]"],
 "deal_or_instrument_terms_if_any": ["bond/loan/convert/DIP terms, spread, timetable, conditions [Dnn] or not in pack"],
 "recent_events": ["dated events up to AS_OF_DATE [Dnn]"],
 "third_point_context": ["AUM, gross/net, existing stake and basis, prior engagement, letters already public, other positions in the sector [Dnn] or not in pack"],
 "document_conflicts": ["any figures or claims on which documents disagree, with both labels"],
 "missing_data": ["figures you wanted but the pack lacks"]
}

PACK:
{{pack}}
