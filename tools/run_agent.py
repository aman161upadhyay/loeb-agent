#!/usr/bin/env python3
"""Run the Loeb agent prompt chain on a point-in-time data pack with a local Ollama model.

Usage:
  python tools/run_agent.py --pack calibration/data_packs/2025_uber_buy --model llama3.1:8b
  python tools/run_agent.py --pack ... --model llama3.1:8b --one-shot          # single call from AGENT.md (strong models)
  python tools/run_agent.py --pack ... --model llama3.1:8b --mask              # replace company name/ticker with 'the Company'
Env: OLLAMA_URL (default http://localhost:11434). Set OPENAI_BASE_URL/OPENAI_API_KEY to use an OpenAI-compatible endpoint instead.
Outputs: calibration/runs/<pack_id>__<model>__<timestamp>.json (all stage outputs + final decision).
"""
import argparse, json, os, re, sys, time, glob, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS = os.path.join(ROOT, 'prompts')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

def load_pack(pack_dir, mask=False):
    meta = json.load(open(os.path.join(pack_dir, 'meta.json')))
    docs = sorted(glob.glob(os.path.join(pack_dir, 'docs', '*.md')))
    parts = []
    for i, d in enumerate(docs, 1):
        label = f"D{i:02d}"
        body = read(d)
        parts.append(f"===== [{label}] {os.path.basename(d)} =====\n{body}\n")
    pack = "\n".join(parts)
    if mask:
        for name in [meta.get('company',''), meta.get('ticker','')] + meta.get('aliases', []):
            if name: pack = re.sub(re.escape(name), 'the Company', pack, flags=re.I)
        meta = dict(meta, company='the Company', ticker='XXX')
    return meta, pack

def fill(template, **kw):
    out = template
    for k, v in kw.items():
        out = out.replace('{{' + k + '}}', v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, indent=1))
    return out

