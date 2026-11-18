"""Write print/data-merge.csv for InDesign Data Merge from _data/cards.yml.

One row per card in deck order. Blank cards get an empty title and text.
Open slots are skipped. Use --approved-only once cards have been approved.
Paragraphs go in body_1..body_3; turn on "Remove blank lines for empty fields" in Data Merge options.
"""
import csv, sys, yaml, os
BASE = 'betterbox.tech'   # change here if the site moves to its own domain
BACK = {'people': 'People', 'exercises': 'Exercises', 'context': 'Context',
        'qualities': 'Qualities', 'values': 'Values'}
ORDER = list(BACK)
cards = yaml.safe_load(open('_data/cards.yml'))
only_approved = '--approved-only' in sys.argv
rows = []
for c in sorted(cards, key=lambda c: (ORDER.index(c['suit']), c['number'])):
    if c['status'] == 'open':
        continue
    if only_approved and not c.get('card_text_approved'):
        continue
    paras = (c.get('card_text') or '').split('\n\n')
    if len(paras) > 3:
        sys.exit(f"{c['id']}: more than 3 paragraphs")
    paras += [''] * (3 - len(paras))
    blank = c['status'] == 'blank'
    rows.append({
        'id': c['id'], 'suit': BACK[c['suit']], 'number': c['number'],
        'title': '' if blank else c.get('deck_title') or c['title'],
        'body_1': paras[0], 'body_2': paras[1], 'body_3': paras[2],
        'url': '' if blank else BASE + c['path'].rstrip('/'),
        'back_label': BACK[c['suit']],
        'status': c['status'], 'text_source': c.get('card_text_status') or '',
        'approved': 'yes' if c.get('card_text_approved') else 'no',
    })
os.makedirs('print', exist_ok=True)
out = 'print/data-merge.csv'
with open(out, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
print(f'{len(rows)} rows -> {out}')
