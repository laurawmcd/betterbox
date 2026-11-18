---
layout: card
title: Security
card_id: security
description: How data is protected, in storage, in transit and against unauthorized access.
redirect_from:
- /cards/non-functional-requirements/security/
---

# Security

Security asks what needs protecting, from whom, and what a breach would cost the people involved. Decide whether data must be encrypted in the database, whether it must be encrypted when it moves between systems, and what authentication people need when they reach the system remotely.

## Questions to ask

- Does the data need to be encrypted in the database?
- Is it encrypted when it travels between internal systems?
- What authentication do people need to access it remotely?
- What would a breach cost the people whose data we hold?

## In a workshop

Use it alongside Threat modeling. Take each asset from the threat map and ask how it is protected.

## Related cards

- [Threat modeling]({{ '/cards/exercises/threat-modeling/' | relative_url }})
- [Data subject]({{ '/cards/people/data-subject/' | relative_url }})
- [Establish people-first data practices]({{ '/cards/context/people-first-data-practices/' | relative_url }})
- [Data integrity]({{ '/cards/qualities/data-integrity/' | relative_url }})
