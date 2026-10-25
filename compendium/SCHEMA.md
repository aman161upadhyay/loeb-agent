# Trade file schema (one markdown file per trade in compendium/trades/)

File name: `YYYY_ticker_or_name.md` (entry year first, e.g. `2011_cp.md`, `2012_herbalife_short.md`).

Each file begins with a YAML front-matter block, then sections. Every factual claim must carry a source
(URL + date). Where sources disagree, say so. Where unknown, write `unknown` (never invent).

```yaml
---
id: 2011_yhoo
company: Yahoo! Inc.
ticker: YHOO
vehicle: Third Point            # Third Point LLC | Third Point Offshore | Third Point Investors Ltd | Third Point Re / SiriusPoint | Far Point (SPAC) | personal
type: activist_long                 # activist_long | passive_long | control | acquisition | preferred_or_credit | short | macro_hedge | spac | merger_arb | other
status: closed                      # open | closed
entry_date: 2011-09                 # first purchase (YYYY-MM or YYYY-MM-DD); 'unknown' if not known
disclosure_date: 2011-10-28         # 13D / letter / interview that revealed it
exit_date: 2016-08                  # 'n/a' if still open
holding_period_months: 59
peak_position: "14.2% of CP; ~$1.4B; ~X% of fund"
entry_price_context: "~C$46-60/share; ~12x EBITDA; stock -X% vs peers over 3y"
outcome: "+~$2.6B realized; ~3x"   # include loss cases honestly
outcome_class: big_win              # big_win | win | flat | loss | big_loss | ongoing
drivers:                            # 3-6 short labels of the reasons Loeb HIMSELF gave at the time
  - "Worst operating ratio among Class I rails (81% vs ~65-70%)"
  - "Fixable: same assets as CN; operations, not franchise, were the problem"
  - "Specific plan: install Hunter Harrison as CEO"
  - "Valuation: limited downside, 2-3x upside if OR reaches 65%"
pattern_tags: [simple_predictable_fcf, underperformer_vs_peers, management_change, operational_turnaround, proxy_fight]
sources:
  - "https://... (13D, 2011-10-28)"
  - "https://... (Third Point 2011 annual letter)"
---
```

## Sections (in this order)

1. **Situation before the trade (point-in-time)** — what a careful public-markets investor could have known on the
   entry date: business description, financials snapshot, stock performance, consensus narrative, what was wrong.
   NO hindsight here. Date-stamp every number.
2. **Loeb's thesis in his own words** — verbatim quotes (letters, 13D, interviews, presentations) with dates and URLs.
3. **What Third Point did** — timeline of actions (purchase, 13D, letters, proxy fight, board seats, settlements, adds/trims, exit).
4. **What happened after** — outcome, P&L, how the thesis played out, and what Loeb said in hindsight (letters, interviews).
5. **Reasoning drivers checklist** — the 3-6 drivers (as in front-matter) with one sentence each on evidence. These are
   the answer key the agent is graded against.
6. **Why this trade fits / breaks his pattern** — how it relates to his stated principles at the time; what changed in his process after.
7. **Public discussion** — what X/Twitter, Reddit, VIC, COBF, Seeking Alpha, press said at the time (with links); contrarian views.
8. **Sources** — full list.
