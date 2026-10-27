# 02. Corrective Checklist

Run this scan on any draft before delivery. Read top to bottom. Stop and fix before continuing.

This voice is a pooled influence from 16 published OSDI/SOSP papers. Bans marked **house rule** are clarity choices
for drafts written in this voice. They are not claims about what these authors do. Several of them (em dashes,
"leverage/utilize", "Surprisingly,", "In summary,") appear in the source papers, which predate chatbot-assisted writing.
All BAD examples below are constructed illustrations. GOOD examples marked with a paragraph ID are verbatim corpus sentences.

Machine-checked rules run through `scripts/voice_check.py --profile profile.json --register paper-formal --check-citations` (paths relative to the skill folder; `SKILL.md` shows the full commands, including the LaTeX conversion step).
Rules marked **judgment** have no detector. Read for them by hand.

---

## Rule 0. Preserve the technical content (judgment, overrides every rule below)

Never delete or weaken a fact, number, unit, equation, citation, condition, scope limit, qualification, or rejected
alternative in order to satisfy a rule or a drift target. If a fix would change what the sentence claims, choose a
different fix or leave the sentence and say why. Most fixes here are rewrites, not deletions.

```
BAD:  The cache reduces misses.                       (draft said: "may reduce misses when objects are small")
GOOD: The cache may reduce misses when objects are small.
```

---

## Hard bans (zero tolerance, fix every instance)

**1. Em dashes (house rule; universal baseline `EM_DASH`).** Use a comma, parentheses, or a period. The source papers
use about one per 2,400 words, so the rewrite is rare and cheap.

```
BAD:  The log absorbs small writes — compaction handles the rest.
GOOD: The log absorbs small writes, and compaction handles the rest.
```

**2. Contractions (`CONTRACTION`).** Write them out. The corpus has 10 in 145,000 words, all "n't".

```
BAD:  The allocator doesn't track freed extents.
GOOD: The allocator does not track freed extents.
```

**3. Exclamation marks (`EXCLAMATION`).** None in the corpus.

```
BAD:  Tail latency drops to 40 μs!
GOOD: Tail latency drops to 40 μs.
```

**4. Certainty words (`EMPTY_INTENSIFIER`).** clearly, obviously, certainly, undoubtedly, definitely, genuinely. The
corpus uses two in 145,000 words. Let the number carry the strength. The checker exempts "clearly" before a participle
such as "separated", "marked", "defined", or "stated". Other manner uses ("to clearly separate") still block, so write
"to separate … cleanly" or drop the adverb.

```
BAD:  The scheduler clearly outperforms the baseline.
GOOD: The scheduler outperforms the baseline.
BAD:  This design certainly reduces tail latency.
GOOD: This design reduces tail latency.
```

**5. Stance adverbs opening a sentence (house rule; `STANCE_OPENER`).** Notably, Surprisingly, Interestingly,
Importantly, Clearly, Obviously, and similar. Do not just delete the word. "Surprisingly" carries information (the result
contradicts an expectation), so state the expectation. "Unfortunately," and "Fortunately," are not on the list and are
allowed sparingly.

```
BAD:  Surprisingly, FIFO eviction outperforms LRU on this trace.
GOOD: We expected LRU to win on this trace, but FIFO eviction outperforms it.
```

**6. Performative verbs (house rule; `PERFORMATIVE_VERB`).** leverage, utilize, delve, foster, elucidate, underscore.
Use "use", "exploit", "build on", or the specific verb. The checker also flags the adjective "utilized". Rewrite resource
utilization with the noun "utilization", which is not flagged.

```
BAD:  We leverage RDMA to replicate log entries.
GOOD: We use RDMA to replicate log entries.
BAD:  The GPUs are highly utilized throughout the run.
GOOD: The GPUs stay at high utilization throughout the run.
```

**7. Filler openers (`FILLER_OPENER`).** It is worth noting that, It goes without saying, Needless to say, In recent
years. The checker matches "in recent years" anywhere in the sentence, so replace it with the actual period from your
source.

