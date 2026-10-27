# Skills: Systems Research Paper Writing (OSDI/SOSP)

Two complementary writing skills for **OSDI/SOSP systems papers**:

| Skill | Main focus | Use it for |
| --- | --- | --- |
| [`research-paper-writing`](research-paper-writing/SKILL.md) | Paper and section structure, research argument, and evidence | Framing the problem and contribution, organizing sections, planning evaluation, and reviewing claims |
| [`sys-write`](sys-write/SKILL.md) | Word choice, sentence structure, and paragraph-level writing | Drafting and polishing prose, improving transitions and tense, and checking writing style against a profile derived from past OSDI/SOSP papers |

Use `research-paper-writing` to develop what the paper needs to say and how its evidence supports the argument. Use `sys-write` to refine how individual sentences and paragraphs express it. They can be used independently or together.

## Packages

### `research-paper-writing`

The installation name remains **`research-paper-writing`** for compatibility. Its display name is **Systems Paper Writing (OSDI/SOSP)**.

This skill helps explain the systems problem, design insight, implementation, and evidence. It checks assumptions, resource and semantic budgets, tail latency, tradeoffs, and claim scope. It gives particular attention to **ML systems**: LLM serving, distributed training, GPU communication, runtimes/compilers, and training reliability. It also supports storage, operating systems, distributed systems, measurement, verification, and operational-experience papers. Guidance is adapted to the paper type; it does not prescribe a fixed number of contributions or benchmarks.

- [`research-paper-writing/SKILL.md`](research-paper-writing/SKILL.md): entry point and task routing.
- [`references/`](research-paper-writing/references/): guides for framing, Abstract, Introduction, Background/Motivation, Related Work, Design/Method, Implementation, Evaluation/Experiments, Discussion/Conclusion, and review.
- [`references/mlsys.md`](research-paper-writing/references/mlsys.md): workload-specific evidence and controls for serving, training, compilers, and reliability.
- [`references/examples/index.md`](research-paper-writing/references/examples/index.md): six source-linked paper examples.
- [`references/sources.md`](research-paper-writing/references/sources.md): bibliography, provenance, and edition-specific venue references.
- [`agents/openai.yaml`](research-paper-writing/agents/openai.yaml): agent metadata.

### `sys-write`

