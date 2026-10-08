import os

base_dir = r"C:\Users\Larry\.gemini\antigravity\scratch\research-submissions\04-sourceos-system-planning"

bib_content = """@article{sweller1988cognitive,
  title={Cognitive load during problem solving: Effects on learning},
  author={Sweller, John},
  journal={Cognitive Science},
  volume={12},
  number={2},
  pages={257--285},
  year={1988}
}

@book{simon1971designing,
  title={Designing Organizations for an Information-Rich World},
  author={Simon, Herbert A},
  year={1971},
  publisher={Johns Hopkins University Press}
}

@book{allen2001getting,
  title={Getting Things Done: The Art of Stress-Free Productivity},
  author={Allen, David},
  year={2001},
  publisher={Penguin}
}

@article{horvitz1999principles,
  title={Principles of mixed-initiative user interfaces},
  author={Horvitz, Eric},
  journal={Proceedings of the SIGCHI conference on Human Factors in Computing Systems},
  pages={159--166},
  year={1999}
}

@article{baddeley1992working,
  title={Working memory},
  author={Baddeley, Alan},
  journal={Science},
  volume={255},
  number={5044},
  pages={556--559},
  year={1992}
}
"""

with open(os.path.join(base_dir, "references.bib"), "w", encoding="utf-8") as f:
    f.write(bib_content.strip())

main_tex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{cite}
\usepackage{listings}
\usepackage{geometry}
\geometry{margin=1in}

\title{\textbf{SourceOS: A Cognitive Pipeline and Attention Allocation Engine\\for Human Executive Function Augmentation}}

\author{
    \textbf{Larry Arnold}\\
    Founder, LA Builds \& Systems Architect\\
    \texttt{arnoldlarry15@github.com}
}
\date{June 2026 (Revised: October 2026)}

\begin{document}

\maketitle

\begin{abstract}
Contemporary personal productivity tools exacerbate cognitive fragmentation by shifting the burden of taxonomic organization---tagging, folder filing, calendar scheduling, and status tracking---onto the user. In contrast, biological human executive function relies on continuous selective attention, automatic salience filtering, and the dynamic decay of low-priority mental states. We present \textbf{SourceOS}, an AI-native system architecture designed to act as an externalized prefrontal cortex. SourceOS implements a five-stage cognitive pipeline: unconstrained multimodal stream-of-consciousness capture, automatic ontological entity extraction into six primitive schema classes (Thought, Task, Idea, Goal, Commitment, Person), temporal memory decay modeling, and multi-objective attention ranking. Rather than maximizing task completion metrics or organizational complexity, SourceOS optimizes for \textit{cognitive relief}---explicitly identifying what to ignore, calculating unresolved mental load, and dynamically synthesizing the single highest-leverage next action. We define the system ontology, formal priority scoring function, graph decay mathematics, and reference implementation architecture.
\end{abstract}

\vspace{1em}
\noindent \textbf{Keywords:} Cognitive architecture, Attention allocation, Human-AI interaction, Executive function, Semantic memory decay, Personal knowledge graphs.

\section{Introduction}
Herbert Simon famously observed that ``a wealth of information creates a poverty of attention'' \cite{simon1971designing}. Over five decades later, digital tools routinely demand that users spend significant working memory maintaining metadata across multiple disjointed productivity silos. 

Current note-taking, project management, and task systems fail because they treat human cognition as a relational database. Users are forced to classify unformed thoughts into rigid hierarchies before their meaning has stabilized. This produces friction, context switching, and mental fatigue \cite{sweller1988cognitive, baddeley1992working}.

\textbf{SourceOS} inverts this paradigm. Instead of demanding that the user structure information to serve software, SourceOS ingests raw cognitive entropy and applies machine reasoning to perform the executive labor of filtering, contextualizing, prioritizing, and surfacing action.

