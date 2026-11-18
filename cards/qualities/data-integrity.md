---
layout: card
title: Data integrity
card_id: data-integrity
description: How much loss, corruption or duplication of data the project can tolerate.
redirect_from:
- /cards/non-functional-requirements/data-integrity-card/
- /cards/non-functional-requirements/data-integrity/
---

# Data integrity

Some records must be exact, such as a case file or a payment. Others can be approximate. Data integrity is about deciding how much loss, corruption or duplication you can tolerate, and how you would notice a problem when it happens.

## Questions to ask

- Which records must be exact, and which can be approximate?
- What happens if a record is lost, changed or duplicated?
- How would we notice?
- Who is affected when the data is wrong, and how can they correct it?

## In a workshop

Choose one type of record and ask the group to describe the worst plausible data error and its consequences.

## Related cards

- [Network resilience]({{ '/cards/qualities/network-resilience/' | relative_url }})
- [Security]({{ '/cards/qualities/security/' | relative_url }})
- [Data subject]({{ '/cards/people/data-subject/' | relative_url }})
- [Interoperability]({{ '/cards/qualities/interoperability/' | relative_url }})
