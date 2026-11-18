#!/usr/bin/env python3
"""Build the site's card list and card pages from the card data.

Reads  _data/cards.yml, _data/suits.yml, _data/retired.yml and _data/web/<suit>.yml
Writes _data/deck.yml (what the drawn cards and suit pages use) and cards/<suit>/<id>.md
       for every confirmed or proposed card. Card pages that no longer have a card are deleted;
       their addresses redirect to the card that replaced them.

Run from the repo root:
    python3 scripts/build_pages.py           # dry run: says what it would change
    python3 scripts/build_pages.py --write   # writes the files
"""
import glob, os, sys, yaml

WRITE = '--write' in sys.argv
OLD_SUIT_NAMES = {'users': 'people', 'facilitation-design': 'exercises',
                  'practicalities': 'context', 'non-functional-requirements': 'qualities'}

cards = yaml.safe_load(open('_data/cards.yml'))
suits = yaml.safe_load(open('_data/suits.yml'))
retired = yaml.safe_load(open('_data/retired.yml')) or []
web = {s['id']: yaml.safe_load(open(f"_data/web/{s['id']}.yml")) or {} for s in suits}
old_deck = {s['folder']: s for s in yaml.safe_load(open('_data/deck.yml'))}
by_id = {c['id']: c for c in cards}
named = [c for c in cards if c['status'] in ('confirmed', 'proposed')]
new_paths = {c['path'] for c in named}


def current_name(path):
    """The same address with the suit's current folder name."""
    parts = path.split('/')
    if len(parts) > 2 and parts[2] in OLD_SUIT_NAMES:
        parts[2] = OLD_SUIT_NAMES[parts[2]]
    return '/'.join(parts)


def front_matter(path):
    if not os.path.exists(path):
        return {}
    text = open(path).read()
    if not text.startswith('---'):
        return {}
    return yaml.safe_load(text.split('---')[1]) or {}


# Redirects: each card's own list, plus retired pages, each also under the current suit names,
# plus whatever the existing page file already redirects.
redirects = {c['id']: set() for c in named}
for c in named:
    for r in c.get('redirect_from', []):
        redirects[c['id']].update([r, current_name(r)])
for r in retired:
    target = r['redirect_to'].strip('/').split('/')[-1]
    if target in redirects:
        redirects[target].update([r['old_page'], current_name(r['old_page'])])
for c in named:
    fm = front_matter(f"cards/{c['suit']}/{c['id']}.md")
    redirects[c['id']].update(fm.get('redirect_from', []))
    redirects[c['id']] -= new_paths

# _data/deck.yml
BLANK_TEXT = {'people': 'Add a person or group of your own',
              'exercises': 'Add an exercise of your own',
              'context': 'Add a piece of context of your own',
              'qualities': 'Add a quality of your own',
              'values': 'Add a value of your own'}
deck = []
for s in suits:
    look = old_deck.get(s['id'], {})
    entry = {'folder': s['id'], 'name': s['title'], 'color': look.get('color', '#A7166A'),
             'pip': look.get('pip', 'circle'), 'deck_size': s['cards'] + s.get('blank', 0), 'cards': []}
    for c in sorted((c for c in cards if c['suit'] == s['id']), key=lambda c: c['number']):
        if c['status'] in ('confirmed', 'proposed'):
            w = web[s['id']].get(c['id']) or {}
            e = {'number': c['number'], 'title': c['title'], 'slug': c['id']}
            if w.get('summary'): e['summary'] = w['summary']
            if c.get('card_text'): e['face'] = c['card_text']
            if c['status'] == 'proposed': e['proposed'] = True
        else:  # blank card, or a slot with no card chosen: left blank for people to write their own
            e = {'number': c['number'], 'title': 'Blank card', 'blank': True,
                 'summary': BLANK_TEXT.get(s['id'], 'Write your own card')}
        entry['cards'].append(e)
    deck.append(entry)

header = ('# Built by scripts/build_pages.py from _data/cards.yml, _data/suits.yml and _data/web/. Edit those, not this.\n'
          '# deck_size: cards in the printed suit, blank included. face: the printed card text. proposed: card not yet confirmed.\n'
          '# blank: left blank for workshop participants to write their own (blank cards and unfilled slots).\n')
deck_text = header + yaml.dump(deck, allow_unicode=True, sort_keys=False, width=120)


# Card pages
def page(c):
    w = web[c['suit']].get(c['id']) or {}
    fm = {'layout': 'card', 'title': c['title'], 'card_id': c['id']}
    if w.get('summary'): fm['description'] = w['summary']
    if redirects[c['id']]: fm['redirect_from'] = sorted(redirects[c['id']])
    out = ['---', yaml.dump(fm, allow_unicode=True, sort_keys=False, width=1000).strip(), '---', '',
           f"# {c['title']}", '']
    if c['status'] == 'proposed':
        out += ['*This card is proposed for the next version of the deck.*', '']
    if w.get('body'): out += [w['body'].strip(), '']
    if w.get('time'): out += [f"**Time:** {w['time']}", '']
    if w.get('steps'):
        out += ['## How to run it', ''] + [f"{i}. {x}" for i, x in enumerate(w['steps'], 1)] + ['']
    if w.get('tips'):
        out += ['## Tips', ''] + [f"- {x}" for x in w['tips']] + ['']
    if w.get('questions'):
        out += ['## Questions to ask', ''] + [f"- {x}" for x in w['questions']] + ['']
    if w.get('use_it'):
        out += ['## In a workshop', '', w['use_it'].strip(), '']
    dp = c.get('digital_principle') or w.get('digital_principle')
    if isinstance(dp, dict) and dp.get('url'):
        out += [f"This card matches one of the nine [Principles for Digital Development]({dp['url']}).", '']
    rel = [by_id[r] for r in w.get('related', []) if r in by_id and by_id[r]['status'] in ('confirmed', 'proposed')]
    if rel:
        out += ['## Related cards', ''] + [f"- [{r['title']}]({{{{ '{r['path']}' | relative_url }}}})" for r in rel] + ['']
    return '\n'.join(out)


pages = {f"cards/{c['suit']}/{c['id']}.md": page(c) for c in named}
leftover = [f for f in sorted(glob.glob('cards/*/*.md'))
            if not f.endswith('index.md') and f not in pages]

# Every address the site used before must still lead somewhere.
covered = set(new_paths)
for r in redirects.values():
    covered |= r
lost = ['/' + f[:-3] + '/' for f in leftover if '/' + f[:-3] + '/' not in covered]

changed = [p for p, t in pages.items() if not os.path.exists(p) or open(p).read() != t]
print(f"{len(pages)} card pages ({len(changed)} new or changed), {len(leftover)} old pages to delete")
for f in leftover: print('  delete', f)
if lost:
    print('Old addresses with no redirect (fix before writing):')
    for u in lost: print('  ', u)
    sys.exit(1)
if WRITE:
    open('_data/deck.yml', 'w').write(deck_text)
    for p, t in pages.items():
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w').write(t)
    for f in leftover: os.remove(f)
    print('Written.')
