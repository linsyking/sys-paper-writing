# Sources and Provenance

Reviewed on **2026-10-13**. This is a selected writing corpus, not an exhaustive survey or evidence that a particular template causes acceptance. The section guides are editorial synthesis; paper-specific observations live in the example notes. Use primary sources to verify technical or quantitative claims before reusing them.

## Paper corpus

The following PDFs were downloaded for review outside the repository. Motivation, design/implementation, and evaluation passages were inspected. The repository contains links and original paraphrased notes; it does not redistribute PDFs, extracted full text, figures, or copied paper prose. Section numbers below refer to the linked paper versions, not PDF viewer page numbers.

| Paper | Venue | Primary record / reviewed PDF | Writing notes |
| --- | --- | --- | --- |
| Zhong et al., **DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving** | OSDI 2024 | [USENIX](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) · [PDF](https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf) | [DistServe](examples/distserve.md) |
| Ren et al., **Enabling Efficient GPU Communication over Multiple NICs with FuseLink** | OSDI 2025 | [USENIX](https://www.usenix.org/conference/osdi25/presentation/ren) · [PDF](https://www.usenix.org/system/files/osdi25-ren.pdf) | [FuseLink](examples/fuselink.md) |
| Jiang et al., **Training with Confidence: Catching Silent Errors in Deep Learning Training with Automated Proactive Checks** | OSDI 2025 | [USENIX](https://www.usenix.org/conference/osdi25/presentation/jiang) · [PDF](https://www.usenix.org/system/files/osdi25-jiang.pdf) | [TrainCheck](examples/traincheck.md) |
| Xie et al., **Strata: Hierarchical Context Caching for Long Context Language Model Serving** | OSDI 2026 | [USENIX](https://www.usenix.org/conference/osdi26/presentation/xie-zhiqiang) · [PDF](https://www.usenix.org/system/files/osdi26-xie-zhiqiang.pdf) | [Strata](examples/strata.md) |
| Strati et al., **Sailor: Automating Distributed Training over Dynamic, Heterogeneous, and Geo-distributed Clusters** | SOSP 2025 | [DOI](https://doi.org/10.1145/3731569.3764839) · [Author PDF](https://fotstrt.github.io/files/2025-sailor.pdf) | [Sailor](examples/sailor.md) |
| Guan et al., **Mercury: Unlocking Multi-GPU Operator Optimization for LLMs via Remote Memory Scheduling** | SOSP 2025 | [DOI](https://doi.org/10.1145/3731569.3764798) · [Public manuscript](https://par.nsf.gov/servlets/purl/10661231) | [Mercury](examples/mercury.md) |

The SOSP 2025 venue assignments can also be checked in the [official accepted-paper list](https://sigops.org/s/conferences/sosp/2025/accepted.html). Historical baselines and hardware in these papers should not be assumed current. When adding a case study, record its version/source and section locators, distinguish observation from editorial advice, and avoid copying source prose or lifting unqualified headline numbers.

## Venue guidance

The reviewed [OSDI 2026 CFP](https://www.usenix.org/conference/osdi26/call-for-papers) and [SOSP 2026 CFP](https://sigops.org/s/conferences/sosp/2026/cfp.html) emphasize significant problems, compelling systems contributions, practicality, clarity, and correctness. These support the skill's general focus; individual design/evaluation recommendations are writing guidance.

OSDI 2026 distinguishes Research and Operational Systems tracks; the latter accepts operational insight without requiring novel research ideas. Its [CFP](https://www.usenix.org/conference/osdi26/call-for-papers) also changes author-response and review procedures relative to earlier editions. Do not treat these details as rules for another year or for SOSP.

For an actual submission check, consult the requested edition's CFP, author instructions, template, and artifact instructions. Verify track, length/format, anonymity, supplementary material, permitted AI assistance, and response/shepherding rules when relevant. State the source and year of any specific requirement. If those instructions cannot be verified, mark the requirement as unverified rather than claiming compliance.

## Original repository attribution

The original ML/CV/NLP writing skill was curated from Prof. Peng Sida (彭思达)'s [open study notes](https://pengsida.notion.site/c1a22465a0fa4b15a12985223916048e) and [learning_research repository](https://github.com/pengsida/learning_research). This adaptation retains the general emphasis on paper logic, paragraph clarity, and reverse outlining. Systems-specific guides and the replacement examples are newly written; do not attribute their technical recommendations to Prof. Peng or imply endorsement by him or the cited authors.

The repository's [MIT license](../../LICENSE) covers its original code/documentation under its terms. Linked publications and upstream materials retain their own copyrights and licenses.
