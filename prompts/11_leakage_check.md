LEAKAGE CHECK. AS_OF_DATE: {{as_of_date}}. Read the agent output and list every statement that depends on information
that could only be known after AS_OF_DATE (later prices, results, management changes, deal outcomes, "as it turned out",
future tense facts stated as known). Also check whether the canary fact "{{canary}}" (planted in the pack) was cited —
if the agent never used it, the pack may not have been read. Return JSON:
{"leakage_statements": ["quoted statement — why it is post-date"], "leakage_count": 0, "canary_cited": true}

AGENT OUTPUT:
{{agent_output}}

