---
layout: card
title: Interoperability
card_id: interoperability
description: Whether the system follows industry standards and can exchange data with others.
redirect_from:
- /cards/non-functional-requirements/interoperability/
---

# Interoperability

Interoperability asks which industry output standards the system should follow, whether it has APIs, and whether it is part of a larger system. Systems that cannot exchange data end up with people re-entering it by hand, which costs time and adds errors.

## Questions to ask

- What other systems does this one need to exchange data with?
- Which standards do they use?
- Does our system offer an API, and to whom?
- Who else might want to connect to it later?

## In a workshop

Draw the system in the middle of a page and add every other system it touches, with an arrow for each data flow.

## Related cards

- [Share, reuse and improve]({{ '/cards/values/share-reuse-improve/' | relative_url }})
- [Create open and transparent practices]({{ '/cards/values/open-transparent-practices/' | relative_url }})
- [Data integrity]({{ '/cards/qualities/data-integrity/' | relative_url }})
