---
name: sys-write
description: Write, revise, or style-check systems-research paper prose (OSDI/SOSP/MLSys style) with a voice built from 16 OSDI 2018/2020 and SOSP 2021 papers. Use when drafting or revising paragraphs of a systems paper; when improving clarity, word choice, sentence structure, or tense; or when checking a LaTeX or Markdown draft against the voice. Preserves technical content. The project's own CLAUDE.md rules and terminology take precedence.
---

# sys-write

A writing voice for systems-paper prose: concrete subjects, purpose-first sentences, a cause after every result,
hedges tied to conditions, numbers instead of intensifiers, and consistent tense. It is an **influence layer** pooled from
16 coauthored OSDI/SOSP papers (2018–2021). It is not one author's style, and its bans are house rules for clarity, not
claims about those authors. A deterministic checker (`scripts/voice_check.py`) enforces the mechanical rules.

## Order of precedence

1. **The project's rules.** `CLAUDE.md`, the terminology it fixes, and the sources of truth it names (for example,
   `notes/BRIEF.md` for numbers). They override this skill wherever the two disagree.
2. **Rule 0** below.
3. **Hard bans.**
4. **Patterns and soft checks.**

## Rule 0. Preserve the technical content

- Never change, add, or round a number, unit, equation, citation, `\label`, `\ref`, or `\todo{}` marker. The same goes
  for project macros (`\sysname`, `\mwmgr`, `\mcsim`, …).
- Never fill a `\todo{}` or invent data. Missing data stays a `\todo{}`.
- Never delete or weaken a condition, scope limit, qualification, or rejected alternative to satisfy a rule or drift
  line. If a fix would change the claim, choose another fix or leave the sentence and say why.
- Keep the project's fixed terms even where this skill would phrase them differently.
- In LaTeX, edit prose only. Keep commands, environments, labels, comments, and line structure unless asked.

## Workflow

1. Make sure the project's `CLAUDE.md` rules and terminology are in context.
2. Before writing new prose or a substantial rewrite, read `references/patterns.md`. It has the quantitative targets,
   sentence and paragraph patterns, the tense table, and five annotated exemplars. Before revising or checking, read
   `references/checklist.md`. It has the hard bans with BAD/GOOD pairs, the soft checks, and the scan list.
3. In an interactive session, state in one sentence what you will write or revise, and wait for confirmation. When
   invoked with a written brief (for example, by a writing subagent), proceed.
4. Write or revise.
5. Run the checker (below). Fix every `block` hit and rerun until the last line is `VOICE_CHECK_PASS` or
   `VOICE_CHECK_REVIEW`. For each `review` hit and drift line, fix it or say in one line why it stays.
6. Read for the judgment rules the checker cannot see: tense, magnitude words without numbers, rhetorical triplets,
   bare "This", "I" or "you", hedges without conditions, and passive paragraph openers.
7. Report what changed, what you left alone on purpose, and the final checker verdict.

## Checker

Run from the project root. Scripts need only `python3` (standard library).

```bash
SKILL=.claude/skills/sys-write
# LaTeX: convert first, then check
python3 $SKILL/scripts/tex2text.py sections/intro.tex --preamble main.tex --output /tmp/intro.md
python3 $SKILL/scripts/voice_check.py /tmp/intro.md --profile $SKILL/profile.json --register paper-formal --check-citations
# Markdown or plain text: check directly
python3 $SKILL/scripts/voice_check.py draft.md --profile $SKILL/profile.json --register paper-formal --check-citations
```

- **Always pass `--check-citations`.** Without it, the checker treats any heading that starts with "Related" as a
  reference list and skips the whole Related Work section.
- **What the converter does:**
  - drops comments, floats, algorithms, display math, `\cite`, `\label`, and `\figplaceholder`;
  - turns `\ref` into `1`, `\S` into `§`, inline math into `x`, and `\todo{…}` into `[todo]`;
  - expands `\newcommand` macros from `--preamble`;
  - turns `---` into `—`, so the em-dash ban fires.

  A spaced ` -- ` is also flagged as a dash. A range such as `29--37` is not.
