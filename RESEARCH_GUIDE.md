# Research guide for all workers on the Loeb-agent project

## What this project is
Aman Upadhyay (HBS, Seminar in Investing, Fall 2026; sponsor Laurion Capital) is building AI agents that reason like
specific great investors. This repository is the **Dan Loeb / Third Point** agent (a sibling of `ackman-agent/`, which is
finished and is the template for everything here — same folder layout, same file schemas, same grading harness). The agent
is graded on *fidelity of decision AND reasoning* to Loeb's real decisions, replayed point-in-time, not on returns.
Rubric per trade: Direction, Reasoning overlap (did it cite the drivers Loeb cited?), Discipline (does it pass on what he passed
on?), Grounding (claims traceable to the data pack, not model memory). The final model is a small, pre-dated open model
(Llama 3.1 8B, data to Dec 2023), so everything the agent must "know" has to be written down explicitly.

Today's date: 25 October 2026. Anything up to today is fair game for the archive. Be especially careful with 2024-2026
events (the Q3 2024-Q2 2026 quarterly letters, every 13F from Q3 2025 through Q2 2026, Loeb's X posts, any 13D/activist
campaign, Third Point Investors Ltd / Malibu Life Re developments, SiriusPoint, the AI and credit books) because those are
the hold-out decisions.

Era switch used in this repo (keep these labels): A = 1995-2008 (small-cap event-driven, the "Mr. Pink" message-board years,
the poison-pen 13D letters: Star Gas, Ligand, Massey, Potlatch, InterCept, Penn Virginia, PDL, Pogo; 2008 drawdown);
B = 2009-2015 (post-crisis credit and distressed — Delphi, Chrysler/Ford/CIT paper, Greek bonds; large-cap constructivism —
Yahoo, Sony I, Herbalife long, Sotheby's, Dow, Amgen, Baxter, Seven & i; Fannie/Freddie prefs); C = 2016-mid 2025 (Nestlé, Honeywell,
UTX, Campbell, Sony II, Disney I/II, Prudential, Intel, PG&E, Shell, Colgate, Bath & Body Works, the 2022 drawdown, AI/quality
book, Far Point/Global Blue, TPIL fight, CoStar/Kenvue/Soho House 2025); E = hold-out, H2 2025-2026.

## Tools that work here (use them from CodeExecution)
- `webSearch({ query, searchQueries: [..], count: 10, isTextExtended: true })` — best first move. Returns snippets + URLs.
- `webFetch({ url })` — fetch a page/PDF as markdown (50k-char chunks; use `startIndex` to continue).
- `externalApi__exa({ path:'/search', method:'POST', headers:{'Content-Type':'application/json'}, body:{ query, numResults: 10, contents:{ text:{ maxCharacters: 3000 } }, startPublishedDate?, endPublishedDate?, includeDomains? } })` — semantic search with page text; `/contents` with `urls:[...]` pulls full text (works where Firecrawl is rate-limited).
- `externalApi__firecrawl({ path:'/scrape', method:'POST', headers:{'Content-Type':'application/json'}, body:{ url, formats:['markdown'] } })` — works on x.com profile and status URLs (returns post text + thread), SEC EDGAR pages, PDFs, most news sites. `/search` with `body:{ query:'site:x.com/DanielSLoeb1 disney', limit:10 }` finds X posts by topic. Expect 429s under load; back off.
- `queryWithLLM({ content, query })` — ask a question of a long document (a 20-page quarterly letter) instead of reading it all.
- NOT available: the X API (402). Reddit: `webFetch` is blocked; try Firecrawl on `https://old.reddit.com/...` and snippets via `webSearch`/Exa.
- Keep ≤5 Exa/Firecrawl requests in flight at once.

## High-value primary sources
- Third Point quarterly investor letters: https://www.thirdpoint.com (Investor Letters page; PDFs usually under thirdpointlimited.com
  or thirdpoint.com/wp-content/uploads/...), 2010-2026. Pre-2010 letters: Insider Monkey, ValueWalk, Scribd, market folly, Dealbreaker,
  Wayback Machine (thirdpoint.com/letters), "Third Point Q4 2008 letter" searches.
