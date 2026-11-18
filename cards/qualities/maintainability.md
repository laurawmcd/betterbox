---
layout: card
title: Maintainability
card_id: maintainability
description: Whether someone will be able to fix, update and run the system in the years after launch.
redirect_from:
- /cards/non-functional-requirements/maintainability/
---

# Maintainability

Most of a system's life comes after launch. Maintainability is about whether it can be understood, repaired and updated by people other than the ones who built it. Documentation, readable code, supported dependencies and a named person or team all matter.

## Questions to ask

- Who will fix and update this in two years, and are they aware of it yet?
- Is it documented well enough for someone new to pick up?
- Which dependencies could stop being supported?
- What does maintenance cost each year, and who pays?

## In a workshop

Ask the developer what they would need to hand over the system tomorrow. The gaps are the maintainability risks.

## Related cards

- [Developer]({{ '/cards/people/developer/' | relative_url }})
- [Administrator]({{ '/cards/people/administrator/' | relative_url }})
- [Build for sustainability]({{ '/cards/values/build-for-sustainability/' | relative_url }})
- [Licensing and copyright]({{ '/cards/qualities/licensing-copyright/' | relative_url }})
