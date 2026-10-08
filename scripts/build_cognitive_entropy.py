import os
import re

base_dir = r"C:\Users\Larry\.gemini\antigravity\scratch\research-submissions\05-cognitive-entropy-framework"

bib_content = """@article{card1983psychology,
  title={The Psychology of Human-Computer Interaction},
  author={Card, Stuart K and Moran, Thomas P and Newell, Allen},
  year={1983},
  publisher={CRC Press}
}

@article{kieras2001using,
  title={Using the Keystroke-Level Model to estimate execution times},
  author={Kieras, David},
  journal={University of Michigan},
  year={2001}
}

@article{sweller2011cognitive,
  title={Cognitive load theory},
  author={Sweller, John and Ayres, Paul and Kalyuga, Slava},
  year={2011},
  publisher={Springer}
}

@article{mark2008cost,
  title={The cost of interrupted work: more speed and stress},
  author={Mark, Gloria and Gudith, Daniela and Klocke, Ulrich},
  booktitle={Proceedings of the SIGCHI Conference on Human Factors in Computing Systems},
  pages={107--110},
  year={2008}
}

@article{norman2013design,
  title={The Design of Everyday Things: Revised and Expanded Edition},
  author={Norman, Don},
  year={2013},
  publisher={Basic Books}
}
"""

with open(os.path.join(base_dir, "references.bib"), "w", encoding="utf-8") as f:
    f.write(bib_content.strip())

with open(r"C:\Users\Larry\.gemini\antigravity\scratch\research-submissions\cognitive_entropy_extracted.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Generate main.tex
main_tex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{cite}
\usepackage{geometry}
\geometry{margin=1in}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=red,
    urlcolor=blue
}

\title{\textbf{Cognitive Entropy: Measurement Framework Version 0.1 (MF-0.1)\\A Formal Engineering Construct for Coordination Overhead in Digital Workflows}}

\author{
    \textbf{Larry Arnold}\\
    LA Builds \& Independent Researcher\\
    \texttt{arnoldlarry15@github.com}
}
\date{July 12, 2026 (Revised: October 2026)}

\begin{document}

\maketitle

\begin{abstract}
Digital workflows increasingly require humans to coordinate across a proliferating landscape of applications, authentication challenges, context shifts, and interface-imposed micro-decisions to accomplish tasks that are conceptually elementary. While informally recognized as ``friction'' or ``context switching,'' this coordination burden has lacked a formal, reproducible, and falsifiable measurement framework. This specification defines \textbf{Cognitive Entropy} ($E_c$) not as a physical thermodynamic or Shannon information quantity, but as an empirical engineering construct: the normalized divergence between an observed human-system coordination process and an established empirical reference baseline required to fulfill identical user intent. Version 0.1 of this framework establishes an intent-task ontology; defines a three-tiered baseline hierarchy (Theoretical $B_t$, Empirical Reference $B_{\text{ref}}$, and Personal $B_u$) governed by the \textit{Baseline Independence Principle}; details eight candidate variables spanning structural, interaction, cognitive, and noise dimensions; and specifies mathematical falsification protocols under Construct Validity.
\end{abstract}

\vspace{1em}
\noindent \textbf{Keywords:} Cognitive Entropy, Human-Computer Interaction, Coordination Overhead, Measurement Theory, Workflow Friction, Keystroke-Level Modeling, Context Switching.

\section{Introduction and Problem Statement}
Software systems routinely impose coordination costs that bear zero intrinsic relationship to the intent a user seeks to realize. A practitioner deploying a digital service may traverse a code editor, a version control repository, cloud infrastructure dashboards, DNS panels, and payment gateways---encountering authentication challenges, permission dialogs, and configuration decisions at every junction. None of these intermediate operations reflect the user's primary intent (``publish service''); they are operational artifacts of contemporary systems architecture.

