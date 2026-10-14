# Reviewer-Style Systems Paper Review

## Review the actual paper type and requested scope

Identify the thesis and central claims first. Assess whether the evidence supports them. A design paper, measurement paper, verification paper, and operational-experience paper need different kinds of evidence; do not require a universal benchmark checklist. Use [paper-story.md](paper-story.md) when framing is unresolved.

## Five review dimensions

| Dimension | Questions that can change the assessment |
| --- | --- |
| Significance and insight | Is this an important systems problem? What changes readers' understanding or practice? Is the contribution distinct from the nearest prior design and simple alternative? |
| Design and correctness | Are assumptions, interfaces, state, and critical execution clear? Do the mechanisms deliver the claimed contract? Are relevant concurrency, numerical, and failure conditions addressed? |
| Evaluation credibility | Are metrics and resource/semantic budgets clear? Are comparisons fair and current enough for the claim? Does evidence explain gains, costs, regressions, and relevant scale? |
| Practicality and reproducibility | Was the system implemented, simulated, or deployed as stated? Are integration constraints and needed configuration/data documented? Can central results be assessed from the main paper? |
| Clarity and scope | Can a broad systems reader follow the argument? Do figures and terms agree? Are prominent claims limited to the workload, hardware, quality, and fault conditions actually established? |

## Common consequential objections

- The motivation shows a symptom but never isolates the proposed cause.
- The main gain could be explained by more GPUs, weaker semantics, a smaller output, lower model quality, or different tuning.
- A scheduler's throughput gain masks unacceptable tail latency, drops, or starvation.
- A local bandwidth/kernel result is presented as an application-level speedup.
- A planner is evaluated only with its own unvalidated simulator.
- A detector sees only faulty runs, so false alarms remain unknown.
- Reliability/correctness language exceeds the stated model or evidence.
- The system's overhead, strongest simple alternative, or unfavorable operating regime is omitted.
- Production context is claimed from a trace replay or a prototype.
- The novelty depends on hiding reused techniques or closely related prior work.

Apply an objection only when it fits the paper's claims; do not manufacture new scope requirements.

## Report actionable findings

| Priority | Claim / locator | Objection and consequence | Existing evidence | Resolution |
| --- | --- | --- | --- | --- |
| Central / significant / minor | Exact claim and section | Why it affects the thesis or interpretation | Supported, partial, absent | Rewrite, narrow scope, supply analysis, or run a named experiment |

Separate missing explanation from missing evidence. Give the smallest useful follow-up and its expected decision value, not an indiscriminate wish list. If no experiment can be added, propose honest claim wording that fits the existing evidence.

For a full-paper review, include a short assessment of the paper's contribution, strongest evidence, main risks, and prioritized revisions. Track resolved and unresolved objections without promising acceptance. For a local edit, report only issues material to that edit.