```
BAD:  It is worth noting that the controller never blocks the write path.
GOOD: The controller never blocks the write path.
```

**8. Summary openers at the start of a paragraph (house rule; `SUMMARY_OPENER`).** In summary, In conclusion, To
summarize, To recap, As we have seen, As discussed above. For contribution lists, write "This paper makes N contributions:".

```
BAD:  In summary, the design reduces DRAM usage by 40%.
GOOD: Together, these techniques reduce DRAM usage by 40%.
```

**9. "Not only X but also Y" (`NOT_ONLY_BUT_ALSO`).**

```
BAD:  The log not only orders writes but also replicates them.
GOOD: The log orders writes and replicates them.
```

**10. A colon directly before a number (`BUILDUP_BEFORE_DATA`).** State the number in the sentence. For an inline
procedure, number the steps with "(1)", "(2)" or use a list. The checker blocks "steps: 1) …".

```
BAD:  The result: 3× higher throughput.
GOOD: Throughput is 3× higher.
BAD:  Recovery has two steps: 1) replay the log, 2) rebuild the index.
GOOD: Recovery has two steps: (1) replay the log and (2) rebuild the index.
```

**11. Hype adjectives (`EVALUATIVE_ADJECTIVE`).** innovative, groundbreaking, revolutionary, cutting-edge, game-changing.
Say what is new instead.

```
BAD:  We present an innovative cache admission policy.
GOOD: We present a cache admission policy that predicts reuse from request frequency.
```

**12. No first-person singular (judgment).** The corpus has no standalone "I". The checker cannot separate "I" from "I/O"
and "i.e.", so this is a hand check. Instead of "I believe the overhead comes from page faults", write:

```
GOOD: We believe the overhead comes from page faults.
```

**13. No second-person reader address (judgment).** No "you can see", "you should". "You" inside a compound
("pay-what-you-use") is fine. Instead of "You can see in Figure 4 that latency drops", write:

```
GOOD: Figure 4 shows that latency drops.
```

---

## Soft checks (flag and consider, fix when the pattern dominates)

Machine-checked, review level:

- **Evaluative adjectives (`EVALUATIVE_ADJECTIVE_SOFT`).** significant, important, novel, powerful, robust, compelling,
  elegant, remarkable, exceptional, state-of-the-art. For "state-of-the-art", name and cite the system rather than
  delete the claim. In statistical writing, reserve "significant" for statistical significance. "Unique" is deliberately
  not checked, because it is usually technical ("unique ID", "125K unique keys").

  ```
  BAD:  We compare against a state-of-the-art key-value store.
  GOOD: We compare against RocksDB [12], the key-value store used in prior work.
  BAD:  The policy yields significant savings in flash writes.
  GOOD: The policy reduces flash writes by 44%.
  ```

- **Questions (`RHETORICAL_QUESTION`).** Keep a question only when it states an evaluation or research question the
  paper answers. Otherwise, state the answer the paragraph gives.

  ```
  BAD:  Why does the log grow so quickly?
  GOOD: The log grows quickly because every append is replicated before compaction.
  ```

