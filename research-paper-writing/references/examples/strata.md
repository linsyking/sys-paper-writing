# Strata: A Changed Bottleneck

Source: [OSDI 2026 paper](https://www.usenix.org/system/files/osdi26-xie-zhiqiang.pdf). Read §§1–3 for motivation, §4 for design/implementation, §5 for evaluation, and §6 for discussion.

## Observed argument

Hierarchical KV caching avoids recomputation but makes cache loading consequential. The paper connects fragmented transfers to low bandwidth utilization and connects scheduling decisions to remaining stalls. Its design combines a different transfer/layout approach with cache-aware scheduling. Evaluation includes end-to-end comparisons, component analysis, and different hardware environments.

## Reusable writing move

Explain why an established optimization exposes a new limiting resource. Separate the costs of data movement from the decisions that determine when movement blocks useful work.

Illustrative frame:

> [Optimization] reduces [old cost], but exposes [new bottleneck]. Improving [transfer] leaves [scheduling stall]. We coordinate [layout] and [policy] to address both.

## Review question

Does the evidence isolate each component's effect and show conditions in which the remaining bottleneck limits the gain?
