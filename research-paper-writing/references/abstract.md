# Abstract for a Systems Paper

## What a reader should learn

Communicate the operational problem, the insight, what was built or learned, and the strongest scoped evidence. Explain the system in ordinary systems terms before relying on its name.

## Design-paper pattern

1. Workload and important objective or constraint.
2. Existing assumption or bottleneck and its consequence.
3. Insight and the system that realizes it.
4. One or two mechanisms essential to understanding the insight.
5. Evidence with the comparison, resource budget, metric, and setting needed to interpret it.
6. A boundary or cost if omitting it would materially mislead.

Illustrative skeleton; brackets are missing author-supplied facts:

> [Workload] must meet [objective] within [resource/semantic constraint]. Existing [approach] suffers from [bottleneck] because [reason]. We present [system], which [core insight and mechanism]. Our implementation [integration scope]. Under [workload and budget], it improves [defined metric] by [measured result] relative to [baseline], while [important tradeoff or guarantee].

Do not insert a numerical gain until the author supplies evidence. “Up to” denotes a maximum, not a typical result. Avoid unexplained ranges pooled across unrelated metrics or baselines.

## Other contribution shapes

For measurement work: problem → what was measured and how → principal finding → systems implication. For verification: problem → property and model → technique → applicability and implementation evidence. For experience: operational setting → consequential challenge → intervention/lesson → observed outcome and scope. Do not force a speedup sentence into these papers.

## Review

- Can a nonspecialist systems reader identify the actual contribution?
- Does each result use the same metric, conditions, and denominator as the evaluation?
- Is a local optimization described as local, rather than a system-wide gain?
- Are approximate computation, changed training semantics, or narrower failure assumptions visible when material?
- Does the abstract avoid claiming universal correctness from tests?

See [DistServe](examples/distserve.md) for an objective-led abstract and [TrainCheck](examples/traincheck.md) for reliability-oriented evidence.