def chat(model, system, user, json_mode=True, temperature=0.1, num_ctx=16384):
    base = os.environ.get('OPENAI_BASE_URL')
    if base:  # OpenAI-compatible
        req = urllib.request.Request(base.rstrip('/') + '/chat/completions', method='POST',
            headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + os.environ.get('OPENAI_API_KEY', 'x')},
            data=json.dumps({'model': model, 'temperature': temperature,
                             'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}],
                             **({'response_format': {'type': 'json_object'}} if json_mode else {})}).encode())
        resp = json.load(urllib.request.urlopen(req, timeout=600))
        return resp['choices'][0]['message']['content']
    url = os.environ.get('OLLAMA_URL', 'http://localhost:11434').rstrip('/') + '/api/chat'
    payload = {'model': model, 'stream': False, 'options': {'temperature': temperature, 'num_ctx': num_ctx},
               'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}]}
    if json_mode: payload['format'] = 'json'
    req = urllib.request.Request(url, method='POST', headers={'Content-Type': 'application/json'}, data=json.dumps(payload).encode())
    resp = json.load(urllib.request.urlopen(req, timeout=1800))
    return resp['message']['content']

def parse_json(s):
    try: return json.loads(s)
    except Exception:
        m = re.search(r'\{.*\}', s, flags=re.S)
        if m:
            try: return json.loads(m.group(0))
            except Exception: pass
    return {'_raw': s}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pack', required=True); ap.add_argument('--model', default='llama3.1:8b')
    ap.add_argument('--one-shot', action='store_true'); ap.add_argument('--mask', action='store_true')
    ap.add_argument('--temperature', type=float, default=0.1); ap.add_argument('--num-ctx', type=int, default=16384)
    a = ap.parse_args()
    meta, pack = load_pack(a.pack, a.mask)
    system = read(os.path.join(PROMPTS, '00_system.md'))
    common = dict(as_of_date=meta['as_of_date'], company=meta['company'], ticker=meta['ticker'])
    out = {'pack': os.path.basename(a.pack.rstrip('/')), 'model': a.model, 'mode': meta.get('mode', 'new'), 'masked': a.mask,
           'as_of_date': meta['as_of_date'], 'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'stages': {}}
    t0 = time.time()
    mode = meta.get('mode', 'new')
    if a.one_shot:
        p = fill(read(os.path.join(PROMPTS, 'one_shot_full.md')), agent_md=read(os.path.join(ROOT, 'AGENT.md')), pack=pack, mode=mode, **common)
        out['final'] = parse_json(chat(a.model, system, p, True, a.temperature, max(a.num_ctx, 32768)))
    elif mode == 'existing':
        p = fill(read(os.path.join(PROMPTS, '08_sell_hold.md')), pack=pack, **common)
        out['final'] = parse_json(chat(a.model, system, p, True, a.temperature, a.num_ctx))
    elif mode == 'hedge':
        p = fill(read(os.path.join(PROMPTS, '09_hedge.md')), pack=pack, **common)
        out['final'] = parse_json(chat(a.model, system, p, True, a.temperature, a.num_ctx))
    else:
        fs = parse_json(chat(a.model, system, fill(read(os.path.join(PROMPTS, '01_fact_sheet.md')), pack=pack, **common), True, a.temperature, a.num_ctx)); out['stages']['fact_sheet'] = fs
        g1 = parse_json(chat(a.model, system, fill(read(os.path.join(PROMPTS, '02_gate1_business_quality.md')), fact_sheet=fs, **common), True, a.temperature, a.num_ctx)); out['stages']['gate1'] = g1
        if isinstance(g1, dict) and isinstance(g1.get('criteria'), dict):  # deterministic hard-fail rule (02_gate1): FAIL on 1 or 4, both 2 and 3, or >=3 FAILs
            c = g1['criteria']; F = lambda k: isinstance(c.get(k), dict) and c[k].get('score') == 'FAIL'
            n_fail = sum(1 for v in c.values() if isinstance(v, dict) and v.get('score') == 'FAIL')
            hf = F('event_identified') or F('downside_floor') or (F('edge') and F('governance_route_or_process')) or n_fail >= 3
            if hf != (g1.get('hard_fail') is True): g1['hard_fail_model'] = g1.get('hard_fail'); g1['hard_fail'] = hf; g1['hard_fail_recomputed'] = True
        g2 = parse_json(chat(a.model, system, fill(read(os.path.join(PROMPTS, '03_gate2_why_mispriced.md')), fact_sheet=fs, gate1=g1, **common), True, a.temperature, a.num_ctx)); out['stages']['gate2'] = g2
        g3 = parse_json(chat(a.model, system, fill(read(os.path.join(PROMPTS, '04_gate3_valuation.md')), fact_sheet=fs, gate2=g2, **common), True, a.temperature, a.num_ctx)); out['stages']['gate3'] = g3
        g4 = parse_json(chat(a.model, system, fill(read(os.path.join(PROMPTS, '05_gate4_catalyst_role.md')), fact_sheet=fs, gate1=g1, gate2=g2, gate3=g3, **common), True, a.temperature, a.num_ctx)); out['stages']['gate4'] = g4
        g5 = parse_json(chat(a.model, system, fill(read(os.path.join(PROMPTS, '06_gate5_risk_sizing.md')), fact_sheet=fs, gate1=g1, gate2=g2, gate3=g3, gate4=g4, **common), True, a.temperature, a.num_ctx)); out['stages']['gate5'] = g5
        fin = parse_json(chat(a.model, system, fill(read(os.path.join(PROMPTS, '07_decision_memo.md')), fact_sheet=fs, gate1=g1, gate2=g2, gate3=g3, gate4=g4, gate5=g5, **common), True, a.temperature, a.num_ctx)); out['final'] = fin
        # Code-level hard-fail enforcement (v1.6 lesson from ackman-agent/adversarial: the memo step must not overturn Gate 1).
        if isinstance(g1, dict) and g1.get('hard_fail') is True and not (False) and str(fin.get('decision', '')).upper() in ('BUY', 'SHORT'):
            fin['decision_before_enforcement'] = fin.get('decision'); fin['decision'] = 'PASS'; fin['enforced_hard_fail'] = True
            fin['memo'] = '[Gate 1 hard fail enforced in code: the decision step returned %s; per the process a hard fail terminates in PASS.]\n\n%s' % (fin['decision_before_enforcement'], fin.get('memo', ''))
    out['elapsed_s'] = round(time.time() - t0, 1)
    os.makedirs(os.path.join(ROOT, 'calibration', 'runs'), exist_ok=True)
    fn = os.path.join(ROOT, 'calibration', 'runs', f"{out['pack']}__{a.model.replace(':','-').replace('/','-')}__{time.strftime('%Y%m%d-%H%M%S')}{'__masked' if a.mask else ''}.json")
    json.dump(out, open(fn, 'w'), indent=1, ensure_ascii=False)
    print(fn); print(json.dumps({k: out['final'].get(k) for k in ['decision', 'conviction', 'target_size_pct_nav', 'reason_class']}, ensure_ascii=False))
    for d in out['final'].get('drivers', []): print(' -', d.get('driver') if isinstance(d, dict) else d)

if __name__ == '__main__': main()
