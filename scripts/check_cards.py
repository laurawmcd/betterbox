#!/usr/bin/env python3
"""Check _data against itself and against the existing site pages. Run from the repo root: python3 scripts/check_cards.py
Reports: slot counts per suit, missing or thin web text, unknown card ids in `related`, banned client-specific words,
old site pages with no redirect, and duplicate ids or redirect sources."""
import glob, os, re, sys, yaml
cards = yaml.safe_load(open('_data/cards.yml'))
suits = {s['id']: s for s in yaml.safe_load(open('_data/suits.yml'))}
retired = yaml.safe_load(open('_data/retired.yml'))
web = {s: yaml.safe_load(open(f'_data/web/{s}.yml')) for s in suits}
ids = [c['id'] for c in cards]
real = {c['id'] for c in cards if c['status'] in ('confirmed', 'proposed')}
problems = []
def bad(msg): problems.append(msg); print('PROBLEM:', msg)

for i in {x for x in ids if ids.count(x) > 1}: bad(f'duplicate id {i}')
for sid, s in suits.items():
    mine = [c for c in cards if c['suit'] == sid]
    named = [c for c in mine if c['status'] in ('confirmed', 'proposed')]
    openc = [c for c in mine if c['status'] == 'open']
    blank = [c for c in mine if c['status'] == 'blank']
    nums = sorted(c['number'] for c in mine)
    print(f"{sid}: {len(named)} cards ({sum(c['status']=='confirmed' for c in named)} confirmed, "
          f"{sum(c['status']=='proposed' for c in named)} proposed), {len(openc)} open, {len(blank)} blank; target {s['cards']}+{s['blank']}")
    if len(named) + len(openc) != s['cards']: bad(f'{sid}: {len(named)+len(openc)} numbered slots, expected {s["cards"]}')
    if len(blank) != s['blank']: bad(f'{sid}: {len(blank)} blanks, expected {s["blank"]}')
    if nums != list(range(1, len(mine) + 1)): bad(f'{sid}: numbers are not 1..{len(mine)} without gaps')
    for c in named:
        w = web[sid].get(c['id'])
        if not w: bad(f"{c['id']}: no web text"); continue
        if not w.get('summary') or not w.get('body'): bad(f"{c['id']}: summary or body missing")
        if 'steps' in w:
            if len(w['steps']) < 3 and c['id'] != 'risk-management': bad(f"{c['id']}: fewer than 3 steps")
        elif len(w.get('questions', [])) < 4: bad(f"{c['id']}: fewer than 4 questions")
        for r in w.get('related', []):
            if r not in real: bad(f"{c['id']}: related id '{r}' is not a card")
        if not c.get('card_text'): bad(f"{c['id']}: no card_text")
        elif c.get('card_text_status') == 'draft' and len(c['card_text'].split()) > 60: bad(f"{c['id']}: draft card_text over 60 words")
    for k in set(web[sid]) - {c['id'] for c in named}: bad(f'{sid}: web text for unknown card {k}')

txt = open('_data/cards.yml').read() + ''.join(open(f).read() for f in glob.glob('_data/web/*.yml'))
for pat in ['World Bank', 'Development Seed', 'DevSeed', 'hydrolog', 'watershed', 'ADA ', 'Santiago']:
    if pat.lower() in txt.lower(): bad(f'client-specific text found: {pat}')
# Stock-word check applies to drafted text only; Laura's own InDesign text is left as written.
drafted = ''.join(c.get('card_text') or '' for c in cards if c.get('card_text_status') != 'indesign') + ''.join(open(f).read() for f in glob.glob('_data/web/*.yml'))
for pat in [r'\bdelve\b', r'\btapestry\b', r'\blandscape\b', r'\bnavigate\b', r'\bnuanced\b', r'\brobust\b', r'\bleverage\b', r'\bgenuinely\b', r'\btruly\b', '—']:
    if re.search(pat, drafted, re.I): bad(f'stock word or dash found in drafted text: {pat}')

redir = [r for c in cards for r in c.get('redirect_from', [])] + [r['old_page'] for r in retired]
for r in {x for x in redir if redir.count(x) > 1}: bad(f'redirect source used twice: {r}')
covered = set(redir) | {c['old_site_page'] for c in cards if c.get('old_site_page')} | {c['path'] for c in cards if c.get('path')}
if os.path.isdir('cards'):
    for f in sorted(glob.glob('cards/*/*.md')):
        rel = f[:-3]
        if rel.endswith('/index'): continue
        if f'/{rel}/' not in covered: print(f'note: {f} has no card or redirect (stray file, safe to delete)')
print('done;', len(problems), 'problems')
sys.exit(1 if problems else 0)