- **Line numbers** in the checker output refer to the converted file. Use the excerpt to find the sentence in the
  `.tex` source.
- **Verdict.** The last line is `VOICE_CHECK_PASS`, `VOICE_CHECK_REVIEW`, or `VOICE_CHECK_BLOCK`, and the exit code is
  1 on BLOCK.
- **Drift lines** (sentence length, commas, hedges, boosters) appear only for 150+ words. They are prompts to look, not
  orders to delete.
- **After editing `profile.json`**, run the regression gate. It must print `VOICE_EVAL_OK`:
  `python3 $SKILL/eval/voice_eval.py score --goldens $SKILL/goldens.jsonl --profile $SKILL/profile.json --gate $SKILL/eval-baseline.json`

## Hard bans (the checker blocks these)

1. **Em dashes** (`—`, LaTeX `---`, or a spaced ` -- `). Use a comma, parentheses, or a period.
2. **Contractions.** Write "does not".
3. **Exclamation marks.**
4. **Certainty words:** clearly, obviously, certainly, undoubtedly, definitely, genuinely. Let the number carry the
   strength.
5. **Stance adverbs opening a sentence:** Notably, Surprisingly, Interestingly, Importantly. Rewrite rather than delete.
   "Surprisingly, X" becomes "We expected Y, but X".
6. **leverage, utilize, delve, foster, elucidate, underscore.** Write "use", "exploit", or "build on". For a resource,
   write "high utilization".
7. **Filler openers:** It is worth noting that, Needless to say, In recent years. Give the actual period.
8. **Summary openers at the start of a paragraph:** In summary, In conclusion, To summarize. For contribution lists,
   write "This paper makes N contributions:".
9. **"Not only X but also Y".** Write "X and Y".
10. **A colon directly before a number.** "The result: 3× higher" becomes "Throughput is 3× higher". Number inline steps
    "(1)", "(2)".
11. **Hype adjectives:** innovative, groundbreaking, revolutionary, cutting-edge, game-changing. Say what is new.
12. **No "I" and no reader-addressed "you".** These are hand checks; write "we" or "Figure 4 shows".

## Core patterns (full detail and exemplars in `references/patterns.md`)

- **Subjects and verbs.** The subject is a concrete actor: the system or a component (about a fifth of sentences), a
  determiner plus technical noun (another fifth), or "we" (one in seven). "We" decides and measures: use, run,
  evaluate, compare, implement, choose. The system acts: uses, provides, reduces, stores, evicts. Repeat the system's
  name rather than switching to "it". Give "This" a noun ("This design …"). "There is" and "It is X to" are rare.
- **Openings.** About a third of sentences front a purpose ("To avoid X, …"), a condition ("When X, …"), or a link
  ("However,", "For example,"), followed immediately by subject and verb. Evaluation paragraphs open with the figure and
  its finding ("Figure 8 shows that the median latency of X is 35% lower than Y …").
