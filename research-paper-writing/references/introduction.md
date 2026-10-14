# Introduction for OSDI/SOSP

## Argument to establish

Lead readers from an important systems problem to a defensible insight, then explain the proposed system and what the paper establishes. Use [paper-story.md](paper-story.md) if the contribution itself is unclear.

## Useful paragraph roles

| Role | What to establish |
| --- | --- |
| Setting and stakes | Workload, deployment environment, objective, and practical consequence |
| Evidence of the problem | A measurement, case, or analysis showing the limitation of an existing approach |
| Root cause | Why the existing abstraction, resource organization, or assumption creates that limitation |
| Insight | Why a different organization or mechanism can address the cause |
| Realization and challenges | What the system changes, how it works at a useful level, and the nontrivial costs it must manage |
| Evidence and contributions | What was implemented or studied, principal scoped findings, and transferable contributions |

These are roles, not a prescribed paragraph count. Define specialist ML concepts only to the extent required for the systems argument. Introduce latency targets, memory limits, or consistency constraints early if they drive the design.

## A concrete transition

> Existing [approach] optimizes [local objective], but [measured case] shows that [system objective] remains limited by [cause]. We observe that [insight]. This suggests [design direction], provided that [new cost/challenge] can be controlled. Our system addresses that challenge through [mechanism], enabling [scoped benefit].

A simple alternative is useful when it exposes the real challenge. Explain why it is insufficient in the target setting; do not hide it to make the contribution seem less incremental.

## Contribution statements

Use statements such as:

- An observation about [bottleneck] established through [method and scope].
- An abstraction or mechanism that [specific capability], with [key insight].
- An implemented system showing [benefit and cost] under [conditions].
- An operational lesson about [decision] supported by [experience].

Avoid counting standard components as separate novelties. Identify what is borrowed and what changes. A component list is useful architecture information, but does not itself establish contribution.

## The first figure

A motivating measurement can make the problem concrete; an architecture sketch can make the insight legible. Choose the figure that resolves the reader's main uncertainty. Label the measurement setting or the important interfaces and resource boundaries. A decorative teaser is not a requirement.

## Check the introduction against the evaluation

For every prominent claim, locate its evidence and retain its scope. Keep typical improvements distinct from best-case gains. Explain disadvantages that materially change the interpretation. End with a roadmap only if it helps the reader navigate the argument.

Examples: [DistServe](examples/distserve.md) connects a serving objective to interference; [Sailor](examples/sailor.md) connects resource availability to planning; [Strata](examples/strata.md) motivates a changed bottleneck with measurements.
