# FuseLink: Mechanism to Application

Source: [OSDI 2025 paper](https://www.usenix.org/system/files/osdi25-ren.pdf). Read §§2–4 for topology/challenges/design, §5 for integration, §6 for evaluation, and §7 for limits.

## Observed argument

Static GPU–NIC bindings leave spare network capacity inaccessible to a busy GPU under imbalanced traffic. The design uses intra-server paths to relay traffic through additional NICs and addresses interference and contention. Evaluation separates communication microbenchmarks from serving and training applications, and reports control overhead.

## Reusable writing move

Show which resource is stranded, how a path exposes it, and what new contention that path introduces. Follow a local efficiency result with evidence about application effects.

Illustrative frame:

> [Binding] limits a busy [worker] while [resource] remains idle. Routing through [path] exposes that capacity, provided [interference] is controlled. We evaluate both [local metric] and [application objective].

## Review question

Does the application gain include relay costs under the reported topology, rather than assuming bandwidth gains translate directly into speedups?
