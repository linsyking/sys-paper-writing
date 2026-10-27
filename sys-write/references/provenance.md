# 03. Corpus Source and Provenance

This file records how the voice was built. Relative paths below (`corpus/`, `stage4/`, `write-like-me/`) refer to the
build workspace at `/home/yiming/Downloads/projects/paper-writing/`, not to this skill folder. The voice was built
there as `write-like-me/voices/osdi-sosp-pre2023/` and copied into this skill on 2026-10-24.

---

## Analysis date

2026-10-22

---

## Corpus role

Influence layer, not personal voice. The user selected 20 third-party, coauthored OSDI 2018, OSDI 2020, and SOSP 2021
papers as admired systems writing. Sixteen form the training split used here. Four are held out for Stage 7. No
conversation exports, personal style notes, or correction files were supplied. Paper text retains its authors' and
publishers' rights. The exemplars and example sentences in this voice are short quotations for analysis.

---

## Corpus sources

| Register | Source path | Filter | Words after filtering |
|----------|-------------|--------|----------------------|
| paper-formal | `corpus/clean/train/` (16 `.txt`, one per paper) | Prose-only extraction from the original PDFs. Front matter, headings, bibliography, acknowledgments, appendices, captions, tables, code, formulas, citation markers, and fragments are removed (see `corpus/DATASET.md`). Paragraph IDs and PDF coordinates are in `corpus/paragraphs.jsonl`. | 145,649 (7,719 sentences, 1,636 paragraphs) |

**Total analyzed:** ~145,649 words in one register. `corpus/validation.json` reports PASS on 124 checks, including no
shared source or duplicate paragraph between the training and held-out splits.

Training papers: Arachne, LegoOS, Noria, Pocket, Ray (OSDI 2018); Assise, Bourbon, CacheLib, Caladan, Clockwork
(OSDI 2020); Boki, Demikernel, HeMem, Kangaroo, LineFS, WineFS (SOSP 2021). URLs and checksums are in `corpus/manifest.tsv`.

Held out for Stage 7, not read during mining or exemplar selection: TVM (OSDI 2018), Theseus (OSDI 2020), ghOSt and
Rudra (SOSP 2021), `corpus/clean/heldout/`.

---

## Tool versions

- `write-like-me` upstream checkout, commit `82797dd9239e5804654eaa26583aadd70f51221e`, unmodified
- `scripts/stylometry.py` from that commit, standard-library tier (`--no-textstat --no-spacy`; optional readability and dependency features not installed)
- `scripts/extract_author_turns.py`, not used (no conversation exports)
- `scripts/voice_profile.py`, `scripts/voice_check.py`, `eval/voice_eval.py` from that commit
- Python 3.14.7 (project `.venv`)
- Supplementary Stage 4 miners outside the checkout: `stage4/mine.py`, `stage4/mine_sentences.py`, `stage4/mine_tense.py` (standard library, training rows only)

---

## Rule derivation

Rules in `01-generative.md` and `02-corrective.md` were derived from:

1. **Existing feedback records.** None supplied.
2. **Corpus statistics.** Upstream stylometry (`paper-formal.stylometry.json`, identical to `corpus/analysis/paper-formal.stylometry.json`), plus `stage4/features.json` and `stage4/sentences.json`:
   - Zero or near-zero features became corrective rules: contractions (10 in 4/16 papers), exclamations (0), standalone "I" (0), second person (0.001/100w), certainty boosters (2 total).
   - Distributional features became generative patterns and drift targets: sentence length, paragraph shape, subject classes, verbs after "we" and after system names, sentence openers, connective categories, hedge-with-condition co-occurrence, adjacent-sentence word reuse (51% versus 17% for random pairs), and within-paragraph length variation.
   - Drift targets are the 5th–95th percentiles over 445 consecutive 250-word training chunks. The `init` defaults flagged 96% of chunks; these flag 29%.
   - Every pattern reports its per-paper spread. Features concentrated in one or two papers are marked moderate.
