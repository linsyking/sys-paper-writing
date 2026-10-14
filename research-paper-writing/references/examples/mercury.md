# Mercury: Abstraction and Design Space

Source: [SOSP 2025 publication](https://doi.org/10.1145/3731569.3764798); [public manuscript](https://par.nsf.gov/servlets/purl/10661231). Read §3 for overview, §§4–6 for representation/scheduling/tuning, §7 for implementation, and §8 for evaluation.

## Observed argument

Mercury represents remote GPU memory as part of an explicitly managed hierarchy through CommIR. This lets the compiler reason about data placement and communication together. The paper explains transformations and lowering, then evaluates operator behavior, model performance, and the explored design space separately.

## Reusable writing move

Explain what a new abstraction makes expressible and optimizable. Connect that expressiveness to legal execution and measured outcomes at the claimed level.

Illustrative frame:

> Existing [interface] hides [decision]. Exposing it in [representation] permits [transformation], subject to [dependence constraint]. We evaluate [local performance], [whole-model effect], and [search cost] separately.

## Review question

Do the claimed benefits include the communication, reshaping, and tuning costs needed to realize the generated schedules?
