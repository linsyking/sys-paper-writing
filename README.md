# Skills: Systems Research Paper Writing (OSDI/SOSP)

A writing skill for **OSDI/SOSP systems papers**, with particular attention to **ML systems**: LLM serving, distributed training, GPU communication, runtimes/compilers, and training reliability. It also supports storage, operating systems, distributed systems, measurement, verification, and operational-experience papers.

The skill helps explain the systems problem, design insight, implementation, and evidence. It checks assumptions, resource and semantic budgets, tail latency, tradeoffs, and claim scope. Guidance is adapted to the paper type; it does not prescribe a fixed number of contributions or benchmarks.

## Package

The installation name remains **`research-paper-writing`** for compatibility. Its display name is **Systems Paper Writing (OSDI/SOSP)**.

- [`research-paper-writing/SKILL.md`](research-paper-writing/SKILL.md): entry point and task routing.
- [`references/`](research-paper-writing/references/): guides for framing, Abstract, Introduction, Background/Motivation, Related Work, Design/Method, Implementation, Evaluation/Experiments, Discussion/Conclusion, and review.
- [`references/mlsys.md`](research-paper-writing/references/mlsys.md): workload-specific evidence and controls for serving, training, compilers, and reliability.
- [`references/examples/index.md`](research-paper-writing/references/examples/index.md): six source-linked paper examples.
- [`references/sources.md`](research-paper-writing/references/sources.md): bibliography, provenance, and edition-specific venue references.
- [`agents/openai.yaml`](research-paper-writing/agents/openai.yaml): agent metadata.

## How it works

For a paragraph edit, return the revision and a brief explanation. For substantive drafting, produce a compact outline, revised prose, unresolved facts, and a claim-evidence map. For review, prioritize objections and identify whether they need explanation, analysis, experiments, or narrower claims.

Performance claims require measurements under explicit conditions. Correctness claims may need a model, invariants, or proofs; experiments alone cannot establish universal guarantees. Missing results stay marked as missing. Evaluation plans are kept distinct from completed experiments.

## Paper corpus

The current examples draw on DistServe (OSDI 2024), FuseLink and TrainCheck (OSDI 2025), Strata (OSDI 2026), and Sailor and Mercury (SOSP 2025). Motivation, design/implementation, and evaluation passages were inspected. See the [source index](research-paper-writing/references/sources.md) for primary records, PDFs, and section locators.

The examples are original paraphrases and writing observations. PDFs and extracted paper text are not bundled. The corpus is a selected set of examples, not a complete related-work survey or a set of conference acceptance rules. Check the target year's official instructions for actual submission requirements.

## Installation

Run from the repository root. These commands copy the skill to each tool's skills directory; use the installation location configured for your environment if it differs.

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R research-paper-writing "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Claude Code

Global:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R research-paper-writing "$HOME/.claude/skills/"
```

Or project-level:

```bash
mkdir -p .claude/skills
cp -R research-paper-writing .claude/skills/
```

### Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R research-paper-writing "$HOME/.gemini/skills/"
```

## Usage examples

```text
Use $research-paper-writing to rewrite my OSDI/SOSP Introduction.
Here are my draft, design notes, and measured results.

Use $research-paper-writing to plan the evaluation of my LLM serving system.
Focus on TTFT/TPOT SLOs, goodput, baseline fairness, and KV-transfer overhead.

Use $research-paper-writing to review my distributed training paper.
Check training semantics, simulator validation, and reconfiguration costs.
```

For Claude Code or Gemini, explicitly request the `research-paper-writing` skill in your prompt.

## Attribution and license

The original skill was curated from Prof. Peng Sida (彭思达)'s [open study notes](https://pengsida.notion.site/c1a22465a0fa4b15a12985223916048e) and [learning_research repository](https://github.com/pengsida/learning_research). This adaptation retains general paper-logic and paragraph-flow principles and replaces the ML/CV examples with newly written systems guidance. Paper-specific ideas are credited to their authors in the source index; no endorsement is implied.

This repository is [MIT licensed](LICENSE). Linked papers and upstream materials retain their own copyrights and licenses.
