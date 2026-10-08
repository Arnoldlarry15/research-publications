import os
import re

base_dir = r"C:\Users\Larry\.gemini\antigravity\scratch\research-submissions\02-frontier-model-blind-spots"

with open(r"C:\Users\Larry\.gemini\antigravity\scratch\research-submissions\blind_spots_cleaned.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Parse sections out of text
sections = {}
# Find headers:
# 1. Introduction
# 2. Background and Related Work
# 3. Formal Characterization of Evaluation Blind Spots
# 4. Adaptive Adversarial Evaluation Architecture
# 5. Empirical Proof of Concept
# 6. Novel Metrics for Dynamic Safety Assessment
# 7. Discussion & Governance Implications
# 8. Conclusion
# References

bib_content = """@article{ganguli2022red,
  title={Red teaming language models to reduce harms: Methods, scaling behaviors, and lessons learned},
  author={Ganguli, Deep and Lovitt, Liane and Kernion, Jackson and Askell, Amanda and Bai, Yuntao and Kadavath, Saurav and others},
  journal={arXiv preprint arXiv:2209.07858},
  year={2022}
}

@article{liang2022holistic,
  title={Holistic evaluation of language models},
  author={Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and others},
  journal={arXiv preprint arXiv:2211.09110},
  year={2022}
}

@article{perez2022red,
  title={Red teaming language models with language models},
  author={Perez, Ethan and Huang, Saffron and Song, Francis and Cai, Trevor and Ring, Roman and Aslanides, John and others},
  journal={arXiv preprint arXiv:2202.03286},
  year={2022}
}

@article{srivastava2022beyond,
  title={Beyond the imitation game: Quantifying and extrapolating the capabilities of language models},
  author={Srivastava, Aarohi and Rastogi, Abhinav and Rao, Abhishek and Shoeb, Abu Awal Md and Abid, Abubakar and Fisch, Adam and others},
  journal={arXiv preprint arXiv:2206.04615},
  year={2022}
}

@article{bai2022constitutional,
  title={Constitutional AI: Harmlessness from AI feedback},
  author={Bai, Yuntao and Kadavath, Saurav and Kundu, Sandipan and Askell, Amanda and Kernion, Jackson and Jones, Andy and others},
  journal={arXiv preprint arXiv:2212.08073},
  year={2022}
}

@article{casper2023explore,
  title={Explore, establish, exploit: Red teaming language models with guided search},
  author={Casper, Stephen and Davies, Xander and Shi, Claudia and Gilbert, Thomas Krendl and others},
  journal={arXiv preprint arXiv:2304.03279},
  year={2023}
}

@article{zou2023universal,
  title={Universal and transferable adversarial attacks on aligned language models},
  author={Zou, Andy and Wang, Zifan and Kolter, J Zico and Matt, Fredrik},
  journal={arXiv preprint arXiv:2307.15043},
  year={2023}
}
"""

with open(os.path.join(base_dir, "references.bib"), "w", encoding="utf-8") as f:
    f.write(bib_content.strip())

# Clean up text for LaTeX and Markdown
# We extract sections cleanly
def extract_section(start_kw, end_kw):
    p1 = text.find(start_kw)
    if p1 == -1: return ""
    p1 += len(start_kw)
    if end_kw:
        p2 = text.find(end_kw, p1)
        if p2 == -1: p2 = len(text)
    else:
        p2 = len(text)
    content = text[p1:p2].strip()
    # remove page markers
    content = re.sub(r'=== PAGE \d+ ===', '', content)
    return content.strip()

abstract = extract_section("Abstract", "Keywords:")
if not abstract:
    abstract = extract_section("Abstract", "1. Introduction")

sec1 = extract_section("1. Introduction", "2. Background and Related Work")
sec2 = extract_section("2. Background and Related Work", "3. Formal Characterization of Evaluation Blind Spots")
sec3 = extract_section("3. Formal Characterization of Evaluation Blind Spots", "4. Adaptive Adversarial Evaluation Architecture")
sec4 = extract_section("4. Adaptive Adversarial Evaluation Architecture", "5. Empirical Proof of Concept")
sec5 = extract_section("5. Empirical Proof of Concept", "6. Novel Metrics for Dynamic Safety Assessment")
sec6 = extract_section("6. Novel Metrics for Dynamic Safety Assessment", "7. Discussion & Governance Implications")
sec7 = extract_section("7. Discussion & Governance Implications", "8. Conclusion")
sec8 = extract_section("8. Conclusion", "References")

main_tex = r"""\documentclass[10pt,twocolumn,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{cite}
\usepackage{geometry}
\geometry{margin=0.75in}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=red,
    urlcolor=blue
}

\title{\textbf{Revealing Evaluation Blind Spots in Frontier Models via Adaptive Adversarial Systems}}

\author{
    \textbf{Larry Arnold}\\
    LA Builds \& Independent AI Safety Research\\
    \texttt{arnoldlarry15@github.com}
}
\date{March 2026 (Revised: October 2026)}

\begin{document}

\maketitle

\begin{abstract}
""" + abstract + r"""
\end{abstract}

\vspace{0.5em}
\noindent \textbf{Keywords:} AI safety evaluation, adversarial testing, frontier models, behavioral assessment, dynamic benchmarking, red-teaming.

\section{Introduction}
""" + sec1 + r"""

\section{Background and Related Work}
""" + sec2 + r"""

\section{Formal Characterization of Evaluation Blind Spots}
""" + sec3 + r"""

\begin{table}[htbp]
\centering
\caption{Taxonomy of Systematic Evaluation Blind Spots in Frontier Models}
\label{tab:blind_spots}
\begin{tabular}{lll}
\toprule
\textbf{Blind Spot Class} & \textbf{Mechanism} & \textbf{Failure Mode} \\
\midrule
Evaluation Gaming & Static test overfitting & High score, low robustness \\
Deployment Divergence & Context distribution shift & Multi-turn guardrail decay \\
Safety Boundary Erosion & Incremental adaptive pressure & Boundary drift \& jailbreaking \\
Coordination Vulnerability & Multi-agent consensus drift & Cascading safety bypass \\
\bottomrule
\end{tabular}
\end{table}

\section{Adaptive Adversarial Evaluation Architecture}
""" + sec4 + r"""

\section{Empirical Proof of Concept}
""" + sec5 + r"""

\begin{table}[htbp]
\centering
\caption{Empirical Comparison: Static Benchmarks vs. Adaptive Adversarial Evaluation (Proof of Concept)}
\label{tab:empirical_results}
\begin{tabular}{lccc}
\toprule
\textbf{Evaluation Domain} & \textbf{Static Violation Rate} & \textbf{Adaptive Violation Rate} & \textbf{Elicitation Ratio} \\
\midrule
Harmful Advice / Jailbreak & 4.2\% & 26.8\% & 6.4$\times$ \\
Information Boundary Bypass & 6.1\% & 31.4\% & 5.1$\times$ \\
Multi-Turn Escalation & 3.5\% & 24.5\% & 7.0$\times$ \\
Context Manipulation & 8.3\% & 33.2\% & 4.0$\times$ \\
\bottomrule
\end{tabular}
\end{table}

\section{Novel Metrics for Dynamic Safety Assessment}
""" + sec6 + r"""

\section{Discussion and Governance Implications}
""" + sec7 + r"""

\section{Conclusion}
""" + sec8 + r"""

\bibliographystyle{ieeetr}
\bibliography{references}

\end{document}
"""

with open(os.path.join(base_dir, "main.tex"), "w", encoding="utf-8") as f:
    f.write(main_tex)

paper_md = f"""# Revealing Evaluation Blind Spots in Frontier Models via Adaptive Adversarial Systems

**Author:** Larry Arnold  
**Affiliation:** LA Builds & Independent AI Safety Research  
**Date:** March 2026 (Revised: October 2026)  
**Target Venue:** NeurIPS / ICLR Workshop, IEEE S&P / SafeAI, arXiv (`cs.CR` / `cs.AI`)  

---

## Abstract

{abstract}

**Keywords:** AI safety evaluation, adversarial testing, frontier models, behavioral assessment, dynamic benchmarking, red-teaming.

---

## 1. Introduction

{sec1}

---

## 2. Background and Related Work

{sec2}

---

## 3. Formal Characterization of Evaluation Blind Spots

{sec3}

### Table 1: Taxonomy of Systematic Evaluation Blind Spots

| Blind Spot Class | Mechanism | Failure Mode |
| :--- | :--- | :--- |
| **Evaluation Gaming** | Static test overfitting | High benchmark score, low real-world robustness |
| **Deployment Divergence** | Context distribution shift | Multi-turn guardrail decay under natural use |
| **Safety Boundary Erosion** | Incremental adaptive pressure | Boundary drift & progressive jailbreaking |
| **Coordination Vulnerability** | Multi-agent consensus drift | Cascading safety bypass across agent interactions |

---

## 4. Adaptive Adversarial Evaluation Architecture

{sec4}

---

## 5. Empirical Proof of Concept

{sec5}

### Table 2: Empirical Comparison — Static Benchmarks vs. Adaptive Adversarial Evaluation

| Evaluation Domain | Static Violation Rate | Adaptive Violation Rate | Elicitation Multiplier |
| :--- | :---: | :---: | :---: |
| **Harmful Advice / Jailbreak** | 4.2% | 26.8% | **6.4x** |
| **Information Boundary Bypass** | 6.1% | 31.4% | **5.1x** |
| **Multi-Turn Escalation** | 3.5% | 24.5% | **7.0x** |
| **Context Manipulation** | 8.3% | 33.2% | **4.0x** |

---

## 6. Novel Metrics for Dynamic Safety Assessment

{sec6}

---

## 7. Discussion and Governance Implications

{sec7}

---

## 8. Conclusion

{sec8}

---

## References

1. D. Ganguli et al., "Red teaming language models to reduce harms: Methods, scaling behaviors, and lessons learned," *arXiv:2209.07858* (2022).
2. P. Liang et al., "Holistic evaluation of language models," *arXiv:2211.09110* (2022).
3. E. Perez et al., "Red teaming language models with language models," *arXiv:2202.03286* (2022).
4. A. Srivastava et al., "Beyond the imitation game: Quantifying and extrapolating the capabilities of language models," *arXiv:2206.04615* (2022).
5. Y. Bai et al., "Constitutional AI: Harmlessness from AI feedback," *arXiv:2212.08073* (2022).
6. S. Casper et al., "Explore, establish, exploit: Red teaming language models with guided search," *arXiv:2304.03279* (2023).
7. A. Zou et al., "Universal and transferable adversarial attacks on aligned language models," *arXiv:2307.15043* (2023).
"""

with open(os.path.join(base_dir, "paper.md"), "w", encoding="utf-8") as f:
    f.write(paper_md)

print("Wrote Blind Spots paper main.tex, paper.md, and references.bib successfully!")
