# 01. Generative Patterns

Read this file when writing or revising prose in the `osdi-sosp-pre2023` voice. It defines what to build toward.

This voice is an **influence layer**, not a personal voice. It pools 16 coauthored OSDI 2018, OSDI 2020, and SOSP 2021
papers. The patterns below are genre tendencies of published systems research to reach toward. They are not habits
of the user or prohibitions taken from these authors. The user's technical content always wins: keep every fact,
number, equation, citation, condition, and qualification in the draft (see `checklist.md`, rule 0).

Topic vocabulary (memory, cache, latency, DRAM, flash, log, thread) and system names are **not** style. Their rates
swing widely between papers (cross-paper coefficient of variation 0.77–2.66). Most function words and connectives used
below are far steadier (0.16–0.59). "Because" (0.82) and "thus" (1.47) are the uneven exceptions and are marked as
moderate. Do not import the corpus's subject matter or jargon into a draft.

---

## Quantitative targets (paper-formal register)

These numbers describe the pooled corpus. They are not constraints to hit precisely. They are the territory to write into.
"Checker range" is what `voice_check.py` treats as normal for a draft of 150 words or more. It spans the 5th–95th
percentile of 445 consecutive 250-word chunks from the corpus.

| Feature | Corpus value | Checker range / rule for drafts |
|---------|--------------|---------------------------------|
| Mean sentence length | 18.9 words (median 18, middle half 13–24) | 14–26 words |
| Short sentences (≤5 words) | 2.8% of real sentences (5.2% raw, inflated by run-in heads) | ≤17%; use them for pointers and terse assertions |
| Long sentences (≥30 words) | 12.0% (2.5% reach 40+) | 0–33% |
| Commas per sentence | 1.01 | 0.5–1.75 |
| Em dashes per 1000 words | 0.41 (10 of 16 papers) | 0 (house rule, see `checklist.md`) |
| Semicolons per 1000 words | 2.44 pooled; median paper 1.25; range 0.1–8.0 | Allowed, sparingly (about one per 800 words) |
| First-person singular per 100 words | 0 real uses (the measured 0.17 is "I/O", "i.e.", "(i)") | 0 |
| Hedging tokens per 100 words | 0.30 | ≤1.15, each hedge tied to a condition |
| Boosting tokens per 100 words | 0.16, of which 73% is "must" (a requirement) | ≤0.75; certainty words such as clearly or certainly: 0 |

---

## Structural patterns

### Sentences

The grammatical subject is a concrete actor. A named system or component is the subject of about a fifth of sentences
("KSet maps an object to a set by hashing its key."). A determiner plus technical noun is the subject of another fifth
("The controller…", "Each slab class…"). "We" is the subject of one in seven. Expletive openings are rare: "There is/are"
opens 0.4% of sentences and "It is X to/that" 0.2%. Prefer the actor that performs the action, and prefer the verb that
names it over a frame such as "perform a", "make use of", "is able to", "in order to", or "the use of".

"We" and the system split the verbs. "We" decides and measures: use, run, evaluate, compare, measure, implement,
configure, choose. The system acts: uses, provides, achieves, supports, implements, maintains, reduces, stores, evicts.
When several consecutive sentences describe the same system, repeat its name instead of switching to "it". A
demonstrative usually takes a noun: "This design…", "This overhead…" appear about twice as often as a bare "This is…".