- Third Point Investors Ltd (London-listed feeder; tickers TPOU/TPIL; now Malibu Life Reinsurance since 2025): monthly reports and
  quarterly letters at https://www.thirdpointlimited.com — exposure tables, top positions, monthly performance.
- SEC: Third Point LLC 13F (CIK 1040273; history on 13f.finance, dataroma, whalewisdom, stockcircle, fintel), 13D filings and the
  famous exhibit letters (Star Gas Feb 2005 — "Irik Sevin"; Ligand 2005-06; Massey 2005-06; Potlatch 2003; InterCept 2004;
  Penn Virginia 2004; Pogo 2007; PDL 2008; Yahoo 2011-12 incl. the Scott Thompson résumé letter; Sotheby's Oct 2013; Sony May 2013 letter
  and June 2019 "A Stronger Sony" deck; Dow Jan 2014 and the Dow presentation; Baxter 2015; Seven & i Oct 2015 letter; Nestlé June 2017
  letter and July 2018 "Nestlé: The Path to Value Creation" deck; UTX May 2018 letter; Campbell 2018 proxy materials and settlement;
  Prudential Feb 2020 letter; Disney Oct 2020 and Aug 2022 letters; Intel Dec 2020 letter; Shell Oct 2021 Q3 letter; Colgate 2022;
  Bath & Body Works Feb 2022 settlement; Advance Auto / Soho House / CoStar / Kenvue 2025 materials).
- Loeb's X account @DanielSLoeb1 (active; long posts on positions, politics, Sony, Disney, Nvidia/AI, Soho House). Scrape the profile
  and individual statuses with Firecrawl; find statuses with Firecrawl `/search` queries like `site:x.com/DanielSLoeb1 sony`.
- Interviews/talks: Sohn/Robin Hood/Delivering Alpha/Bloomberg Invest presentations (Sony 2019, Nestlé 2018, Baxter 2015), CNBC and
  Bloomberg interviews, *The Alpha Masters* (Maneet Ahuja, 2012) Loeb chapter, Vanity Fair/New Yorker/NYT profiles ("Dan Loeb's
  constructivism"), Institutional Investor "Loeb's letters" pieces, HBS/Columbia cases on Yahoo/Sony/Sotheby's, Graham & Doddsville.
- Forums/discussion: Value Investors Club write-ups on Third Point situations, COBF threads ("Third Point", "Loeb letter"), Reddit
  r/SecurityAnalysis / r/investing / r/wallstreetbets threads on Yahoo/Sony/Disney/Intel letters, Seeking Alpha, FinTwit, Dealbreaker,
  market folly's "Third Point letter" posts (2008-2016 — very complete).

## Writing rules
1. Every factual claim gets a source (URL + date) inline or in a numbered list. Prefer primary sources (letters, 13Ds, transcripts, X posts).
2. **No hindsight contamination** in "point-in-time" sections: write only what was knowable on that date and date-stamp numbers.
3. Quote Loeb verbatim wherever possible; his *stated reasons at the time* (quarterly letter, 13D letter, X post) are the grading key.
   Mark hindsight quotes as hindsight.
4. Be honest about losses and reversals (2008, Q1 2020, 2022, Herbalife exit, Intel, Disney II, the SPAC/Upstart era, TPIL discount fight);
   divergences are as valuable as matches.
5. Where sources conflict or you are unsure, say so explicitly (`unverified`, `conflicting`). Never invent dates, numbers or quotes.
6. Dense, factual prose and tables; no filler.
7. Files are Markdown; keep each under ~60 KB; split if needed. Write with the `writeFile` callback or the WriteFile tool.
8. When you finish, append a short entry to `loeb-agent/run_log.md` (what you produced, open gaps, corrections you verified).
9. Mirror the Ackman repo's file schemas exactly: `compendium/SCHEMA.md` (trade files), `calibration/README.md` (packs/keys),
   and look at `ackman-agent/calibration/data_packs/2025_uber_buy/` + `ackman-agent/calibration/answer_keys/2025_uber_buy.json`
   as the worked example of a pack and key. In `meta.json` use `fund_aum_usd_bn` (Third Point firm or Offshore fund AUM, say which)
   instead of `pershing_aum_usd_bn`.
