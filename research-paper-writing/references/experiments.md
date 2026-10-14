# Systems Evaluation / Experiments

## Begin with questions, not a benchmark list

Map each major claim to the evidence needed to establish it. Choose only experiments relevant to those claims; no fixed number of baselines, datasets, or ablations establishes completeness.

| Claim | Question | Evidence and control |
| --- | --- | --- |
| End-to-end benefit | Does the complete system improve the intended objective? | Relevant baseline, same semantics and workload, explicit resource budget |
| Mechanism explains gain | Which decision removes the bottleneck? | Valid remove/replace variant, simple alternative, breakdown, or controlled perturbation |
| Scalability | How does behavior change with scale? | Resource/load sweep, normalized efficiency, saturation point |
| Adaptation | How does it respond to changing conditions? | Time series, transition overhead, bursts/preemption/skew |
| Low overhead | What does the system add when benefit is small? | CPU/GPU/memory/network costs and unfavorable regimes |
| Reliability/correctness | What properties and failures are covered? | Stated model, proof/analysis where needed, fault/bug cases, misses and false alarms |
| Practical value | Does the design fit its intended environment? | Integration evidence, operational observations, limits, reproducibility |

See [mlsys.md](mlsys.md) for serving, training, compiler, and reliability-specific controls.

## State the protocol before results

Describe hardware/topology; software/baseline versions; workload construction; parameter choices; resource budgets; metrics; warm-up and measurement windows; and repetition/uncertainty appropriate to the experiment. Report whether requests are open-loop arrivals or closed-loop clients. Closed-loop load reduces submissions during stalls and can mask queueing tails; explain why the model fits the target service.

For traces, give provenance, sampling, anonymization or transformations, and what was retained. Separate measured executions, simulations, extrapolations, and production observations. Validate a simulator before relying on its large-scale predictions.

## Fair comparisons

Use the strongest relevant public systems and a practical simple alternative. Cite versions and explain tuning effort and important feature differences. A historical baseline in an example is not necessarily a current competitor.

Align hardware type/count, memory/network budget, input mix, output length, precision/quality, consistency, and correctness assumptions where the question requires equivalence. If a design intentionally uses a different resource mix, compare cost/performance or a justified budget and disclose the difference. Do not quietly substitute an impoverished baseline or omit failed/OOM configurations.

## Define metrics precisely

- Throughput: completed work per unit time; distinguish requests, tokens, samples, and iterations.
- Latency: endpoint timestamps, included queueing, percentile, and population. A ratio of latencies is not a percentage reduction.
- Goodput: specify the useful-completion predicate, measurement window, admission/drop policy, and normalization. Distinguish compliant completions per second from maximum sustainable arrival rate at a target SLO attainment; different papers use different definitions.
- SLO attainment: define numerator/denominator and whether every required latency constraint must pass for one request. Include rejected, timed-out, and unfinished requests appropriately so admission cannot inflate service quality.
- Cost/efficiency: define denominator, hardware/time/pricing assumptions, and communication or idle-resource costs. GPU utilization alone does not establish cost savings.

Avoid averaging percentiles across runs or hiding tails in mean latency. Explain how repeated runs or samples are combined. Identify maximum, median, arithmetic mean, and geometric mean correctly; do not turn an “up to” gain into an average.

## Write each result as an argument

State the question → describe the comparison → report the scoped observation → explain the mechanism → acknowledge a boundary. A curve is not self-explanatory. Include neutral or negative results when they change the design's applicability.

Ablations should preserve a valid system. If disabling a component changes semantics or makes execution impossible, use a meaningful alternative or another form of evidence and explain the choice. Measure component interactions when the claim depends on them. Pair microbenchmarks with application results before asserting end-to-end benefit.

## Figures and tables

Give axes units, workload/model, resource count, baseline identity, metric direction, and uncertainty when relevant. Show load/latency or SLO curves when a single operating point conceals a tradeoff. Label simulated results and distinguish offered load from achieved throughput. Captions should identify the setting and the takeaway without claiming more than the figure shows.

Prefer readable typography, consistent precision, sparse table rules, and encodings that remain distinguishable in grayscale. Follow the actual venue/template's caption and layout conventions; a right-column placement or decorative teaser is not a universal rule. Do not manipulate axes or aggregate away regressions.

## Prioritize missing evidence

Label each gap as essential to the central claim, helpful for mechanism understanding, or optional breadth. Recommend the smallest experiment/analysis that resolves a consequential uncertainty. If it cannot be run, narrow the claim rather than writing the result as though it exists.

Examples: [DistServe](examples/distserve.md) for SLO-aware objectives, [FuseLink](examples/fuselink.md) for microbenchmarks plus applications, [TrainCheck](examples/traincheck.md) for detection quality, [Sailor](examples/sailor.md) for simulator validation, and [Mercury](examples/mercury.md) for scoped compiler evaluation.