- **Announcement colons (`ANNOUNCEMENT_COLON`).** A colon after a short head. The corpus uses "claim: evidence" colons
  ("Caladan is highly effective at mitigating interference: storage and memcached achieve nearly the same tail
  latency…", osdi2020-caladan-p0069), so keep those. Rewrite a colon that only builds suspense.

  ```
  BAD:  The fix is simple: batch the updates.
  GOOD: The fix is to batch the updates.
  ```

- **Hedge connectives (`HEDGE_CONNECTIVE`).** that said, to be fair, worth knowing. Keep the contrast and use a plain
  connective.

  ```
  BAD:  That said, the prototype does not support kernel objects.
  GOOD: However, the prototype does not support kernel objects.
  ```

- **Runs of short sentences (`STACCATO_RUN`).** Three or more sentences of 8 words or fewer in a row. Join the connected
  events.

  ```
  BAD:  The log fills. Compaction starts. Writes stall.
  GOOD: When the log fills, compaction starts and writes stall.
  ```

- **Drift lines.** Sentence length, short/long share, commas per sentence, hedge and booster density, first-person rate.
  Drift is a prompt to look, not an instruction to delete. Under Rule 0, a hedge with its condition or a requirement
  stated with "must" stays.

Judgment, review level (read for these by hand):

- **A magnitude word on a result without its number.** "significant(ly)", "dramatically", "greatly", "very". Put the
  number beside it when the data exists (house rule; the corpus does this only 24% of the time).

  ```
  GOOD: Batching reduces flash writes by 44%.
  ```

- **Rhetorical triplets.** The checker's tricolon rule is off because lists of three in systems papers are usually
  taxonomic ("We evaluate on three workloads: YCSB-A, YCSB-B, and TPC-C."). Rewrite only a triplet that exists for rhythm.
- **", not X." tags.** The checker's antithesis rule is off because "rather than" usually names the rejected design
  alternative (see the GOOD sentence below). Cut a ", not X." tail only when it adds nothing.
- **Bare "This".** Give the demonstrative its noun when the referent is a whole clause ("This design reduces copies.").
- **"It" where the name is clearer.** In a description of one system, repeat the name rather than switch to "it".
- **Wordy frames.** in order to → to, is able to → can, a number of → several or the number, the use of X → the verb,
  perform a/an X → the verb. "allows X to" is a common corpus pattern and stays.
- **Hedges without conditions.** Keep "may", "might", "could" when the draft is uncertain, and add the condition under
  which the claim holds ("when objects are small").
- **Passive voice in a paragraph's first sentence.** Prefer the actor: "we" for decisions, the system for behavior.

### Tense (judgment)

Default to the present for the system, results, setup, other systems, and signposts. Use the past for a specific event
that is over: a one-off run, a change already made to existing software, a production event, or an earlier
investigation. Use the present perfect for prior literature and for developments that lead up to now. Use "will" for
the consequence of a condition inside a mechanism. Keep one tense within a paragraph unless the time reference changes.
Under Rule 0, never change a tense that encodes a real time difference in the draft. The full evidence table is in
`patterns.md` ("Tense and aspect"). The BAD examples below are constructed illustrations.

```
BAD:  Figure 5 showed that the cache reduced misses by 29%.
GOOD: Figure 5 shows that the cache reduces misses by 29%.
BAD:  We run each benchmark five times and reported the median.
GOOD: We run each benchmark five times and report the median.
BAD:  The scheduler has assigned each task to a core.              (describing how the scheduler works)
GOOD: The scheduler assigns each task to a core.
BAD:  Section 5 will show that batching hides the latency.
GOOD: Section 5 shows that batching hides the latency.
BAD:  We found that the allocator fragmented memory under churn.   (the behavior still holds)
GOOD: We found that the allocator fragments memory under churn.
```

Verbatim corpus sentences that show each tense in its place:

```
GOOD: We deploy Clockwork in a private cluster of 12 Dell PowerEdge R740 Servers.                 (osdi2020-clockwork-p0074)
GOOD: We also modified RAMCloud to use Arachne.                                                   (osdi2018-arachne-p0100)
GOOD: We observed that this holds for other levels as well.                                       (osdi2020-bourbon-p0040)
GOOD: To combat network overheads, several file systems have been built or retrofitted to use RDMA.   (osdi2020-assise-p0016)
GOOD: Once the GC interference has been successfully mitigated, the LC task will yield the extra cores.   (osdi2020-caladan-p0047)
GOOD: Section 4 describes the core arbiter in detail.                                             (osdi2018-arachne-p0018)
```

---

## Approved genre patterns the checker must not block

These verbatim training sentences show patterns that this profile deliberately allows. They are pass cases in `goldens.jsonl`.

```
GOOD: We then perform 60M lookups of a hot-set of 125K unique keys in random order.                (sosp2021-winefs-p0087)
GOOD: HeMem monitors application memory use by sampling memory access via CPU events, rather than page tables.   (sosp2021-hemem-p0002)
GOOD: The Arachne runtime will not release a core until the dispatcher is invoked on that core, which happens when a user thread blocks, yields, or exits.   (osdi2018-arachne-p0040)
GOOD: As noted earlier, Demikernel libOSes may have to hold references for a long time; for example, the TCP stack can safely dec_ref only after the receiver has acked the packet.   (sosp2021-demikernel-p0035)
GOOD: Learned indexes could be beneficial when the database or a portion of it is cached in memory.   (osdi2020-bourbon-p0034)
GOOD: Unlike Ray, most existing cluster computing systems use a centralized scheduler architecture.   (osdi2018-ray-p0085)
GOOD: This is due to the PEBS thread being unable to keep up with the samples generated.   (sosp2021-hemem-p0072)
```

---

## How this voice differs from the universal baseline document

The upstream write-like-me universal baseline (`references/00-universal-baseline.md` in that repository) is built into
`scripts/voice_rules.py` and stays active. This profile changes only its documented knobs:

| Baseline behavior | This voice | Why |
|-------------------|-----------|-----|
| "state-of-the-art" blocks | Review | It names the comparison class (10/16 papers); deleting it drops a claim |
| "unique" is reviewed | Not checked | 16 of 25 corpus uses are technical (unique ID, unique keys) |
| Tricolon reviewed | Off; judgment for rhetorical triplets | 367 corpus hits, every sampled one a taxonomic list |
| "rather than" / ", not X." reviewed | Off; judgment | "rather than" names the rejected alternative (13/16 papers) |
| Semicolons off by default (init proposed review) | Off (allowed) | All 16 papers use them, at very different rates (1–76 per paper) |
| Contractions, exclamations, questions off | Block, block, review | Near zero in the corpus |
| certainly, undoubtedly, definitely unlisted | Added to intensifiers | 1 corpus use in total |
| Drift targets ±15% of the pooled mean | 5th–95th percentile of 250-word corpus chunks | Default targets flag 96% of the corpus's own text; these flag 29% |

The baseline document lists "significant", "important", "novel", "unique", and "robust" among banned pre-modifiers, but
the code reviews rather than blocks them. This voice follows the code, with the changes above. No `rule_overrides` are used.

---

## Final mechanical scan

Before delivery, grep the draft for each of these and confirm the count:

| Pattern | Target count |
|---------|-------------|
| `—` and ` -- ` between words | 0 |
| `n't`, `it's`, `that's`, `we're`, `they're`, `let's` | 0 |
| `!` | 0 |
| `clearly`, `obviously`, `certainly`, `undoubtedly`, `definitely`, `genuinely` | 0 ("clearly" + participle such as "separated" excepted) |
| `leverag`, `utiliz` (verb or adjective) | 0 (`utilization` is fine) |
| `delve`, `foster`, `elucidate`, `underscore` | 0 |
| `It is worth noting`, `Needless to say`, `It goes without saying`, `in recent years` | 0 |
| `In summary`, `In conclusion`, `To summarize`, `To recap` at a paragraph start | 0 |
| `not only` … `but also` | 0 |
| `innovative`, `groundbreaking`, `revolutionary`, `cutting-edge`, `game-changing` | 0 |
| `: ` followed by a digit | 0 |
| Standalone `I`, `my`, `me` | 0 |
| `you`, `your` addressing the reader | 0 |
| `?` | Only in stated evaluation or research questions |
| `;` | Sparing, about one per 800 words |
| `significant`, `significantly`, `dramatically`, `greatly`, `very` | Each next to its number |
| `state-of-the-art` | Each names and cites the system |
| `in order to`, `is able to`, `a number of`, `the use of` | Prefer to, can, several or the number, the verb |
| `will show`, `will describe`, `will discuss`, `will present` in signposts | 0 (use the present) |
| `Figure N` / `Table N` followed by `showed`, `illustrated`, `reported` | Present, unless the sentence narrates a one-off event |
| `has` / `have` + participle describing the system or a result | Present simple, unless it is a development up to now |
