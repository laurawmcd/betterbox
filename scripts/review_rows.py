"""Build the rows for the Google Sheet text review, one tab per suit (writes print/review_rows.json)."""
import yaml, json, glob, os
cards = yaml.safe_load(open('_data/cards.yml'))
web = {}
for f in glob.glob('_data/web/*.yml'):
    web.update(yaml.safe_load(open(f)) or {})
title = {c['id']: c['title'] for c in cards if c.get('title')}
TABS = [('values', 'Values'), ('people', 'People'), ('exercises', 'Exercises'),
        ('context', 'Context'), ('qualities', 'Qualities')]
HEAD = ['#', 'Title on the card', 'Status', 'Card text (printed)', 'Card text from',
        'Card text approved', 'Web summary', 'Web body', 'Questions or steps', 'Tips', 'Time',
        'In a workshop', 'Related cards', 'Web text approved', 'Your notes', 'Card ID (leave as is)']
SRC = {'indesign': 'Your InDesign file', 'draft': 'Claude draft'}
out = {}
for suit, tab in TABS:
    rows = [HEAD]
    for c in sorted((c for c in cards if c['suit'] == suit), key=lambda c: c['number']):
        if c['status'] == 'open':
            continue
        w = web.get(c['id'], {})
        blank = c['status'] == 'blank'
        qs = w.get('questions') or w.get('steps') or []
        num = '' if w.get('questions') else '{n}. '
        qtext = '\n'.join((f'{i}. ' if w.get('steps') else '• ') + q for i, q in enumerate(qs, 1))
        rows.append([
            c['number'], '' if blank else (c.get('deck_title') or c['title']), c['status'],
            (c.get('card_text') or '').strip(), SRC.get(c.get('card_text_status'), ''),
            False,
            '' if blank else w.get('summary', ''), '' if blank else (w.get('body') or '').strip(),
            qtext, '\n'.join('• ' + t for t in w.get('tips', [])), w.get('time', ''),
            w.get('use_it', ''), ', '.join(title.get(r, r) for r in w.get('related', [])),
            '' if blank else False, '', c['id']])
    out[tab] = rows
os.makedirs('print', exist_ok=True)
json.dump(out, open('print/review_rows.json', 'w'), ensure_ascii=False)
for t, r in out.items():
    print(t, len(r) - 1, 'rows')
