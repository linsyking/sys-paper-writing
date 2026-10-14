# Background and Motivation

## Give only the background the design needs

Introduce the relevant execution model, resource hierarchy, existing interface, or correctness model. Define terms at first use. Separate established facts, cited prior results, and new observations collected for this paper.

For an ML system, a useful background paragraph might explain prefill versus decode, collective communication, optimizer state, or compiler transformations. Do not turn the section into an ML tutorial when only one concept drives the design.

## Write a motivating measurement

Provide:

1. The question and the existing design being measured.
2. Hardware/software, workload, input sizes, and method sufficient to interpret the result.
3. The observation, with magnitude and variability when available.
4. The causal explanation supported by the experiment or analysis.
5. The design implication and limits of the observation.

A synthetic workload can isolate a cause; a trace can establish relevance. Label each accurately. If a dataset has no arrival timestamps, adding generated arrivals creates a synthetic arrival process, not a production request trace.

## Distinguish symptom from cause

High latency is a symptom. Waiting behind long work, a bandwidth limit, coordination overhead, or memory pressure may be the cause. Compare an isolated mechanism, change the proposed causal factor, or provide an execution breakdown. Correlation between utilization and latency alone does not establish causality.

## Alternatives and opportunity

Discuss the strongest natural response: larger batches, more replicas, a different placement, a larger cache page, or a simpler scheduler. Show the relevant constraint or tradeoff. An idealized upper bound can identify headroom, but label which costs and constraints it omits.

## Figure pattern

Caption: “[Metric] for [existing design] under [workload] on [hardware]. Changing [controlled variable] exposes [observation]. [Important omitted cost or uncertainty].”

Keep the figure's observation separate from a general claim about every workload or platform. For a measured I/O bottleneck and layout tradeoff, see [Strata](examples/strata.md). For a topology-dependent imbalance, see [FuseLink](examples/fuselink.md).
