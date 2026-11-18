---
layout: card
title: Network resilience
card_id: network-resilience
description: How the system copes when the connection, the power or the hardware fails.
redirect_from:
- /cards/non-functional-requirements/network-resilience/
- /cards/non-functional-requirements/robustness/
- /cards/qualities/robustness/
---

# Network resilience

A system running in the real world will meet boundary conditions: the internet connection goes down, the power fails, a device breaks. Network resilience is its ability to handle those errors and conditions while it runs. A resilient system carries on where it can, fails safely where it cannot, and recovers without losing data.

## Questions to ask

- What happens when the connection drops in the middle of a task?
- What happens when the power fails, or a device breaks?
- Can people carry on with a fallback, such as paper or SMS?
- How does the system recover, and how do we know that it did?

## In a workshop

Walk through one key task and stop at each step to ask: what if it fails here?

## Related cards

- [Connectivity]({{ '/cards/context/connectivity/' | relative_url }})
- [Data integrity]({{ '/cards/qualities/data-integrity/' | relative_url }})
- [Performance]({{ '/cards/qualities/performance/' | relative_url }})
- [Maintainability]({{ '/cards/qualities/maintainability/' | relative_url }})
