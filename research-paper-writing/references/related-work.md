# Related Work in a Systems Paper

## Position the contribution by mechanism

Organize around the nearest design decisions or assumptions: scheduling versus disaggregation, memory placement versus caching, explicit communication versus collective APIs, or testing versus invariant checking. Use publication chronology only when it explains a changed assumption.

For each cluster, describe the common approach, its intended setting, and the specific relation to this paper. A difference is not automatically a deficiency. Do not dismiss a system for an objective or workload it did not target.

## Comparison matrix

| Prior system | Objective and scope | Assumptions / mechanism | Relationship to this work | Evaluation comparison |
| --- | --- | --- | --- | --- |
| Verified citation and version | What it optimizes or guarantees | Hardware, workload, semantics | Borrowed idea, changed interface, or distinct tradeoff | Included, inapplicable with reason, or missing |

Check the closest predecessor, strongest current competitor, and simplest credible approach. A reused mechanism should be credited where it enters Design, not only in Related Work. Feature tables complement explanation; unsupported checkmarks do not establish novelty.

## Paragraph pattern

> [Research line] addresses [objective] through [mechanism]. [Representative works] assume or target [setting]. Our work shares [borrowed principle], but addresses [different bottleneck/contract] through [precise change]. Under [conditions], this changes [tradeoff], which we evaluate in [locator].

Read the cited paper before making a technical limitation claim. If its contents or relevant version are unavailable, mark the comparison as unverified. Do not invent citations or claim “first” from a small example corpus. Literature updates require current primary sources; the historical examples in [sources.md](sources.md) are writing references, not a complete baseline survey.
