# Pack-worker brief (Loeb agent) — read fully before building anything

You are building point-in-time DATA PACKS and ANSWER KEYS for the calibration/hold-out replay of the Loeb agent.
Read first: loeb-agent/RESEARCH_GUIDE.md (tools + sources), loeb-agent/calibration/README.md (layout), loeb-agent/AGENT.md
(the decision process the agent follows — your packs must contain the evidence that process needs: business economics,
record, management, price/valuation, the worry/cloud, the fund's own context), and the worked example
ackman-agent/calibration/data_packs/2025_uber_buy/ (meta.json + docs/D01..D08) with ackman-agent/calibration/answer_keys/2025_uber_buy.json.
Use the trade dossiers already written in loeb-agent/compendium/trades/ (and their INDEX files) as your starting point for
dates, sizes and stated drivers; verify against primary sources and correct them if wrong (note corrections in run_log.md).

## Pack = folder calibration/data_packs/<trade_id>/ containing
- meta.json: {"id", "company", "ticker", "aliases": [every name/brand/ticker/subsidiary string that would reveal the identity
  when masked — be exhaustive], "as_of_date": "YYYY-MM-DD", "mode": "new|existing|hedge", "era": "A|B|C|D|E",
  "first_action_window": "...", "fund_aum_usd_bn": <number; say in notes which figure>, "instrument": "common|options|convert|bond|loan|CDS|SPAC|private", "notes": "..."}
  mode: "new" = a purchase/short decision not yet owned; "existing" = sell/hold/add/trim/escalate on a position already held
  (the pack must describe the original thesis and what happened since); "hedge" = a portfolio/market-level decision
  (portfolio risk / regime decisions: ADD_RISK / REDUCE_GROSS / HEDGE / NO_CHANGE — e.g. 2008 gross cut, Q1 2020, 2022 growth cut, 2016 energy shorts).
- docs/D01_business_overview.md, D02_financial_snapshot.md, D03_latest_results.md, D04_price_valuation.md, D05_market_worries.md,
  D06_peer_industry.md, D07_event_timeline.md, D08_fund_context.md (Third Point context: AUM, gross/net exposure, top positions, credit book, prior engagement with the company, nomination windows, prior public statements before as_of). Add D09/D10 when the case needs
  them (deal terms; capital structure; a 13D letter already public; a prior public statement by the investor BEFORE as_of).
  Each doc starts with three header lines: "Title: ...", "Source: <url or citation>", "Date: YYYY-MM-DD" and the Date MUST be
  ≤ as_of_date. 300-900 words per doc, dense numbers, no filler. 2-6 KB each; the whole pack ≤ 40 KB.
- POINT-IN-TIME DISCIPLINE: nothing dated after as_of_date; no outcome language ("as it turned out", "would later"); price and
  multiples as of the as_of_date or the last close before it; if you cannot recover a figure, write "not available in
  contemporaneous sources" rather than inventing it, and say so in meta.notes. Old cases (pre-1995) are reconstructed from
  letters, books (cite chapter) and period press: label reconstructed figures "(reconstructed from <source>)".
- D05 must state the bear case honestly and strongly (what a sceptic said at the time); D08 must give the fund's situation
  (cash/AUM, existing holdings, constraints, prior statements) WITHOUT revealing the decision.
- Do NOT write the decision, the investor's later rationale, or hints about it anywhere in docs/. The pack is what an analyst
  would have had on the desk that day.

## Answer key = calibration/answer_keys/<trade_id>.json (hold-outs go in answer_keys/holdout/)
{"id", "actual_decision": "BUY|SHORT|PASS|HOLD|ADD|TRIM|SELL|ESCALATE|ADD_RISK|REDUCE_GROSS|HEDGE|NO_CHANGE", "conviction": "low|medium|high", "size_pct_nav": "number or text with basis",
 "first_action_date", "disclosure_date", "reason_class": "L1-L5 (see AGENT.md §4) or null", "opportunity_template": [..],
 "catalyst_role": "...", "instrument": "...", "plan": {"actors": [], "governance_route": "", "timetable_quarters": 0}, "drivers": [3-6 × {"driver": one sentence in the investor's own framing, "source": url (date),
 "quote": verbatim quote or null}], "entry_valuation_stated": "...", "outcome_note": "...", "sources": [...],
 "pack_quality_notes": "what you could not recover"}.
Drivers must be the investor's STATED reasons at or near the time (letter, interview, filing, X post), with quotes where they
exist; mark hindsight explanations (e.g. a letter written months later) with the date. For controls the key is PASS with the
documented reason (or "never owned per 13F history; no public comment" if silent).

## Quality bar (checked by the orchestrator)
- JSON parses; every doc has the three header lines with Date ≤ as_of_date; no doc mentions events after as_of_date (grep
  yourself for later years); aliases complete; the pack supports every driver in the key (an analyst could reach them).
- Controls: verify from 13F history/letters that the investor never held the name in the window; the pack must look like a
  plausible buy (that is the point) and the key explains why it was a PASS.
- When done: append a run_log.md entry (packs built, gaps, corrections) and write calibration/<your-set>_MANIFEST.md listing
  trade_id, as_of_date, mode, era, actual decision, one-line why, and pack quality grade (A/B/C).
Work in parallel batches of 3-4 packs; prefer Exa /contents, webFetch and Firecrawl per the RESEARCH_GUIDE; python3 is available
(node is not). Keep going until the full list is built; do not stop to ask questions — make the decision and document it.