Historically, Human-Computer Interaction (HCI) has relied on task-completion metrics (GOMS/KLM) \cite{card1983psychology, kieras2001using} or subjective survey instruments (NASA-TLX). However, existing methodologies fail to isolate exogenous coordination friction from intrinsic task difficulty or individual user expertise. Without a standardized measurement construct, claims that modern tooling ``reduces friction'' cannot be verified, benchmarked across platforms, or scientifically falsified.

\section{Design Principles of MF-0.1}
The Cognitive Entropy measurement standard is governed by six foundational principles:
\begin{enumerate}
    \item \textbf{Observability:} All component variables must be strictly observable through passive screen telemetry, event logging, or verifiable protocol inspection without requiring intrusive neurological hardware.
    \item \textbf{Baseline Independence:} The Cognitive Entropy score of a workflow must be invariant to user expertise and task complexity once normalized against reference baselines.
    \item \textbf{Construct Validity:} $E_c$ must exclusively capture systemic coordination overhead, exhibiting low correlation with intrinsic task difficulty.
    \item \textbf{Bounded Normalization:} $E_c \ge 0$, where $E_c = 0$ represents optimal theoretical zero-coordination execution, and $E_c = 1.0$ designates standardized baseline performance.
    \item \textbf{Diagnostic Interpretability:} Scores must decompose into orthogonal sub-factors indicating whether friction originates from structural tool fragmentation, interaction steps, or context switching noise.
    \item \textbf{Extensibility:} The framework supports versioned evolution from provisional heuristics (MF-0.1) toward calibrated mathematical functionals.
\end{enumerate}

\section{Reference Baseline Architecture}
Measurement normalization relies on a three-tiered hierarchy:
\begin{itemize}
    \item \textbf{Theoretical Baseline ($B_t$):} The theoretical minimum coordination path physically required by information theory to satisfy intent (often $E_c = 0$, representing instant intent fulfillment).
    \item \textbf{Reference Baseline ($B_{\text{ref}}$):} The median execution path demonstrated by qualified domain experts using reference tooling under laboratory conditions:
    \begin{equation}
    B_{\text{ref}} = \text{Median}\left(X_{\text{expert}}^{(1)}, X_{\text{expert}}^{(2)}, \dots, X_{\text{expert}}^{(k)}\right)
    \end{equation}
    \item \textbf{Personal Baseline ($B_u$):} The historical baseline of an individual user, used exclusively for intra-subject longitudinal analysis.
\end{itemize}

\section{Candidate Variable Specification}
MF-0.1 establishes eight candidate observation variables categorized into four complexity tiers:

\subsection{1. Structural Complexity}
\begin{itemize}
    \item $N_{\text{apps}}$: Total count of distinct application contexts, domains, or software boundaries crossed during workflow execution.
    \item $N_{\text{auth}}$: Frequency of authentication, 2FA, token refreshes, or security boundary checkpoints encountered.
\end{itemize}

\subsection{2. Interaction Complexity}
\begin{itemize}
    \item $N_{\text{clicks}}$: Total count of physical pointer clicks, touches, and input keystrokes.
    \item $N_{\text{nav}}$: Count of navigation state transitions (page loads, menu traversals, view switches).
\end{itemize}

\subsection{3. Cognitive Complexity}
\begin{itemize}
    \item $T_{\text{pause}}$: Cumulative idle dwell time (pauses $> 2.5$ seconds) indicating cognitive hesitation, decision paralysis, or mental search.
    \item $N_{\text{context}}$: Frequency of rapid context-switching events across unrelated informational domains.
\end{itemize}

\subsection{4. Noise and Disruption}
\begin{itemize}
    \item $N_{\text{error}}$: Rate of recoverable error dialogs, invalid form entries, or aborted execution branches.
    \item $N_{\text{interrupt}}$: Frequency of unsolicited system notifications, popups, or external interruptions occurring during active workflow execution.
\end{itemize}