About a third of sentences front a phrase before the subject. That phrase states the purpose ("To avoid overloading the
global scheduler, …"), the condition ("When a LibFS log grows to the size of a LineFS chunk, …"), or the link to the
previous sentence ("However, …", "For example, …"). The subject and main verb follow immediately after the comma.

Sentences average 19 words. Length follows content, not rhythm. Short sentences point ("Figure 10 shows the results.")
or assert one fact ("This support is not necessary."). Long sentences (30+ words) usually hold one condition and its
consequence, or a measurement and its cause. A 40-word sentence is rare (2.5%).

Numbers carry claims: a quarter of sentences contain a digit. Comparisons take the form "X% lower than Y", "N× fewer",
"by up to N", with units and the configuration that produced them. Parentheses hold definitions, examples, settings,
and cross-references ("(i.e., its local task queue exceeds a predefined threshold)", "(e.g., 4 MB)", "(§4)", "(Figure 3)")
so the main clause stays short.

### Paragraphs

A typical paragraph has 4 sentences (middle half 3–6) and about 80 words. The first sentence states the claim, problem,
or role of the paragraph and is the shortest on average (16 words). Later sentences give mechanism, cause, or evidence.
The last sentence is the longest on average (20 words) and often carries the consequence or the number.

Length varies inside the paragraph. In nearly half of paragraphs with three or more sentences, a sentence of 12 words or
fewer sits next to one of 25 or more. The common move is a short claim followed by a long mechanism: "However,
set-associative caches write many excess bytes to flash. Admitting a single small object to the cache requires
re-writing an entire set, …"

Each sentence picks up something the previous sentence introduced. In half of adjacent sentence pairs, the second
sentence's opening reuses a content word from the first. Random pairs from the same paper do this only 17% of the time.
New information goes at the end of the sentence, where the next sentence can pick it up as its subject.

Design and evaluation paragraphs may open with a run-in head: a noun phrase and a period ("Comparison with Cloudburst.",
"Kernel objects in tiered memory."). About one paragraph in eight does so. Evaluation paragraphs often open on the figure
and its finding: "Figure 8 shows that the median latency of WineFS is 35% lower than ext4-DAX and 60% lower than NOVA."

### Essay movement

Within a section, paragraphs move in a recognizable order. First, a problem paragraph states a limitation and spells out
its consequences as conditions. A design paragraph then introduces the mechanism with a purpose-first sentence. A
choice paragraph names the alternative and the reason. An evaluation paragraph reports a figure, its numbers, and the
cause of each deviation. Transitions between paragraphs are carried by the first sentence ("To satisfy the above
requirements, we design…", "We next describe how…"), not by summary openers. This ordering comes from reading, because
the corpus lacks reliable section labels. Treat it as a guide, not a measurement.

### Perspective and stance

The authors write as "we" (1.2 per 100 words) and never as "I". They do not address the reader as "you". Opinions and
predictions are labelled and given a reason: "We believe this is a reasonable design choice because…", "we expect this
gap to be smaller, as…". Hedges come with their condition: "Learned indexes could be beneficial when the database or a
portion of it is cached in memory." Softeners such as perhaps, possibly, seem, and somewhat appear about ten times in
145,000 words. Certainty words such as clearly, obviously, and certainly appear twice.

Comparisons are bounded. Scope is stated ("only if", "in practice", "at high load"), numbers are marked as approximate
when they are ("∼8 Gb/s", "about 10 seconds"), and losses are admitted with their cause ("LegoOS performs worse with
higher workload threads, because…"). Design choices name the rejected alternative, sometimes conceding its merit ("which
can perform equally well"), before the deciding reason.

### Tense and aspect

Present tense is the default. Of 4,691 main verbs classified in the training papers, 82% are present simple ("does"),
4% past ("did"), 1.5% present perfect ("has done"), 1.6% "will", and 10% modal (can, may, must). Choose the tense from
the time the sentence refers to, not from when the work was done. The system, the figures, and the setup exist now, as
the reader reads the paper.

| What the sentence does | Tense | Evidence (training papers) |
|------------------------|-------|----------------------------|
| Describes the system, a component, or a mechanism | Present | 815 present vs 10 past; every paper at least 91% present |
| Gives the consequence of a condition inside a mechanism | "will" | 73 uses of "will" in 14 papers, mostly after if/once/when |
| Reports what a figure, table, or measurement shows | Present | 398 present vs 19 past; all 16 papers mostly present (lowest 65%) |
| Describes the standard experimental setup | Present | 263 present vs 21 past; 15 of 16 papers mostly present (Arachne's 5 detected setup sentences are all past) |
| Narrates a one-off extra run, a change already made to existing software, or a production event | Past | Most of the 202 past-tense sentences |
| Describes the implementation | Present for the artifact as it stands; past for the engineering history | 53 present vs 28 past; 7 papers mostly present, 4 mostly past (a per-paper habit) |
| Reports what this paper's data shows | Present: we find, we observe, we see | 29 present uses of these verbs |
| Reports an earlier investigation | Past verb, present fact: "we found that X does" | 17 past uses; the reported fact stays present in 14 of 15 |
| States a design or baseline choice | Present for a standing choice; past for a decision made during design | 7 present vs 9 past (small sample) |
| Describes what another system does | Present | 273 present vs 11 past; all 16 papers mostly present |
| Summarizes prior literature or a development that leads up to now | Present perfect | 72 present-perfect sentences in 15 papers |
| States a completed action of the authors that matters now | Present perfect | e.g., releasing the code |
| Signposts the paper | Present: we present, we describe, Section 4 describes | 92 present vs 2 "will show"; 3 conclusions use "This paper presented" |
| States future work | "we plan to" + verb | 28 of 30 future-work sentences |

Examples (verbatim):

- System, present: "LibFS intercepts the application’s POSIX file system calls and writes file data and metadata to the PM log." (sosp2021-linefs-p0028)
- Conditional consequence, "will": "Once the GC interference has been successfully mitigated, the LC task will yield the extra cores." (osdi2020-caladan-p0047)
- Results, present: "Figure 3 shows the number of hugepages available as a file system is aged." (sosp2021-winefs-p0017)
- Setup, present: "We run RocksDB configured to use memory-mapped reads and writes, with hugepages enabled and a memory cap of 64GB." (sosp2021-winefs-p0084)
- One-off change or event, past: "We also modified RAMCloud to use Arachne." (osdi2018-arachne-p0100); "The net effect was a 15% reduction in the number of NAND writes to the flash device per second." (osdi2020-cachelib-p0067)
- Implementation, present: "We implement both the local and global schedulers as event-driven, single-threaded processes." (osdi2018-ray-p0049)
- This paper's data, present: "From the table, we see that the log replay optimization is crucial for BokiStore to achieve an acceptable performance." (sosp2021-boki-p0105)
- Earlier investigation, past verb with present fact: "We observed that this holds for other levels as well." (osdi2020-bourbon-p0040)
- Choice, either tense: "We choose Assise as a baseline system because it is a client-local DFS like LineFS." (sosp2021-linefs-p0056); "We chose to offer only UAF protection as there is no low cost way for Demikernel to provide full write-protection." (sosp2021-demikernel-p0021)
- Other systems, present: "NOVA uses log-structured layout for its metadata, and contains a per-inode log in the form of a linked list." (sosp2021-winefs-p0069)
- Development up to now, present perfect: "To combat network overheads, several file systems have been built or retrofitted to use RDMA." (osdi2020-assise-p0016); "State management has become a major challenge in serverless computing." (sosp2021-boki-p0120)
- Signpost, present: "We now describe BOURBON, an LSM-based store that uses learning to make indexing faster." (osdi2020-bourbon-p0047); "Section 4 describes the core arbiter in detail." (osdi2018-arachne-p0018)

Within a paragraph, keep one tense unless the time reference changes. Of 664 paragraphs with three or more classified
verbs, 81% stay entirely in the present and 13% mix present and past. In those mixed paragraphs, the switch marks a real
change in time: project history leading into the present mechanism ("Recently, CacheLib was updated to include a more
advanced admission policy … Thus, CacheLib implements efficient tracking of object request frequencies …",
osdi2020-cachelib-p0070), or a one-off modification inside an otherwise present-tense setup (osdi2020-caladan-p0059).
The tense choice is made per kind of passage, not once per paper. Caladan narrates its implementation in the past
(7 of 7 detected sentences) but writes its setup in the present (14 of 14). Pick one tense for each kind of passage in
a draft and keep it.

---

## Discourse connective profile

Causal and adversative links dominate. Additive links are half as frequent, and the heavier additive forms are rare.

| Type | Rate per 1000 words | Preferred forms | Rare or absent |
|------|---------------------|-----------------|----------------|
| Causal | 5.3 | because (1.4), due to (1.0), thus (1.0), since, as a result, so that | therefore (0.17), consequently (0.05) |
| Adversative | 5.1 | However, (opens 1 in 50 sentences), but, instead, in contrast, unlike X, while | on the other hand (0.08), nevertheless |
| Exemplifying | 3.8 | For example, (opens 1 in 60 sentences), such as, (e.g., …), (i.e., …) | for instance (0.12) |
| Additive | 2.7 | also, in addition, similarly | moreover (0.11), furthermore (0.13), additionally (0.12) |
| Sequence | — | First, … Second, … Finally, (1.2) | — |
| Conditional | 3.0 | if, when, unless, would/could in counterfactuals | — |

"Thus" is preferred over "therefore", but 58 of its 143 uses come from one paper. Treat that preference as moderate.
"Note that" appears 19 times and "This is because" 8 times. Both are available but not habitual.

---

## Cognitive process markers

- **Causation-heavy.** Results and design decisions are followed by their cause ("This is due to the PEBS thread being
  unable to keep up with the samples generated."). Causal connectives outnumber additive ones two to one.
- **Conditional and counterfactual reasoning.** "If …, the operating system will multiplex workers on a single core,
  resulting in …"; "Memcached would perform better if it could…". Conditions define when a claim holds.
- **Quantified rather than intensified.** Strength comes from numbers and comparisons, not from boosters. Where the
  corpus does use "significant" or "dramatically", the house rule for this voice is to put the number beside it.
- **Observation, then inference.** "We find", "we observe", "we see" (0.5 per 1000 words, 15 of 16 papers) report
  evidence. "Thus" or "As a result" draws the design consequence.
- **Labelled belief.** "We believe" and "we expect" mark claims that go beyond the evidence (10 of 16 papers).

---

## Exemplars

Use these to calibrate feel before writing, not to copy structure or vocabulary. All five are verbatim training paragraphs
from five different papers. None comes from the held-out papers.

---

**Exemplar 1. Problem stated, consequences as conditions** (osdi2018-arachne-p0010, OSDI 2018)

> The number of worker threads is fixed when memcached starts, which results in several inefficiencies. If the number of cores available to memcached is smaller than the number of workers, the operating system will multiplex workers on a single core, resulting in long delays for requests sent to descheduled workers. For best performance, one core must be reserved for each worker thread. If background tasks are run on the machine during periods of low load, they are likely to interfere with the memcached workers, due to the large number of distinct worker threads. Furthermore, during periods of low load, each worker thread will be lightly loaded, increasing the risk that its core will enter power-saving states with high-latency wakeups. Memcached would perform better if it could scale back during periods of low load to use a smaller number of kernel threads (and cores) more intensively.

What to notice: The first sentence states the fact and promises "several inefficiencies". Each later sentence delivers
one, as a condition followed by its consequence ("If …, … resulting in …"), so the paragraph argues by mechanism rather
than by adjectives. A 12-word requirement sits between two long conditional sentences. The closing counterfactual points
at the design goal without naming the solution yet.

---

**Exemplar 2. Two prior designs, each with mechanism and cost** (sosp2021-kangaroo-p0006, SOSP 2021; run-in head "The problem." omitted)

> Prior flash-cache designs either use too much DRAM or write flash too much. Log-structured caches write objects to flash sequentially and keep an index (typically in DRAM) that tracks where objects are located on flash. By writing objects sequentially and batching many insertions into each flash write, log-structured caches greatly reduce the excess bytes written to flash. However, tracking billions of tiny objects requires a large index, and even a heavily optimized index needs large amounts of DRAM. Set-associative caches operate by hashing objects’ keys into distinct “sets,” much like CPU caches. These designs do not require a DRAM index because an object’s possible locations are implied by its key. However, set-associative caches write many excess bytes to flash. Admitting a single small object to the cache requires re-writing an entire set, significantly amplifying the number of bytes written to the flash device.

What to notice: A 13-word opening states the dilemma. Each design then gets a mechanism sentence and a "However," cost
sentence, and "These designs" resumes the subject with a noun instead of "they" or "this". The final pair is a short
claim (9 words) followed by its long mechanism (24 words). "Greatly" and "significantly" stand without numbers here. In
a draft, put the number beside them when the data exists.

---

**Exemplar 3. Mechanism, purpose first** (osdi2018-ray-p0043, OSDI 2018)

> To satisfy the above requirements, we design a two-level hierarchical scheduler consisting of a global scheduler and per-node local schedulers. To avoid overloading the global scheduler, the tasks created at a node are submitted first to the node’s local scheduler. A local scheduler schedules tasks locally unless the node is overloaded (i.e., its local task queue exceeds a predefined threshold), or it cannot satisfy a task’s requirements (e.g., lacks a GPU). If a local scheduler decides not to schedule a task locally, it forwards it to the global scheduler. Since this scheduler attempts to schedule tasks locally first (i.e., at the leaves of the scheduling hierarchy), we call it a bottom-up scheduler.

What to notice: Two sentences open with "To <goal>,", so the reader knows why each mechanism exists before seeing it.
"Unless" and "If" spell out exactly when each path is taken. Parentheses define the threshold and give an example
without breaking the clause. The design is named only in the last sentence, after the reader has seen why the name fits.

---

**Exemplar 4. Design choice against a named alternative** (sosp2021-demikernel-p0010, SOSP 2021; space left by a removed citation marker closed)

> For μs-scale CPU multiplexing, Demikernel uses coroutines to encapsulate both OS and application computation. Coroutines are lightweight, have low-cost context switches and are well-suited for the state-machine-based asynchronous event handling that I/O stacks commonly require. We chose coroutines over user-level threads (e.g., Caladan’s green threads), which can perform equally well, because coroutines encapsulate state for each task, removing the need for global state management. For example, Demikernel’s TCP stack uses one coroutine per TCP connection for retransmissions, which keeps the relevant TCP state.

What to notice: The order is what the system uses, why the mechanism suits the task, the choice against a named
alternative, then one concrete instance. The alternative gets its due ("which can perform equally well") before the
deciding "because", which makes the choice credible without an evaluative word. The subjects change from Demikernel to
coroutines to "we" to the TCP stack, and each one is a concrete actor.

---

**Exemplar 5. Evaluation result with causes and a counterfactual cost** (osdi2018-pocket-p0097, OSDI 2018)

> Figure 10 shows that Pocket quickly and effectively scales the allocated storage bandwidth (dotted line) to meet application throughput demands (solid line). The spike surpassing the allocated throughput is due to a short burst in EC2 VM network bandwidth. The VMs provide ‘up to 10 Gb/s’, but since we typically observe a ∼8 Gb/s bandwidth limit in practice, the controller allocates throughput assuming each node provides 8 Gb/s. As the controller rightsizes resources for each job, job execution time stays within 5% of its execution time when running on 50 nodes, the conservative default resource allocation. If the controller had to spin up new VMs to accommodate a job’s requirements instead of just launching containers, the job’s start time would be delayed by up to 215 seconds (see EC2 NVMe server startup time in Figure 7) since the register job call blocks until the required storage servers are available.

What to notice: The first sentence names the figure and its finding, and the parentheses map the plotted lines to
quantities. Each deviation gets its cause ("is due to", "since we typically observe … in practice"), and the
approximation is marked (∼8 Gb/s). The paragraph ends by quantifying a counterfactual cost (up to 215 seconds) instead of
praising the design. That 53-word sentence is an outlier, and it stays readable only because it is a single if-then with
one since-clause.
