# ML Systems Lens for OSDI/SOSP

Use alongside the section being written. Select the relevant workload family; do not apply every item to every paper. The contribution should teach a systems lesson about resources, abstraction, coordination, programmability, correctness, or operation. A better model score alone does not explain the systems contribution.

## LLM and ML serving

**Objective.** Define request-level SLOs and the cost/resource budget. For autoregressive serving, distinguish time to first token (TTFT), average time per output token (TPOT), inter-token latency distribution, and total request latency. A good average TPOT can hide a visible stall between two tokens. Define endpoints and queueing explicitly.

**Workload.** Report model/weight version, precision, input/output length distributions, arrival process, burstiness, concurrency, prefix reuse and cache state. For multi-model systems, include popularity skew, model sizes, switching/loading costs, and autoscaling delay. Requests rejected, truncated, or unfinished at the end of a run need documented treatment.

**Mechanism.** Explain batching/admission, scheduling, KV-cache ownership/transfer/eviction, and coordination across prefill/decode or model instances. Count extra model replicas and memory, transfer traffic, CPU/storage costs, and interference introduced by overlap. Evaluate warm and cold cache conditions when cache benefits are central.

**Semantics and evidence.** Hold model quality and generation settings fixed for a performance-only claim. Quantization, approximate attention, cache approximation, speculation, or early stopping need a clear quality/correctness comparison. Test long/short and mixed contexts if breadth is claimed. Show throughput or goodput together with latency/SLO behavior under a load sweep.

Examples: [DistServe](examples/distserve.md) and [Strata](examples/strata.md).

## Distributed training and resource management

**Objective.** Distinguish iteration time, samples/tokens per second, time to a stated quality target, job completion time, and monetary cost. A faster iteration does not establish faster convergence.

**Protocol.** Report model, sequence length, global batch size, optimizer, numerical precision, gradient accumulation, parallelism degrees, checkpointing/recomputation, topology, and dataset/data order when relevant. Disclose changes in effective batch size, synchronization, dropped updates, or numerical semantics.

**Mechanism.** Explain partitioning, communication/computation overlap, straggler handling, placement, and memory peaks. For elastic/reliable systems, specify how parameters, optimizer state, data progress, and random state survive rescaling or recovery. Identify lost/duplicated work under the stated failure model.

**Evidence.** Separate planner/simulator accuracy from achieved execution performance. Include profiling/search time and reconfiguration/checkpoint/recovery costs when they affect the objective. Sweep relevant heterogeneity, bandwidth, skew, and scale. Label simulated large-cluster results; validate the model and state extrapolation limits.

Examples: [Sailor](examples/sailor.md) and [FuseLink](examples/fuselink.md).

## GPU runtimes, communication, and compilers

**Abstraction.** Explain what the runtime/compiler exposes and what prior interfaces hide. State legal transformations, data dependencies, ownership/synchronization, and hardware assumptions.

**Protocol.** Report operator shapes, model context, dtype/precision, device count, topology, memory, and backend/library versions. Match mathematical semantics and error tolerance. Separate compile/search/profiling cost from steady-state execution and discuss amortization.

**Evidence.** Compare against relevant tuned libraries/manual implementations and a simpler strategy. Show applicable shapes/topologies, memory usage, unsupported cases, regressions, and causal breakdowns. Operator speedups support operator claims; model-wide claims require evidence including cross-operator communication, layout changes, and synchronization.

Example: [Mercury](examples/mercury.md).

## Training reliability and diagnosis

**Contract.** Define the error/fault classes and the information available to the detector. Inferred invariants are conditional checks, not automatically universal semantic guarantees. Explain learning/checking separation and which valid configurations can violate a learned rule.

**Protocol.** Document bug/fault sourcing, reproduction, representativeness, and separation between rule-learning and evaluation cases. Include healthy executions and legitimate phase changes; fault cases alone do not establish false-positive behavior.

**Evidence.** Report detection coverage/recall, false alarms, detection delay, diagnosis usefulness, and runtime/storage overhead as separate outcomes. Count misses and state coverage limits. An absence of alarms is not proof that the training run was correct.

Example: [TrainCheck](examples/traincheck.md).
