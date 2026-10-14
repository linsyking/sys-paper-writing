# Sailor: Planning and Execution Evidence

Source: [author's SOSP 2025 PDF](https://fotstrt.github.io/files/2025-sailor.pdf); [publication DOI](https://doi.org/10.1145/3731569.3764839). Read §3 for motivation, §4 for the system, and §§5.1–5.5 for evaluation.

## Observed argument

Resource availability motivates jointly choosing a cluster and a training configuration across heterogeneous environments. Sailor separates profiling, planning, simulation, and execution. Evaluation distinguishes simulator accuracy, plan quality, search scalability, optimization breakdowns, and reconfiguration overhead, using measured and simulated settings.

## Reusable writing move

Give each layer its own contract and evidence. A predicted fast configuration and a quickly executable configuration answer different questions.

Illustrative frame:

> [Planner] selects [configuration] using [prediction]. We validate that prediction against [measurements], then assess [execution objective], including [adaptation cost]. Results beyond [measured scale] use [validated simulation scope].

## Review question

Are the planner's recommendations validated independently of its simulator, and is the evidence labeled with its measured or simulated scope?
