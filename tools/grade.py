#!/usr/bin/env python3
"""Grade a run against its answer key with the rubric prompt (prompts/10_grader.md) and append to the scoreboard.

Usage: python tools/grade.py --run calibration/runs/<run>.json --key calibration/answer_keys/<id>.json --model llama3.1:70b
Recommended: grade with the strongest model you have (or a human); the grader does not need to be pre-dated because it sees the key.
"""
import argparse, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_agent import read, fill, chat, parse_json, PROMPTS, ROOT

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--run', required=True); ap.add_argument('--key', required=True); ap.add_argument('--model', default='llama3.1:8b')
    a = ap.parse_args()
    run = json.load(open(a.run)); key = json.load(open(a.key))
    prompt = fill(read(os.path.join(PROMPTS, '10_grader.md')), as_of_date=run['as_of_date'], answer_key=key, agent_output=run['final'])
    score = parse_json(chat(a.model, 'You are a strict, literal grader. Return JSON only.', prompt, True, 0.0, 16384))
    # Deterministic grounding share and state rule (ackman-agent/adversarial findings: grader arithmetic drifted).
    import re, math
    fin = run.get('final', {}) or {}
    texts = [fin.get('memo', '') or ''] + [(d.get('driver', '') + ' ' + ''.join('[%s]' % c for c in d.get('citations', []))) if isinstance(d, dict) else str(d) for d in fin.get('drivers', [])]
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"(])', ' '.join(texts)) if len(s.strip()) > 25]
    cited = sum(1 for s in sents if re.search(r'\[D\d\d\]', s))
    score['grounding'] = dict(score.get('grounding', {}) or {}, sentences=len(sents), cited=cited, share=round(cited / len(sents), 2) if sents else 0)
    ro = score.get('reasoning_overlap', {}) or {}
    try: k, n = int(ro.get('k', 0)), int(ro.get('n', 0))
    except Exception: k, n = 0, 0
    thr = math.ceil(0.75 * n) if n else 0
    score['state_llm'] = score.get('state')
    score['state'] = 'MISS' if score.get('direction') == 'MISS' else ('MATCH' if (score.get('direction') == 'MATCH' and k >= thr) else 'PARTIAL')
    score['actual_decision'] = key.get('actual_decision'); score['agent_decision'] = fin.get('decision')
    if fin.get('enforced_hard_fail'): score['enforced_hard_fail'] = True
    score['trade_id'] = key.get('id', run['pack']); score['run_file'] = os.path.basename(a.run); score['model_run'] = run['model']; score['grader_model'] = a.model; score['graded_at'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    os.makedirs(os.path.join(ROOT, 'calibration', 'scores'), exist_ok=True)
    fn = os.path.join(ROOT, 'calibration', 'scores', os.path.basename(a.run).replace('.json', '__score.json'))
    json.dump(score, open(fn, 'w'), indent=1, ensure_ascii=False)
    board = os.path.join(ROOT, 'calibration', 'scores', 'scoreboard.jsonl')
    with open(board, 'a') as f: f.write(json.dumps(score, ensure_ascii=False) + '\n')
    print(fn); print(json.dumps({k: score.get(k) for k in ['direction', 'state', 'discipline']}), score.get('reasoning_overlap', {}).get('k'), '/', score.get('reasoning_overlap', {}).get('n'), 'grounding', score.get('grounding', {}).get('share'))

if __name__ == '__main__': main()