- **Connections.** Old information comes before new; half of adjacent sentence pairs reuse a word from the previous
  sentence. Give the cause right after a result ("because", "due to", "This is because …"). Name the thing contrasted
  ("Unlike X, …", "In contrast, …"). Ground a general claim with "For example,". Number multi-part reasoning ("First, …
  Second, … Finally,"). Causal and contrastive links outnumber additive ones (moreover, furthermore) two to one.
- **Qualifications.** Tie each hedge to its condition ("could be beneficial when …"). Avoid softeners (perhaps,
  possibly, seem). Label beliefs and predictions with a reason ("We believe … because …", "we expect …, as …"). State
  scope ("only if", "in practice") and mark approximations ("∼8 Gb/s"). Admit where a baseline wins and why. For design
  choices, name the rejected alternative and the deciding reason in one or two sentences.
- **Length.** Sentences average about 19 words (half fall between 13 and 24; about 12% reach 30+). Vary length within a
  paragraph, typically a short claim followed by its long mechanism. Paragraphs run 3–6 sentences, opening shortest and
  ending longest.
- **Numbers and parentheses.** Claims carry numbers with units and configuration ("X% lower than Y", "N× fewer", "by up
  to N"). Parentheses hold definitions, examples, settings, and cross-references, so the main clause stays short.
- **Wordy frames.** in order to → to, is able to → can, a number of → several or the number, the use of X → the verb.

## Tense (full table in `references/patterns.md`)

Present is the default (82% of main verbs in the source papers). Choose the tense from the time the sentence refers to,
not from when the work was done.

- **Present:**
  - the system and its mechanisms;
  - what a figure or measurement shows;
  - the standard experimental setup;
  - other systems;
  - what this paper's data shows ("we find", "we see");
  - signposts ("Section 4 describes …"; avoid "will show").
- **"Will":** the consequence of a condition inside a mechanism ("Once X, the task will yield the extra cores").
- **Past:** a specific event that is over, such as a one-off extra run, a change already made to existing software, a
  production event, or an earlier investigation. The reported fact stays present if it still holds ("We found that
  Linux migrates threads …").
- **Present perfect:** prior literature and developments leading up to now ("several file systems have been built …"),
  or a completed action that matters now (releasing code). Never use it to describe how the system works or what a
  result shows.
- **Either present or past:** implementation and design choices. Pick one per kind of passage and keep it.
- **Within a paragraph:** keep one tense unless the time reference changes.

## Soft checks (fix when the pattern dominates)

- **Evaluative adjectives** (significant, important, novel, powerful, robust, state-of-the-art). Name and cite the
  system; put the number beside the adjective. "Unique" in its technical sense is fine.
- **Magnitude words** (significantly, dramatically, greatly, very). Put the number beside them.
- **Questions.** Only as stated evaluation or research questions. Otherwise, state the answer.
- **Colons that only build suspense.** "The fix is simple: …" becomes "The fix is to …". Keep "claim: evidence" colons.
- **Three or more short sentences in a row.** Join them.
- **Rhetorical triplets.** Taxonomic lists of three are normal; rewrite only lists that exist for rhythm.
- **", not X." tails.** Cut only when they add nothing; "rather than" naming an alternative stays.
- **Semicolons.** Allowed, sparingly (about one per 800 words).

## Files

| Path | Purpose |
|------|---------|
| `references/patterns.md` | Targets, structural patterns, connective profile, tense table, five annotated exemplars |
| `references/checklist.md` | Rule 0, hard bans with BAD/GOOD pairs, soft and judgment checks, baseline differences, final scan list |
| `references/provenance.md` | How the voice was built, evidence sources, limitations |
| `profile.json` | Machine-readable rules and drift targets for `voice_check.py` |
| `goldens.jsonl`, `eval-baseline.json` | 69 scored examples and the saved gate (`eval/voice_eval.py`) |
| `scripts/voice_check.py`, `voice_rules.py`, `voice_segment.py`, `voice_profile.py`, `stylometry.py` | Unmodified checker from write-like-me commit `82797dd`, MIT (`LICENSE-write-like-me.txt`) |
| `eval/voice_eval.py` | Unmodified eval harness from the same commit |
| `scripts/tex2text.py` | LaTeX-to-prose converter for checking `.tex` sections |

## Limits

- The voice pools introduction, design, evaluation, and related-work prose; section-specific habits are not separated.
- Tense, subject, and hedge rules come from regex heuristics over 145,649 words. Treat the ratios as directional.
- Exemplars and example sentences are short verbatim quotations from the source papers, which keep their authors' and
  publishers' rights. The MIT license covers only the scripts.
