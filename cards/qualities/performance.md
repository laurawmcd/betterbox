---
layout: card
title: Performance
card_id: performance
description: How fast the system needs to be, and what slowness or downtime costs.
redirect_from:
- /cards/non-functional-requirements/performance/
---

# Performance

*This card is proposed for the next version of the deck.*

Performance covers latency, speed and the cost of downtime. What counts as acceptable depends on the people using it: a delay that annoys a desk worker may make the system useless on a poor connection, and an outage that is an inconvenience in one setting may put people at risk in another.

## Questions to ask

- How quickly does each key task have to complete?
- What do users' connections and devices allow?
- What does an outage cost, and who bears it?
- What happens at peak use?

## In a workshop

Pick the most time-critical task and ask what the longest acceptable wait would be, then check it against the connection.

## Related cards

- [Connectivity]({{ '/cards/context/connectivity/' | relative_url }})
- [Network resilience]({{ '/cards/qualities/network-resilience/' | relative_url }})
- [Design for scale]({{ '/cards/context/design-for-scale/' | relative_url }})
