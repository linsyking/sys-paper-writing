# System Design / Method

## Begin with the contract

State the system's inputs, externally visible behavior, objective, and assumptions. List relevant limits: workload knowledge, hardware features, consistency, failure model, or numerical semantics. Explain what the design guarantees and what it merely optimizes empirically.

## Overview before mechanisms

Use an architecture diagram and a representative request, iteration, or operation. Identify components, interfaces, state ownership, and the flow of data and decisions. Distinguish control-plane decisions from work on the critical path. Where useful, show placement across process, host, GPU, or trust boundaries.

A common arrangement is goals/assumptions → overview → mechanisms → correctness/failure handling → implementation. Combine or reorder these when the reader's dependencies require it.

## Explain each consequential design choice

| Question | Content to supply |
| --- | --- |
| Why is it needed? | Bottleneck, conflicting goals, or semantic obligation |
| How does it work? | Inputs, state, decision rule, ordered actions, outputs |
| Why this choice? | Reasoning and comparison with a plausible alternative |
| What must remain true? | Invariant, ordering rule, resource bound, or numerical constraint |
| What does it cost? | Communication, memory, metadata, synchronization, tuning, or complexity |
| Where does it stop helping? | Workload, hardware, or failure boundary |

Do not mechanically repeat this table for every trivial helper. Use it to find missing explanations in important mechanisms.

## Make the execution inspectable

For scheduling, specify what is measured or predicted, the decision interval, the objective, admission and queue behavior, tie-breaking/fairness when relevant, and how decisions are enforced. For caching, specify keys, ownership, sharing, invalidation, eviction, and transfer completion. For compilers, specify the abstraction, legal transformations, dependence constraints, lowering, and search space.

Use pseudocode when it clarifies a decision rule. Define symbols and units before an equation. An optimization objective needs constraints and a description of how its solution affects execution.

## Correctness and failure behavior

Choose obligations appropriate to the paper. Explain concurrency and state transitions that can violate the contract: migration while a request runs, stale metadata, retries after partial completion, or reconfiguration during a training iteration. State failure assumptions and recovery behavior if resilience is claimed. If the system requires reliable nodes, say so rather than inventing recovery support.

A proof should connect its abstract model to the implemented mechanism. Empirical tests can expose bugs and validate particular cases; they do not prove a universal safety guarantee. Learned invariants or heuristics require stated applicability conditions.

## Tradeoffs belong in the design

Disaggregation may add communication. Overlap may add buffering or interfere with foreground work. Aggressive batching may harm latency. Faster training may change numerical behavior. Explain why the chosen compromise fits the intended setting, then direct readers to the evaluation that measures it.

See [DistServe](examples/distserve.md) for decoupling with placement costs, [Mercury](examples/mercury.md) for an abstraction exposing a design space, and [TrainCheck](examples/traincheck.md) for preconditions on inferred checks.
