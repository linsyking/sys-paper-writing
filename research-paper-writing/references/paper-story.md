# Build the Systems Paper Story

## Establish the thesis

Fill in: “For [workload] in [environment], existing [approach/assumption] causes [measured consequence]. Our insight is [reason a different design is possible]. We build/analyze [system or abstraction] to obtain [benefit] under [constraints], with [cost or boundary].”

An ML model's popularity is context, not the systems problem. Explain the resource mismatch, coordination issue, semantic requirement, or operational gap that matters beyond a single benchmark.

## Choose the contribution shape

| Paper type | Central contribution | Evidence to seek |
| --- | --- | --- |
| New design or abstraction | New organization, interface, mechanism, or policy with a reason it works | Implemented behavior, alternatives, end-to-end effects, costs |
| Measurement or diagnosis | A consequential observation that changes understanding or practice | Sampling method, confounders, validation, applicability limits |
| Correctness or verification | Precisely stated property under an explicit model | Definitions, invariants, proof/analysis, implementation connection |
| Operational experience | Transferable lessons from a real system and its evolution | Deployment context, observations, interventions, limitations |

Mix shapes when the actual work supports them. A valid contribution need not be a new neural network, outperform every baseline, or include three novel modules.

## Questions before outlining

- Who encounters the problem, at what scale, and with what operational consequence?
- What existing assumption fails? Which measurement or case exposes it?
- What is the closest competing design, including a simple practical alternative?
- Why does the insight remove the bottleneck rather than move it elsewhere?
- What implementation challenge makes the idea nontrivial to realize?
- What costs, guarantees, or workload boundaries change?
- What can a systems reader learn or reuse beyond this particular implementation?

## Working map

| Problem / observation | Insight | Design decision | Claim | Evidence / gap |
| --- | --- | --- | --- | --- |
| Concrete bottleneck with context | Explanation enabling a solution | Mechanism and rejected alternative | Scoped benefit or property | Existing figure/analysis or a proposed check |

Use this map to decide section order. A common design paper moves through Introduction, Background/Motivation, Design, Implementation, Evaluation, Discussion, Related Work, and Conclusion. Move Related Work or combine sections when that improves the argument. A measurement paper may foreground methodology and findings; a verification paper may introduce the model and property earlier.

## Avoid framing errors

Do not turn a list of optimizations into a contribution list without a unifying principle. Separate novel insight, engineering realization, and evidence. Do not inflate novelty by withholding implementation detail or suppressing the closest comparison. A limited but well-established claim is more credible than an unsupported broad claim.

For measurement-led problem framing, see [Strata](examples/strata.md). For an abstraction-led story, see [Mercury](examples/mercury.md). For heterogeneous resource planning, see [Sailor](examples/sailor.md).
