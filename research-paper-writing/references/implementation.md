# Implementation and Reproducibility

## Explain what was actually built

Describe the prototype's integration points, modified versus reused components, and supported configurations. Include engineering details that determine whether the design works: execution hooks, data layout, synchronization, memory allocation, transport, or fallback behavior. Lines of code can indicate integration effort, but are not evidence of novelty or correctness.

Keep essential mechanisms in Design. Put realization-specific details here. Do not move a crucial algorithm, safety assumption, or main evaluation protocol into a supplement merely to shorten the paper.

## Distinguish the scopes of evidence

Use precise labels: implemented prototype, simulation, emulation, trace replay, pilot deployment, or production deployment. Explain which claims each supports. A production workload replay does not establish that the system itself ran in production.

## Information an evaluator needs

- Hardware model/count, memory capacity, interconnect topology and bandwidth, CPU/storage resources when relevant.
- OS, drivers, framework/compiler/runtime versions, baseline versions or commits, and important configuration differences.
- Workload/model versions, preprocessing, precision, context lengths, batch sizes, parallelism, and datasets or trace provenance.
- Commands and configurations to regenerate principal results, raw measurements, plotting/aggregation procedure, and expected variation.
- Required privileges, nonpublic data/hardware dependencies, unsupported features, and substitutes with clearly narrower claims.

For simulation, explain calibration and validation against measured executions, prediction error, and unvalidated scale or configurations. For a hardware-limited prototype, acknowledge the limitation and justify the bounded conclusion.

## Artifact description

When writing an artifact appendix, give a minimal working path and a map from paper figures to scripts/configuration/output. Distinguish available, functional, and reproduced claims rather than treating a repository link as proof of all three. Check the chosen year's artifact instructions through [sources.md](sources.md) when needed.

When a draft lacks implementation facts, mark them as missing; do not infer a software version, deployed scale, or reproducibility result from another paper's example. See [Sailor](examples/sailor.md) for keeping measured and simulated evaluations distinguishable.
