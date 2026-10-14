# Paragraph Flow for Systems Readers

## Reverse-outline the argument

Write the section's purpose, each paragraph's main message, and the evidence/explanation supporting that message. Check that each paragraph advances the purpose and each detail supports its paragraph. Split paragraphs with independent messages; remove repetition or supply the missing logical step.

## Check reader dependencies

Introduce a workload, resource, term, symbol, or metric before relying on it. Keep system/component names stable. A systems reader should understand why a detail is necessary: it explains a bottleneck, a decision, execution, a property, or a result.

Prefer an informative opening sentence. “We implement three components” signals structure; “Separating admission from execution lets the scheduler enforce the latency budget” explains a design purpose. Do not require every paragraph to follow an identical sentence template.

## Relationships between sentences

Make the link concrete: cause, consequence, contrast, condition, refinement, or evidence. Transition words cannot repair a missing causal argument. For a difficult mechanism, walk through an operation before returning to a general claim.

## Final pass

- Can readers distinguish an observation from its explanation?
- Can they identify the conditions of a performance claim or guarantee?
- Is “it” or “this” tied to an unambiguous object or result?
- Are latency, throughput, goodput, and utilization used consistently?
- Does the last sentence advance the argument rather than repeat the opening?

This guide preserves the original package's reverse-outlining approach in newly written systems-focused guidance; it does not reproduce the previously bundled external PDF text.
