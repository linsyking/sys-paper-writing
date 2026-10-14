# DistServe: Objective Before Mechanism

Source: [OSDI 2024 paper](https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf). Read §§1–4 for motivation/design and §§5–6 for implementation/evaluation.

## Observed argument

The paper defines serving success through latency requirements for prefill and decode and a resource-normalized goodput objective. It connects colocated phases to interference and coupled allocation, then motivates separate execution. Placement must account for the communication introduced by that separation. Evaluation varies load and latency requirements and includes application results, breakdowns, and ablations.

## Reusable writing move

Define the service objective before describing the optimization. Explain the cost introduced by the insight alongside its benefit.

Illustrative frame:

> Co-locating [phases] couples [resource decisions] and delays [latency-sensitive work]. Separating them permits [independent choice], but adds [transfer]. We use [placement mechanism] to manage that cost within [budget].

## Review question

Are the claimed gains tied to explicit latency targets and total resources, with the transfer cost included?
