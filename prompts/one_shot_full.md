ONE-SHOT MODE (for strong models). Read AGENT.md in full, then the pack. AS_OF_DATE: {{as_of_date}}. Company: {{company}} ({{ticker}}). Mode: {{mode}}.

Work through Gates 1-6 of AGENT.md explicitly (headed sections, each with cited evidence), then return the final JSON
object of Section 8 of AGENT.md. Every factual sentence must end with a pack citation [Dnn]. Use nothing dated after
AS_OF_DATE and nothing from memory. If mode is "existing", use the sell/hold rules of Section 4 and include
"reason_class" (L1-L5, ESCALATE or THESIS_ON_TRACK). If mode is "hedge", use prompts/09_hedge.md (portfolio risk and regime).

AGENT.md:
{{agent_md}}

PACK:
{{pack}}
