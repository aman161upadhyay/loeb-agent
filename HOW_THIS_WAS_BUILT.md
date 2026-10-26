# How this agent was built — the flow of actions

Written 2026-10-25 by the Replit agent that built the three investor agents (ackman-agent, buffett-agent, loeb-agent) for
Aman Upadhyay. Everything happened inside one Replit conversation workspace; no files were pulled from the user's machine, and
nothing was downloaded in bulk — the research was read from public web pages and written up as notes with sources.

## Technical version

1. **Research by worker subagents.** For each investor, parallel workers (`<investor>-archive`, `<investor>-trades-A/B/C`, plus
   earlier shared ones for forums/X and peer investors) used web search and page fetch to read public sources — SEC filings
   (13F, 13D, 8-K, proxies), shareholder/quarterly letters, annual-meeting and interview transcripts, decks, press, X posts,
   forum threads, and third-party screening pages (13f.info, StockAnalysis, Macrotrends, FactSet/Cboe data where cited).
   Nothing was stored as raw PDFs; each worker wrote Markdown notes with sources and dates into `archive/` (profile,
   principles, reasoning patterns, letters/interviews guides, x_posts, forums) and `compendium/trades/` (one dossier per
   decision: date, size, thesis at the time, the investor's own words, outcome, lessons, sources). Totals: Buffett 30 archive
   files / 201 dossiers; Loeb 37 / 253.
2. **Point-in-time data packs.** Pack workers turned selected decisions into `calibration/data_packs/<id>/` with `meta.json`
   (as-of date, era, mode, aliases) and docs D01-D08 (business, financials, latest results, price/valuation, market worries,
   peers, timeline, fund context), containing only what was public on the as-of date. A numbers-desk pass enriched prices and
   multiples. Sets: calibration (decisions up to 1 Aug 2025), controls (names never held, at value-looking moments), sealed
   hold-outs (decisions after 1 Aug 2025), plus a forward pack F01-F06 as of 25 Oct 2026.
3. **Agent spec and prompt chain.** `AGENT.md` (era switch, filters/gates, templates, sell rules, output contract) and a staged
   prompt chain: `00_system` → `01_fact_sheet` → gate prompts → `07_decision_memo`, with separate prompts for existing
   positions, hedging/regime, grading, leakage checks, and forward prediction. `tools/run_agent.py` and `grade.py` mirror the
   chain for offline use.
4. **Harness in the notebook.** Using the conversation's code-execution notebook, each pack was run through the chain against
   Replit's internal model, named and masked (company name/ticker/aliases replaced by "the Company"), then graded against the
   answer keys with a grader prompt plus code-level rules (direction, state, driver overlap, hard-fail enforcement, Wilson
   intervals).
5. **Calibration loop.** Misses were traced to a gate or rule; prompts were changed only from calibration cases and logged in
   `prompts/CHANGELOG.md` with the motivating case. Controls were run to catch over-permissiveness (Loeb v1.4 → 6/10 controls
   BUY → v1.5 discipline tests).
6. **Freeze and firewall.** SHA-256 hashes of AGENT.md and the prompts were recorded (`calibration/PROMPT_HASHES_v1.x.txt`);
   iteration runs moved to `calibration/prefreeze/`; a clean re-run of all calibration and controls; then the hold-outs were
   opened and run once, never used to edit prompts.
7. **Outputs.** `calibration/scores/scoreboard.md` (summary, by era/mode, per-decision, divergences, hold-out reading),
   `forward/next_trade_prediction.md` / `.json` (coverage runs merged plus the principal's reconciliation), README, run log.
8. **Push to GitHub** through the GitHub connector (Git Data API): per-directory trees with inline content, nested bottom-up,
   then a commit on `main`. Repos are private.
9. **Adversarial review.** A separate large-tier subagent, told to attack the agent and write only into `adversarial/`,
   produced seven reports; its accepted findings went into the scoreboard/README and were pushed.
10. **Final delivery.** Zips of the three repos (no `.git`) and a summary into the conversation Library; a JSON summary into
    the user's Google Drive.

## Layman version

1. **Reading up.** Several research helpers were sent out at once. They read everything public about each investor —
   regulatory filings, the letters he wrote to his investors, interviews, presentations, news, and what people said online at
   the time — and wrote it up as organized notes with sources. Nothing was copied wholesale; the notes are summaries that say
   where each fact came from.
2. **Building a trade diary.** From those notes came one page per real decision the investor made: when, how big, what he said
   his reasons were, how it turned out. About 200 pages for Buffett and 250 for Loeb.
3. **Making "exam questions."** For a chosen set of decisions, a folder was built that shows only what was knowable on that
   date — the company's numbers, its price, what the market was worried about, who the competitors were — with the answer
   (what the investor actually did) kept in a separate key. Some folders were deliberately companies he never touched, to
   check the agent knows how to say no. A sealed set of recent decisions was kept aside for the final test.
4. **Writing the rulebook.** How each investor thinks was written down, step by step, as instructions a language model can
   follow: what he looks at first, what disqualifies an idea, how he values it, how big he sizes it, when he sells.
5. **Taking the exam.** The agent read each folder, with and without the company's name, and made a call. It was graded: same
   action as the investor? Same reasons? Did it refuse the ones he refused?
6. **Fixing the rulebook.** Where it was wrong, the rule that caused it was found and changed, with a note of which case forced
   the change. The sharpest lesson: the Loeb version started buying almost every cheap, troubled company, so it needed explicit
   "walk away" rules.
7. **Locking it.** Once the rulebook was fixed, it was sealed (a fingerprint of the files) and only then were the held-back
   recent decisions opened and run once. That is the honest test, because the rules could not have been tuned to it.
8. **Writing the report card.** Scores, where it diverged from the investor and why, and a forecast of what each investor might
   do next, to be checked against filings early next year.
9. **Publishing.** Everything went into private GitHub repos in the user's account.
10. **Getting it challenged.** A separate reviewer agent was told to tear it apart. Its best criticisms were accepted and added
    to the report card, and the repos were updated.

## The caveat that applies to both versions
The testing used Replit's current model, which may remember how these trades turned out. Each repo includes the tooling
(`tools/run_agent.py`, `grade.py`, `scoreboard.py`, `canary.py`) to rerun the same exam on an older offline model (Llama 3.1 8B,
training data to Dec 2023) on a Mac Mini, which is the stricter test.

## Where the work is stored
- GitHub (private, owner aman161upadhyay): ackman-agent, buffett-agent, loeb-agent — the system of record.
- The Replit conversation workspace: the working copies of the three repositories and the deliverables folder.
- The Replit conversation Library: zips of the three repositories (without `.git`) and a one-page summary.
- Google Drive: `investor_agents_summary_2026-10-25.json` (a JSON summary with links; the Drive connector accepts JSON uploads
  only, so the zips are not mirrored there).
