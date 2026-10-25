#!/usr/bin/env python3
"""Summarise calibration/scores/scoreboard.jsonl into a markdown table with Wilson intervals (small-N honest reporting)."""
import json, math, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def wilson(k, n, z=1.96):
    if n == 0: return (0, 0)
    p = k / n; d = 1 + z*z/n; c = p + z*z/(2*n); h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return ((c-h)/d, (c+h)/d)
rows = [json.loads(l) for l in open(os.path.join(ROOT, 'calibration', 'scores', 'scoreboard.jsonl')) if l.strip()]
by_model = collections.defaultdict(list)
for r in rows: by_model[(r.get('model_run'), r.get('run_file','').endswith('__masked.json'))].append(r)
print('| model | masked | N | direction match | state match | state partial | drivers k/n | grounding | leakage flags |')
print('|---|---|---|---|---|---|---|---|---|')
for (m, masked), rs in by_model.items():
    n = len(rs); dm = sum(r.get('direction') == 'MATCH' for r in rs); sm = sum(r.get('state') == 'MATCH' for r in rs); sp = sum(r.get('state') == 'PARTIAL' for r in rs)
    k = sum((r.get('reasoning_overlap') or {}).get('k', 0) for r in rs); nn = sum((r.get('reasoning_overlap') or {}).get('n', 0) for r in rs)
    g = [ (r.get('grounding') or {}).get('share') for r in rs if (r.get('grounding') or {}).get('share') is not None ]
    leaks = sum(len((r.get('grounding') or {}).get('leakage_flags', [])) for r in rs)
    lo, hi = wilson(dm, n)
    print(f"| {m} | {masked} | {n} | {dm}/{n} (95% CI {lo:.0%}-{hi:.0%}) | {sm}/{n} | {sp}/{n} | {k}/{nn} | {sum(g)/len(g):.0%} | {leaks} |" if g else f"| {m} | {masked} | {n} | {dm}/{n} | {sm}/{n} | {sp}/{n} | {k}/{nn} | n/a | {leaks} |")