\section{The Cognitive Entropy Functional}
The provisional Cognitive Entropy Functional $\mathcal{E}_c(W)$ for a workflow instance $W$ relative to reference baseline $B_{\text{ref}}$ is formulated as:
\begin{equation}
E_c(W) = \sum_{i=1}^8 w_i \left( \frac{V_i(W) - V_i(B_{\text{ref}})}{\sigma_i(B_{\text{ref}})} \right)^+
\end{equation}
where $(\cdot)^+ = \max(0, \cdot)$ denotes positive deviation beyond baseline expert coordination, $\sigma_i$ is the empirical standard deviation observed during reference benchmarking, and $w_i$ represents normalized importance weights ($\sum w_i = 1$).

\section{Falsification and Construct Validity Protocols}
To establish scientific legitimacy, MF-0.1 incorporates explicit falsification criteria:
\begin{equation}
\mathcal{H}_0: \quad \text{Corr}\left(E_c, \text{Task Difficulty}\right) \ge 0.70
\end{equation}
If empirical trials demonstrate that $E_c$ merely mirrors intrinsic task complexity rather than coordination friction, the construct validity of MF-0.1 is rejected. Conversely, successful validation requires that identical intent executed across two distinct software ecosystems reflects lower $E_c$ in the workflow that removes redundant tool hopping, even when executed by novice users.

\section{Conclusion and Roadmap}
The Cognitive Entropy Framework provides the HCI and software engineering communities with a reproducible instrument to quantify digital friction. By standardizing $E_c$, industry and academia can transition from qualitative intuitions about user experience toward rigorous, empirical optimization of human-computer coordination.

\bibliographystyle{ieeetr}
\bibliography{references}

\end{document}
"""

with open(os.path.join(base_dir, "main.tex"), "w", encoding="utf-8") as f:
    f.write(main_tex)

paper_md = f"""# Cognitive Entropy: Measurement Framework Version 0.1 (MF-0.1)

**A Formal Engineering Construct for Coordination Overhead in Digital Workflows**

**Author:** Larry Arnold  
**Affiliation:** LA Builds & Independent Researcher  
**Date:** July 12, 2026 (Revised: October 2026)  
**Target Venue:** ACM SIGCHI / IEEE Transactions on Human-Machine Systems, arXiv (`cs.HC` / `cs.CY`)  
**Status:** Provisional Research Standard & Working Specification  

---

## Abstract

Digital workflows increasingly require humans to coordinate across a proliferating landscape of applications, authentication challenges, context shifts, and interface-imposed micro-decisions to accomplish tasks that are conceptually elementary. While informally recognized as "friction" or "context switching," this coordination burden has lacked a formal, reproducible, and falsifiable measurement framework.

This specification defines **Cognitive Entropy** ($E_c$) not as a physical thermodynamic or Shannon information quantity, but as an empirical engineering construct: the normalized divergence between an observed human-system coordination process and an established empirical reference baseline required to fulfill identical user intent. Version 0.1 of this framework establishes an intent-task ontology; defines a three-tiered baseline hierarchy (Theoretical $B_t$, Empirical Reference $B_{{\\text{{ref}}}}$, and Personal $B_u$) governed by the *Baseline Independence Principle*; details eight candidate variables spanning structural, interaction, cognitive, and noise dimensions; and specifies mathematical falsification protocols under Construct Validity.

---

## 1. System Ontology & Motivation

```mermaid
flowchart LR
    Intent[User Intent\ne.g. 'Publish Web App'] --> Coordination[Coordination Overhead\nApps, Logins, Navigations, Context Switches]
    Coordination --> Realization[Intent Realization]
    Coordination -.-> Ec[Cognitive Entropy Measurement\nEc = Divergence from Baseline]
```

Modern digital knowledge work is characterized by acute coordination inflation. A simple intent requires traversing multiple authentication gates, tab switches, configuration dialogues, and disconnected software systems. Existing tools (GOMS/KLM, NASA-TLX) fail to separate **intrinsic task difficulty** from **systemic coordination friction**.

---

## 2. Design Principles