3. **Universal-baseline audit.** The unmodified universal checker gave a BLOCK verdict on all 16 training papers (`stage4/baseline-<paper>.json`). Rules that would harm precise technical writing were relaxed through documented knobs only: "state-of-the-art" moved to review, "unique" removed from review, tricolon and compressed-antithesis checks off, semicolons allowed. Em dash, stance-opener, performative-verb, and summary-opener bans were kept as house rules.
4. **Qualitative observation.** Reading 48 training paragraphs (three per paper, at fixed positions) gave the paragraph moves, fair-comparison and design-choice patterns, and exemplar candidates.
5. **Stage 5 review.** The user accepted all recommendations on 2026-10-22, with a single `paper-formal` register (checklist: `stage4/candidate-rules.md`, revision 2).
6. **Tense and aspect (added 2026-10-24 at the user's request).** `stage4/mine_tense.py` → `stage4/tense.json`.
   - **Method.** For 4,691 of 7,653 non-bullet training sentences, the miner reads the finite verb after a clean subject
     ("we", a named system, Figure/Table, a pronoun, or a noun phrase followed by an auxiliary). Context labels come from
     cues: system description, results, setup, implementation, findings, decision, other systems, signposts, future work.
   - **Accuracy.** A hand check of 40 random sentences found 38 tense calls correct, and both error types were then
     fixed. Known remaining misparses include "Fig. 11 (Left) illustrates", read as the past "left", and words ending
     in "-ed" such as "memcached".
   - **Rules.** Present for the system, results, setup, other systems, and signposts. Past for one-off events and
     earlier investigations, with a present reported fact. Present perfect for prior literature and developments up to
     now. "Will" for conditional consequences. Either tense for implementation and choices, kept consistent per kind of
     passage.

Exemplars (verbatim, five different papers): osdi2018-arachne-p0010, sosp2021-kangaroo-p0006 (run-in head omitted),
osdi2018-ray-p0043, sosp2021-demikernel-p0010 (citation-marker space closed), osdi2018-pocket-p0097. Candidates
rejected for teaching banned or broken patterns: osdi2018-noria-p0091 (em dashes), sosp2021-winefs-p0087 (contraction),
osdi2020-caladan-p0069 (extraction damage), osdi2020-cachelib-p0070 (dropped citation, merged heading).

---

## Primary register: key measured values

| Feature | Value |
|---------|-------|
| Mean sentence length | 18.88 words (19.06 after removing run-in heads and bullets) |
| % long sentences (≥30w) | 12.0% |
| % short sentences (≤5w) | 5.2% (2.8% after removing run-in heads and bullets) |
| Commas per sentence | 1.007 |
| Em dashes per 1000w | 0.412 |
| Semicolons per 1000w | 2.444 (median paper 1.25) |
| Hedge tokens per 100w | 0.298 |
| Booster tokens per 100w | 0.157 (73% "must") |
| 1st person singular per 100w | 0.172 (tokenizer artifacts; 0 real) |
| 1st person plural per 100w | 1.218 |
| MATTR (window 100) | 0.6935 |
| Hapax ratio | 0.0171 |
| Concession rate | 0.114 |
| Paragraph length | mean 89, median 78 words; median 4 sentences |

---

## Re-run instructions

From the project root (`paper-writing/`):

1. `.venv/bin/python write-like-me/scripts/stylometry.py corpus/clean/train --register paper-formal --output write-like-me/voices/osdi-sosp-pre2023/paper-formal.stylometry.json --min-words 50000 --no-textstat --no-spacy`
2. `.venv/bin/python -I stage4/mine.py > stage4/features.json` and `.venv/bin/python -I stage4/mine_sentences.py > stage4/sentences.json`
3. `.venv/bin/python write-like-me/scripts/generate_report_from_json.py paper-formal:write-like-me/voices/osdi-sosp-pre2023/paper-formal.stylometry.json --output corpus/analysis/_STYLE-PROFILE-<DATE>.md`
4. Compare the new profile with this snapshot using `write-like-me/references/08-regeneration-and-diff.md`.
5. If targets change, edit `profile.json` and run `voice_profile.py validate`. Then run `eval/voice_eval.py score --goldens voices/osdi-sosp-pre2023/goldens.jsonl --profile voices/osdi-sosp-pre2023/profile.json --gate voices/osdi-sosp-pre2023/eval-baseline.json` from `write-like-me/`.
6. Update this file with the new date and word counts.

Never point the scripts at `corpus/` or the project root: that would count raw text, held-out text, and documentation.

---

## Limitations

- **Pooled, coauthored sources.** The profile averages many author teams. It cannot separate one team's habits from genre convention, except where per-paper spread is reported. Semicolons (1–76 per paper) and "thus" (58 of 143 uses in Bourbon) are examples of uneven habits.
- **No section split.** 1,218 of 1,636 paragraphs carry the label "Introduction" because the extractor lost section headings. Introduction, design, and evaluation prose are pooled in one register.
- **Extraction effects.** Run-in heads appear as short sentences. Flattened bullet lists inflate question-mark and colon counts. Some inline mathematics and citations are lost. Two exemplars needed a documented minimal edit.
- **Heuristic parsing.** Sentence splitting is regex-based (no spaCy). Subject classes, the 348 detected proper names, "This + noun" versus bare "This", and the hedge-condition association are regex heuristics. Treat those ratios as directional.
- **Tokenizer artifacts.** "I/O" and "i.e." inflate first-person-singular counts. The drift cap for that metric is set to 1.0 per 100 words for this reason, and real "I" is a hand check.
- **Booster and hedge lists.** The booster list counts deontic "must". The hedge list counts conditional "would/could". Drift caps are loose so that requirements and qualifications are not deleted.
- **House rules are not corpus facts.** The em dash, performative-verb, stance-opener, and summary-opener bans, and the "number beside magnitude words" rule, are clarity choices. Most of these patterns appear in the source papers.
- **Tense detection is heuristic.** Without a part-of-speech tagger, tense is read from word forms. 39% of sentences
  have no clean subject and verb and are not classified. Context labels come from cues, not section headings. The
  decision context has only 16 sentences, and deployment was too noisy to support a rule. Tense rules are judgment
  checks, because `voice_check.py` has no tense detector.
- **Optional features off.** textstat readability and spaCy syntax were not installed.
- **Time and venue.** 2018–2021 OSDI/SOSP only. Other venues, fields, and later conventions are not represented.
