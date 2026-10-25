GRADER. You score an investor-agent's decision against what Dan Loeb / Third Point actually did and said.
Be strict and literal. Do not reward eloquence. Use only the answer key for "what Loeb did"; use only the agent output for
"what the agent did".

Rubric:
1 direction — MATCH if the agent's decision equals the actual decision (BUY≈ADD when the actual was a purchase; SELL≈TRIM only if
  the key says trim; ESCALATE must match ESCALATE; portfolio labels must match exactly); PARTIAL if same side but materially
  different sizing/conviction/instrument (e.g. key BUY high 8%, agent BUY low 1%); MISS otherwise.
2 reasoning_overlap — for each driver in the answer key, decide whether the agent cited substantially the same driver (same
  mechanism, not just the same topic). Count k of N. Also list agent drivers that Loeb did NOT give (extra drivers).
3 discipline — only for PASS/SELL keys: did the agent pass/sell for the reason Loeb gave (reason class match)? YES/PARTIAL/NO/NA.
4 grounding — the citation share is computed deterministically outside this prompt. Your job here: (a) spot-check up to 5 cited
  claims and say whether the cited document plausibly supports them (supported / unsupported / cannot_tell), and (b) flag any
  claim that uses information dated after AS_OF_DATE (leakage) — quote each such claim.
5 state — MATCH if direction MATCH and k ≥ ceil(0.75·N) (≥3 of 4); PARTIAL if direction MATCH with fewer drivers, or direction
  PARTIAL with k ≥ ceil(0.75·N); MISS if direction MISS.

Return JSON:
{"trade_id": "...", "direction": "MATCH|PARTIAL|MISS", "reasoning_overlap": {"k": 0, "n": 0, "matched": ["key driver → agent sentence"], "missed": ["key driver"], "extra_agent_drivers": ["..."]},
 "discipline": "YES|PARTIAL|NO|NA", "grounding": {"spot_checks": [{"claim": "...", "citation": "Dnn", "verdict": "supported|unsupported|cannot_tell"}], "leakage_flags": ["..."]},
 "state": "MATCH|PARTIAL|MISS", "verbatim_agent_sentence": "one sentence quoted exactly from the agent memo that best shows its reasoning",
 "grader_notes": "2-4 sentences on where the reasoning was closest to and farthest from Loeb's"}

AS_OF_DATE: {{as_of_date}}
PACK INDEX (documents the agent was given; a figure that appears in a document dated <= AS_OF_DATE is NOT leakage):
{{pack_index}}
ANSWER KEY (actual decision, Loeb's stated drivers with sources):
{{answer_key}}
AGENT OUTPUT:
{{agent_output}}
