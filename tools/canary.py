#!/usr/bin/env python3
"""Plant a canary fact in a pack (a harmless, invented but plausible detail) and later verify the agent cited it.
Usage: python tools/canary.py plant calibration/data_packs/<id>   -> writes docs/D99_canary.md and records the canary in meta.json
       python tools/canary.py check calibration/runs/<run>.json   -> reports whether the canary text appears in the agent output
"""
import json, os, sys, random
if __name__ == '__main__':
    cmd, path = sys.argv[1], sys.argv[2]
    if cmd == 'plant':
        meta = json.load(open(os.path.join(path, 'meta.json')))
        canary = f"The company disclosed that its {random.choice(['Omaha','Tulsa','Reno','Albany'])} regional office lease runs through {random.randint(2027, 2034)}."
        meta['canary'] = canary; json.dump(meta, open(os.path.join(path, 'meta.json'), 'w'), indent=1)
        open(os.path.join(path, 'docs', 'D99_canary.md'), 'w').write(f"Title: Lease footnote\nSource: company filing (footnote)\nDate: {meta['as_of_date']}\n\n{canary}\n")
        print('planted:', canary)
    else:
        run = json.load(open(path)); txt = json.dumps(run)
        meta = json.load(open(os.path.join(os.path.dirname(os.path.dirname(path)), 'data_packs', run['pack'], 'meta.json')))
        print('canary cited:', meta.get('canary', '')[:40] in txt or 'D99' in txt)