\section{The Cognitive Pipeline}
The SourceOS execution pipeline operates across five continuous stages:
\begin{enumerate}
    \item \textbf{Frictionless Multimodal Ingestion:} High-bandwidth, zero-classification capture via hotkeys, speech-to-text streams, or raw markdown notes.
    \item \textbf{Semantic Decomposition and Ontological Mapping:} An LLM parser deconstructs the unstructured stream into discrete cognitive entities, extracting latent intent, implicit urgency, emotional tone, and referenced entities.
    \item \textbf{Dynamic Semantic Graph with Memory Decay:} Extracted entities populate a directed knowledge graph where edge weights decay over time according to an Ebbinghaus-inspired temporal curve.
    \item \textbf{Attention Allocation and Ranking Engine:} Computes multi-factor priority scores based on active user themes, deadlines, contextual relevance, and accumulated cognitive debt.
    \item \textbf{Executive Reflection and Surface Synthesis:} Translates complex internal state into three concise outputs: \textit{Today's Focus}, \textit{Next Best Action}, and \textit{Unresolved Mental Load}.
\end{enumerate}

\section{Cognitive Object Ontology}
Every input object is resolved into one of six core ontological classes:
\begin{itemize}
    \item \textbf{Thought:} Ephemeral observations, affective states, or reflections. Requires no execution; serves as contextual background.
    \item \textbf{Task:} Actionable commitments with verifiable completion states.
    \item \textbf{Idea:} Generative hypotheses, product sketches, or creative concepts requiring incubation.
    \item \textbf{Goal:} Macroscopic desired outcomes that anchor and weight associated tasks.
    \item \textbf{Commitment:} Social contracts and explicit obligations made to external stakeholders.
    \item \textbf{Person:} Human relationships, collaborators, and contact contexts linked to obligations.
\end{itemize}

\section{Attention Ranking and Priority Dynamics}
SourceOS replaces static priority tags (e.g., High/Medium/Low) with a continuous dynamic priority functional $\mathcal{P}(O, t)$:
\begin{equation}
\mathcal{P}(O, t) = w_I \cdot \mathcal{I}(O) + w_U \cdot \mathcal{U}(O, t) + w_A \cdot \mathcal{A}(O, \mathcal{G}_{\text{themes}}) + w_E \cdot \mathcal{E}(O) - \lambda \cdot \Delta t
\end{equation}
where:
\begin{itemize}
    \item $\mathcal{I}(O) \in [0, 1]$: Intrinsic importance derived from goal hierarchy alignment.
    \item $\mathcal{U}(O, t)$: Temporal urgency modeled as hyperbolic discounting toward deadline $t_d$:
    \begin{equation}
    \mathcal{U}(O, t) = \frac{1}{1 + \gamma (t_d - t)}
    \end{equation}
    \item $\mathcal{A}(O, \mathcal{G}_{\text{themes}})$: Cosine similarity between the object vector embedding and active user thematic goals.
    \item $\mathcal{E}(O)$: Emotional friction / cognitive weight score (stress footprint).
    \item $\lambda \cdot \Delta t$: Temporal decay attenuation for dormant thoughts that lack active reinforcement.
\end{itemize}

\section{The Unresolved Mental Load Engine}
A distinguishing architectural property of SourceOS is its quantification of latent cognitive debt:
\begin{equation}
\mathcal{L}_{\text{mental}}(t) = \sum_{O_i \in \text{Unresolved}} \mathcal{E}(O_i) \cdot \ln(1 + \Delta t_i)
\end{equation}
By surfacing items that are perpetually deferred yet generate ongoing background anxiety, SourceOS prompts active resolution: execute, delegate, or consciously archive.

\section{System Architecture and Implementation}

\begin{table}[htbp]
\centering
\caption{Architectural Subsystems of the SourceOS Platform}
\label{tab:sourceos_arch}
\begin{tabular}{lll}
\toprule
\textbf{Subsystem} & \textbf{Core Function} & \textbf{Technology Stack} \\
\midrule
Capture Ingress Gateway & Low-latency raw input ingestion & FastAPI, WebSockets, Whisper API \\
Cognitive Parser & Entity extraction \& classification & Claude / GPT-4o structured JSON \\
Vector Memory Store & Semantic retrieval \& theme alignment & pgvector / Qdrant, OpenAI \texttt{text-embedding-3} \\
Ranking Engine & Dynamic attention prioritization & Asynchronous Python execution \\
Executive Dashboard & Minimalist reflection interface & Next.js, Tailwind CSS, TypeScript \\
\bottomrule
\end{tabular}
\end{table}

\section{Conclusion}
SourceOS shifts the locus of computing from passive information repository to active executive partner. By automating extraction, modeling memory decay, and mathematically optimizing attention allocation, SourceOS protects human focus, reduces decision fatigue, and translates chaotic internal thoughts into focused external momentum.

\bibliographystyle{ieeetr}
\bibliography{references}

\end{document}
"""

with open(os.path.join(base_dir, "main.tex"), "w", encoding="utf-8") as f:
    f.write(main_tex)

paper_md = """# SourceOS: Systems Architecture & Cognitive Engine Specification

**Author:** Larry Arnold  
**Affiliation:** Founder, LA Builds & Systems Architect  
**Date:** June 2026 (Revised: October 2026)  
**Target Venue:** Systems Architecture Whitepaper, ACM SIGCHI / Human-AI Interaction, Open Systems Specification  

---

## Executive Summary

Current productivity and knowledge tools force humans to act like database administrators for their own thoughts—demanding manual categorization, tagging, folder filing, and schedule juggling. This imposes substantial cognitive friction.

**SourceOS** is an AI-native system architecture designed to act as an externalized **digital prefrontal cortex**. SourceOS implements a continuous five-stage cognitive pipeline: frictionless capture of unconstrained thoughts, automated ontological extraction into six primitive schema classes (Thought, Task, Idea, Goal, Commitment, Person), temporal memory decay modeling, and multi-factor attention allocation. Rather than optimizing for organizational complexity, SourceOS optimizes for **cognitive relief**—explicitly surfacing what to ignore, calculating latent mental load, and generating the single highest-leverage next action.

---

## 1. Architectural Pipeline

```mermaid
flowchart TD
    Raw[Raw Stream of Consciousness\nVoice / Text / Quick Capture] --> Ingest[Ingestion Gateway]
    Ingest --> Parser[Semantic Parser & Entity Extractor\nLLM Structured JSON]
    Parser --> Graph[Cognitive Knowledge Graph\nSemantic Objects & Decay Dynamics]
    Graph --> Rank[Dynamic Attention Allocation Engine\nPriority Functional P]
    Rank --> Out1[Today's Focus: Top Priorities]
    Rank --> Out2[Next Best Action: Contextualized]
    Rank --> Out3[Unresolved Mental Load: Latent Debt]
```

1. **Frictionless Ingestion:** Zero-classification entry. Auto-focused single-line capture accepting rapid thoughts, stream-of-consciousness drafts, or voice audio transcripts.
2. **Semantic Extraction:** Deconstructs inputs into discrete typed objects with inferred urgency, goal relationships, and cognitive friction scores.
3. **Graph Storage & Temporal Decay:** Nodes decay naturally over time unless reinforced, mimicking biological working memory retention.
4. **Attention Ranking:** Balances deadlines, theme relevance, and emotional drag.
5. **Executive Action Surface:** Synthesizes clear guidance without overwhelming dashboards.

---

## 2. Ontological Schema

Every parsed item is instantiated as an instance of one of six core classes:

| Class | Semantics | Lifecycle Behavior |
| :--- | :--- | :--- |
| **Thought** | Ephemeral reflections, observations | Decays quickly; acts as ambient background context |
| **Task** | Actionable units of execution | Has completion criteria, urgency curves, and dependencies |
| **Idea** | Creative concepts, architectural sparks | Incubates; connects via semantic similarity to goals |
| **Goal** | High-level macroscopic outcomes | Anchors task trees; provides importance weighting |
| **Commitment** | Obligations made to external stakeholders | Carries high social accountability weight |
| **Person** | Collaborators, team members, contacts | Linked to tasks, meetings, and commitments |

---

## 3. Attention Allocation & Priority Functional

Priority is not a static flag (Low/Medium/High). It is computed continuously as:

$$\\mathcal{P}(O, t) = w_I \\cdot \\mathcal{I}(O) + w_U \\cdot \\mathcal{U}(O, t) + w_A \\cdot \\mathcal{A}(O, \\mathcal{G}_{\\text{themes}}) + w_E \\cdot \\mathcal{E}(O) - \\lambda \\cdot \\Delta t$$

Where:
- $\\mathcal{I}(O) \\in [0, 1]$: Intrinsic importance linked to top-level active goals.
- $\\mathcal{U}(O, t)$: Temporal urgency with hyperbolic deadline discounting:
  $$\\mathcal{U}(O, t) = \\frac{1}{1 + \\gamma (t_{\\text{deadline}} - t)}$$
- $\\mathcal{A}(O, \\mathcal{G}_{\\text{themes}})$: Cosine similarity between entity embedding and active strategic focus areas.
- $\\mathcal{E}(O)$: Emotional drag / cognitive friction score.
- $\\lambda \\Delta t$: Natural decay discount for stale thoughts.

---

## 4. The Unresolved Mental Load Metric

SourceOS tracks cumulative unaddressed cognitive debt:

$$\\mathcal{L}_{\\text{mental}}(t) = \\sum_{O_i \\in \\text{Unresolved}} \\mathcal{E}(O_i) \\cdot \\ln(1 + \\Delta t_i)$$

This isolates tasks and commitments that have lingered without resolution, prompting the user with explicit actions: **Execute now**, **Delegate**, or **Consciously Archive**.

---

## 5. Reference Implementation Stack

- **Ingress Gateway:** FastAPI / Node.js WebSocket stream receiver.
- **LLM Decomposition:** Claude 3.5 Sonnet / GPT-4o structured extraction prompts.
- **Vector & Graph Engine:** PostgreSQL with `pgvector` for semantic embeddings + relational graph schema.
- **Executive Frontend:** Minimalist Next.js / Tailwind desktop view focused on clarity and low visual noise.

---

## References

1. J. Sweller, "Cognitive load during problem solving: Effects on learning," *Cognitive Science*, 12(2):257–285 (1988).
2. H. A. Simon, *Designing Organizations for an Information-Rich World*, Johns Hopkins University Press (1971).
3. D. Allen, *Getting Things Done: The Art of Stress-Free Productivity*, Penguin (2001).
4. E. Horvitz, "Principles of mixed-initiative user interfaces," *Proceedings of ACM SIGCHI*, 159–166 (1999).
5. A. Baddeley, "Working memory," *Science*, 255(5044):556–559 (1992).
"""

with open(os.path.join(base_dir, "spec.md"), "w", encoding="utf-8") as f:
    f.write(paper_md)

print("Wrote SourceOS main.tex, spec.md, and references.bib successfully!")
