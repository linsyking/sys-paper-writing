# Discussion, Limitations, and Conclusion

## Discussion explains applicability

Address boundaries that change deployment or interpretation: hardware dependence, workload skew, unavailable information, resource overhead, quality/consistency tradeoffs, failure coverage, or unsupported features. Distinguish an architectural limitation from an implementation limitation, and report both when they matter.

Do not hide a fixable defect solely because it makes the story less polished. Do not imply a fix is complete because it is easy to imagine. Explain a proposed extension as future work, including the unresolved challenge.

For a measurement paper, discuss sampling and generalization. For a simulation-heavy paper, identify unvalidated conditions. For an operational paper, distinguish observations and interventions from causal experiments and explain what transfers to another deployment.

## Conclusion closes the established argument

Restate the problem, core systems insight, and strongest supported outcome. Say what readers can reuse or learn. Do not add a new guarantee, unreported deployment, or unsupported generalization in the final paragraph.

Illustrative skeleton:

> [System/study] addresses [problem] through [insight]. Under [evaluated scope], [evidence] establishes [benefit or finding], with [important cost/boundary]. These results suggest [transferable implication]. Extending the approach to [new setting] requires addressing [unresolved challenge].

A future-work sentence is optional. It is more useful to state a concrete boundary than to promise broad applicability. Keep limitations consistent across Abstract, Introduction, Design, and Evaluation.