1. **Observability:** All variables must be strictly observable via passive telemetry and event logging without intrusive biometric hardware.
2. **Baseline Independence:** Normalization ensures $E_c$ scores reflect tool overhead rather than user intelligence or typing speed.
3. **Construct Validity:** $E_c$ must isolate coordination friction from intrinsic task difficulty.
4. **Bounded Normalization:** $E_c = 0$ represents optimal zero-coordination execution; $E_c = 1.0$ represents standardized baseline.
5. **Diagnostic Interpretability:** Decomposes into orthogonal components (structural, interactional, cognitive, and noise).

---

## 3. The Three-Tier Baseline Framework

- **Theoretical Baseline ($B_t$):** The theoretical zero-friction coordination lower bound.
- **Reference Baseline ($B_{{\\text{{ref}}}}$):** Median performance of verified domain experts under controlled reference tooling:
  $$B_{{\\text{{ref}}}} = \\text{{Median}}\\left(X_{{\\text{{expert}}}}^{{(1)}}, X_{{\\text{{expert}}}}^{{(2)}}, \\dots, X_{{\\text{{expert}}}}^{{(k)}}\\right)$$
- **Personal Baseline ($B_u$):** Individual historical average used for longitudinal tracking.

---

## 4. The Eight Candidate Variables

| Dimension | Variable | Description |
| :--- | :--- | :--- |
| **Structural** | $N_{{\\text{{apps}}}}$ | Total count of distinct application/domain context switches |
| **Structural** | $N_{{\\text{{auth}}}}$ | Number of security checkpoints, 2FA prompts, and token gates |
| **Interaction** | $N_{{\\text{{clicks}}}}$ | Total pointer clicks, touches, and keyboard input sequences |
| **Interaction** | $N_{{\\text{{nav}}}}$ | Menu transitions, view changes, and routing state switches |
| **Cognitive** | $T_{{\\text{{pause}}}}$ | Dwell time pauses (>2.5s) indicating hesitation or mental search |
| **Cognitive** | $N_{{\\text{{context}}}}$ | Rapid shifts across unrelated informational domains |
| **Noise** | $N_{{\\text{{error}}}}$ | Corrective actions, form validation failures, backtracks |
| **Noise** | $N_{{\\text{{interrupt}}}}$ | Unsolicited popups, notifications, and banners during flow |

---

## 5. The Cognitive Entropy Functional

The provisional Cognitive Entropy Functional $\\mathcal{{E}}_c(W)$ is formulated as:

$$E_c(W) = \\sum_{{i=1}}^8 w_i \\left( \\frac{{V_i(W) - V_i(B_{{\\text{{ref}}}})}}{{\\sigma_i(B_{{\\text{{ref}}}})}} \\right)^+$$

where $(z)^+ = \\max(0, z)$ measures positive friction beyond the reference baseline, $\\sigma_i$ is empirical baseline variance, and $\\sum w_i = 1$.

---

## 6. Falsification & Construct Validity

The framework establishes an explicit falsification hypothesis:

$$\\mathcal{{H}}_0: \\quad \\text{{Corr}}\\left(E_c, \\text{{Task Difficulty}}\\right) \\ge 0.70$$

If empirical evaluation reveals that $E_c$ tracks intrinsic task difficulty rather than external coordination overhead, the model is rejected.

---

## References

1. S. K. Card, T. P. Moran, and A. Newell, *The Psychology of Human-Computer Interaction*, CRC Press (1983).
2. D. Kieras, *Using the Keystroke-Level Model to Estimate Execution Times*, University of Michigan (2001).
3. J. Sweller, P. Ayres, and S. Kalyuga, *Cognitive Load Theory*, Springer (2011).
4. G. Mark, D. Gudith, and U. Klocke, "The cost of interrupted work: More speed and stress," *Proceedings of ACM SIGCHI*, 107–110 (2008).
5. D. Norman, *The Design of Everyday Things*, Basic Books (2013).
"""

with open(os.path.join(base_dir, "paper.md"), "w", encoding="utf-8") as f:
    f.write(paper_md)

print("Wrote Cognitive Entropy main.tex, paper.md, and references.bib successfully!")