Based on [`Hiro-Inagawa/write-like-me`](https://github.com/Hiro-Inagawa/write-like-me), with a writing profile built from **16 past OSDI/SOSP papers**. Corpus analysis supplies patterns for word choice, concrete subjects and verbs, sentence length, tense, transitions, and paragraph flow. A deterministic checker applies mechanical style rules and flags possible drift from the profile.

- [`sys-write/SKILL.md`](sys-write/SKILL.md): entry point, revision workflow, and checker instructions.
- [`references/patterns.md`](sys-write/references/patterns.md): sentence and paragraph patterns, tense guidance, and annotated examples.
- [`references/checklist.md`](sys-write/references/checklist.md): editing checklist and examples of revisions.
- [`references/provenance.md`](sys-write/references/provenance.md): corpus, analysis methods, and limitations.
- [`profile.json`](sys-write/profile.json): machine-readable style rules and targets.
- [`scripts/voice_check.py`](sys-write/scripts/voice_check.py) and [`scripts/tex2text.py`](sys-write/scripts/tex2text.py): prose checker and LaTeX-to-text converter; require only `python3` and its standard library.

The profile captures shared writing patterns across the source papers. Revisions preserve technical claims, numbers, units, citations, LaTeX commands, and project terminology. The project's own writing rules take precedence.

## How to use them together

1. Use `research-paper-writing` to frame the story, outline sections, connect claims to evidence, and identify missing results.
2. Use `sys-write` to revise words, sentences, and paragraphs for clarity and consistent systems-paper prose.
3. Run the `sys-write` checker and review its findings while preserving technical meaning and qualifications.

For a paragraph edit, `research-paper-writing` returns the revision and a brief explanation. For substantive drafting, it produces a compact outline, revised prose, unresolved facts, and a claim-evidence map. For review, it prioritizes objections and identifies whether they need explanation, analysis, experiments, or narrower claims.

Performance claims require measurements under explicit conditions. Correctness claims may need a model, invariants, or proofs; experiments alone cannot establish universal guarantees. Missing results stay marked as missing. Evaluation plans are kept distinct from completed experiments.

## Paper corpora

### `research-paper-writing` examples

The current examples draw on DistServe (OSDI 2024), FuseLink and TrainCheck (OSDI 2025), Strata (OSDI 2026), and Sailor and Mercury (SOSP 2025). Motivation, design/implementation, and evaluation passages were inspected. See the [source index](research-paper-writing/references/sources.md) for primary records, PDFs, and section locators.

The examples are original paraphrases and writing observations. PDFs and extracted paper text are not bundled. The corpus is a selected set of examples, not a complete related-work survey or a set of conference acceptance rules. Check the target year's official instructions for actual submission requirements.

### `sys-write` style profile

The profile was built from **16 papers from OSDI 2018, OSDI 2020, and SOSP 2021**, totaling approximately **145,649 words** of filtered prose. Four additional papers were reserved as a held-out split. The analysis covers word choice, sentence and paragraph structure, connective patterns, hedging, and tense. See the [provenance record](sys-write/references/provenance.md) for the paper list, methods, and limitations.

The resulting skill includes a style profile, writing guidance, short quoted examples, and a checker. Some checker rules are editorial choices; the measured patterns are guidance for revision rather than requirements for every sentence or paragraph.

## Installation

Run from the repository root. These commands copy both skills to each tool's skills directory. To install only one, include only its directory in the `cp` command. Use the installation location configured for your environment if it differs.

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R research-paper-writing sys-write "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Claude Code

Global:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R research-paper-writing sys-write "$HOME/.claude/skills/"
```

Or project-level:

```bash
mkdir -p .claude/skills
cp -R research-paper-writing sys-write .claude/skills/
```

### Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R research-paper-writing sys-write "$HOME/.gemini/skills/"
```

## Usage examples

```text
Use $research-paper-writing to rewrite my OSDI/SOSP Introduction.
Here are my draft, design notes, and measured results.

Use $research-paper-writing to plan the evaluation of my LLM serving system.
Focus on TTFT/TPOT SLOs, goodput, baseline fairness, and KV-transfer overhead.

Use $research-paper-writing to review my distributed training paper.
Check training semantics, simulator validation, and reconfiguration costs.

Use $sys-write to polish these paragraphs from my OSDI/SOSP paper.
Focus on word choice, sentence structure, tense, and paragraph flow.
Preserve all technical claims, numbers, citations, and LaTeX commands.

Use $research-paper-writing to improve the argument in this Introduction,
then use $sys-write to polish its sentences and paragraphs.
```

For Claude Code or Gemini, explicitly request the `research-paper-writing` or `sys-write` skill in your prompt.

To check a Markdown or plain-text draft directly, run from the repository root:

```bash
python3 sys-write/scripts/voice_check.py draft.md \
  --profile sys-write/profile.json --register paper-formal --check-citations
```

The checker reports findings with line numbers and ends with `VOICE_CHECK_PASS`, `VOICE_CHECK_REVIEW`, or `VOICE_CHECK_BLOCK`. For LaTeX drafts, first convert the prose with `tex2text.py`; see the [checker instructions](sys-write/SKILL.md#checker).

## Attribution and license

`research-paper-writing` was curated from Prof. Peng Sida (彭思达)'s [open study notes](https://pengsida.notion.site/c1a22465a0fa4b15a12985223916048e) and [learning_research repository](https://github.com/pengsida/learning_research). This adaptation retains general paper-logic and paragraph-flow principles and replaces the ML/CV examples with newly written systems guidance. Paper-specific ideas are credited to their authors in the source index; no endorsement is implied.

`sys-write` is based on [Hiro-Inagawa/write-like-me](https://github.com/Hiro-Inagawa/write-like-me), using its checker and evaluation harness from commit [`82797dd`](https://github.com/Hiro-Inagawa/write-like-me/tree/82797dd9239e5804654eaa26583aadd70f51221e). Its writing profile and guidance were derived from the OSDI/SOSP corpus described above.

This repository is [MIT licensed](LICENSE). Source papers, quoted examples, and upstream materials retain their own copyrights and licenses.
