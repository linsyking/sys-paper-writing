---
name: research-paper-writing
description: Draft, revise, and review computer systems research papers for OSDI/SOSP, especially ML systems for serving, distributed training, GPU runtimes, compilers, and reliability. Use for paper framing, section writing, design explanations, evaluation planning, claim-evidence checks, or reviewer-style critique.
---
# Systems Research Paper Writing

## Purpose

Help authors communicate a significant systems problem, the insight behind their solution, and credible evidence about its benefits and limits. Target OSDI/SOSP readers, including systems researchers unfamiliar with the particular ML workload. The installed name remains `research-paper-writing`.

## Start from the requested task

For a sentence or paragraph edit, preserve technical meaning and give the revision with a brief explanation. Flag material unsupported claims even in a small edit, and explain any change to claim strength. For a section, first establish its role in the paper. For a full draft or review, build a paper story and evidence map before polishing prose. Do not force a full-paper checklist onto a small edit.

Use the provided draft, measurements, design notes, and target venue/year. If essential information is missing, identify the gap; continue useful work with clearly marked placeholders. Never invent results, citations, hardware, deployment experience, or guarantees. Separate proposed experiments from completed experiments.

## Systems paper workflow

1. **Frame the problem.** Identify the workload, operating environment, objective, and important constraint. Explain the consequence of a bottleneck or broken assumption with measurements, a concrete case, or analysis.
2. **Find the insight.** Explain why existing approaches fall short and what changes in the proposed abstraction, mechanism, policy, or organization. State the contribution precisely, including which techniques are inherited.
3. **Explain the system.** Walk through a representative operation. Identify interfaces, state ownership, coordination, resource costs, and applicable correctness or failure assumptions. Explain consequential alternatives and tradeoffs.
4. **Match evidence to claims.** Use experiments for performance, analysis/proofs for guarantees, and observations for experience claims. Tests alone do not establish universal correctness. Scope each claim to the evidence actually available.
5. **Revise for readers.** Reverse-outline the section, keep terminology consistent, and make figures and captions independently interpretable.
6. **Review at the requested scope.** Identify the strongest remaining objection and whether it needs clearer writing, analysis, an experiment, or a narrower claim. A writing revision cannot substitute for missing research evidence.

These are writing aids, not a mandatory section order. Measurement, verification, and operational-experience papers may need different structures. OSDI/SOSP value insight and significance; avoid imposing an arbitrary number of contributions, baseline wins, datasets, or ablations.

## Load references selectively

Read the guide for the current edit. Add an adjacent guide only when it resolves a dependency.

| Task | Reference |
| --- | --- |
| Story, contribution, or whole-paper outline | [paper-story.md](references/paper-story.md) |
| Abstract | [abstract.md](references/abstract.md) |
| Introduction | [introduction.md](references/introduction.md) |
| Background and motivating measurements | [background.md](references/background.md) |
| Related Work | [related-work.md](references/related-work.md) |
| Design / Method | [method.md](references/method.md) |
| Implementation and artifact description | [implementation.md](references/implementation.md) |
| Evaluation / Experiments and figures | [experiments.md](references/experiments.md) |
| ML serving, training, compilers, or reliability | [mlsys.md](references/mlsys.md), alongside the relevant section guide |
| Discussion, limitations, and conclusion | [conclusion.md](references/conclusion.md) |
| Paragraph flow | [writing-flow.md](references/writing-flow.md) |
| Reviewer critique | [paper-review.md](references/paper-review.md) |
| Concrete writing patterns | [examples/index.md](references/examples/index.md); open the matching example only |
| Paper provenance or venue requirements | [sources.md](references/sources.md) |

## Constraints that matter

- Preserve actual novelty and acknowledge prior art. Explain even a small mechanism's significant insight; do not disguise incremental work with new names or hide a simple alternative.
- Distinguish empirical results, analytical conclusions, hypotheses, and operational observations. Keep unsupported promises out of final paper prose.
- State the comparison budget: hardware, resources, workload, configuration, and semantics. Faster execution under weaker consistency, lower model quality, or a larger budget is a different claim.
- Define metrics before interpreting them. Separate throughput, latency, tail latency, goodput, utilization, and monetary cost; they are not interchangeable.
- Discuss assumptions and failure behavior relevant to the system. Do not impose distributed fault tolerance on work whose scope does not include it.
- Put evidence essential to judging the contribution in the main paper. Supplements can carry supporting detail.
- Treat the paper examples as editorial observations, not official acceptance rules. Check the actual venue/year/track instructions when asked about submission requirements; do not reuse a past edition's limits or policies as current facts.

## Output appropriate to scope

For section drafting or a substantial rewrite, return:

1. A compact outline or paragraph-role map.
2. Revised prose; put role labels outside publication-ready paragraphs.
3. A short list of consequential changes and unresolved facts.
4. A claim-evidence table when substantive claims are added or changed.

Use this evidence schema for substantive drafting, evaluation planning, or review:

| Claim and scope | Evidence type | Evidence locator or proposed check | Status / action |
| --- | --- | --- | --- |
| Specific claim under stated conditions | Measurement / analysis / proof / experience | Figure, table, section, supplied data, or clearly proposed experiment | Supported / partial / needs evidence; revise or gather evidence |

For evaluation planning, give prioritized questions, comparisons, metrics, and controls, without presenting anticipated gains as results. For a full-paper review, prioritize objections by their effect on the paper's claims and state what would resolve each one. Report unresolved issues honestly; do not promise acceptance or imply that every concern has been eliminated.
