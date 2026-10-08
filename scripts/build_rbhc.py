import os
import re

base_dir = r"C:\Users\Larry\.gemini\antigravity\scratch\research-submissions\01-rbhc-cosmology"
tex_src = r"C:\Users\Larry\Downloads\rbhc-paper\rbhc-paper"

def read_file(name):
    p = os.path.join(tex_src, name)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            return f.read().strip()
    return ""

abstract_txt = read_file("abstract.tex")
intro_txt = read_file("introduction.tex")
framework_txt = read_file("framework.tex")
predictions_txt = read_file("predictions.tex")
comparison_txt = read_file("comparison.tex")
philosophy_txt = read_file("philosophy.tex")
futurework_txt = read_file("futurework.tex")
conclusion_txt = read_file("conclusion.tex")

def clean_dup_headers(txt):
    txt = re.sub(r"\\section\{[^}]+\}", "", txt)
    txt = re.sub(r"^[0-9]\.?\s+[A-Za-z\s]+\n", "", txt)
    return txt.strip()

intro_clean = clean_dup_headers(intro_txt)
framework_clean = clean_dup_headers(framework_txt)
predictions_clean = clean_dup_headers(predictions_txt)
comparison_clean = clean_dup_headers(comparison_txt)
philosophy_clean = clean_dup_headers(philosophy_txt)
futurework_clean = clean_dup_headers(futurework_txt)
conclusion_clean = clean_dup_headers(conclusion_txt)

main_tex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{cite}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{margin=1in}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=red,
    urlcolor=blue
}

\title{\textbf{Recursive Black Hole Cosmology:\\A Boundary-Driven Framework for Time, Space, and Information}}

\author{
    \textbf{Larry Arnold}\\
    Independent Researcher in Theoretical Physics, Information Theory, and Machine Learning\\
    LA Builds\\
    \texttt{arnoldlarry15@github.com}
}
\date{July 2025 (Revised: October 2026)}

\begin{document}

\maketitle

\begin{abstract}
""" + abstract_txt + r"""
\end{abstract}

\vspace{1em}
\noindent \textbf{Keywords:} Black hole cosmology, Holographic principle, Quantum gravity, Information theory, Metric inversion, Dark energy, Emergent spacetime.

\section{Introduction}
""" + intro_clean + r"""

\section{Core Theoretical Framework}
""" + framework_clean + r"""

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth]{figures/recursion_diagram.png}
    \caption{Hierarchical architecture of nested universes: parent black hole collapse generates child spacetime interior manifolds recursively unfolding inward.}
    \label{fig:recursion_diagram}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth]{figures/boundary_encoding.png}
    \caption{Holographic boundary encoding at the event horizon. Information is mapped via boundary degrees of freedom into bulk emergent spacetime.}
    \label{fig:boundary_encoding}
\end{figure}

\section{Mathematical Foundations of Recursive Metric and Information Dynamics}
\subsection{Parent-Child Metric Transformation}
Consider a rotating Kerr black hole in a parent universe of recursion index $n-1$, parameterized in Boyer-Lindquist coordinates:
\begin{equation}
ds^2_{n-1} = -\left(1 - \frac{2Mr}{\Sigma}\right)dt^2 + \frac{4Mar \sin^2\theta}{\Sigma} dt\,d\phi + \frac{\Sigma}{\Delta} dr^2 + \Sigma d\theta^2 + \sin^2\theta\left(r^2 + a^2 + \frac{2Ma^2r \sin^2\theta}{\Sigma}\right)d\phi^2
\end{equation}
where $\Sigma = r^2 + a^2 \cos^2\theta$, $\Delta = r^2 - 2Mr + a^2$, $M$ represents progenitor black hole mass, and $a = J/M$ is angular momentum per unit mass.

Across the outer event horizon $r_+ = M + \sqrt{M^2 - a^2}$, the signature of the radial and temporal coordinates undergoes an inversion. The emergent child universe (recursion level $n$) is described by a Robertson-Walker interior metric:
\begin{equation}
ds^2_n = -dt^2 + a(t)^2 \left[\frac{dr^2}{1 - kr^2} + r^2(d\theta^2 + \sin^2\theta\, d\phi^2)\right]
\end{equation}
Boundary matching across the horizon boundary requires:
\begin{equation}
R_H(n-1) = c\, t_0(n)
\end{equation}
where $R_H$ is the horizon radius of the progenitor black hole and $t_0$ is the characteristic expansion scale (cosmic epoch) of the interior child universe.

\subsection{Modified Friedmann Expansion and Recursive Density}
The evolution of the cosmic scale factor $a(t)$ within recursion level $n$ obeys a modified Friedmann equation incorporating recursive horizon contributions:
\begin{equation}
\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3} \rho_{\text{eff}} - \frac{k}{a^2} + \frac{\Lambda_{\text{rec}}}{3}
\end{equation}
The effective energy density $\rho_{\text{eff}}$ integrates baryonic, radiation, and inherited recursive boundary pressure:
\begin{equation}
\rho_{\text{eff}} = \rho_{\text{matter}} + \rho_{\text{radiation}} + \rho_{\text{recursive}}
\end{equation}
where the recursive boundary coupling term is formalized by:
\begin{equation}
\rho_{\text{recursive}} = \left(\frac{\hbar c}{8\pi G}\right) \left(\frac{A_{\text{horizon}}}{V_{\text{universe}}}\right) f_{\text{rec}}(n)
\end{equation}
Here $A_{\text{horizon}}$ is the progenitor event horizon surface area, $V_{\text{universe}}$ is the interior comoving volume, and $f_{\text{rec}}(n)$ is a normalized recursion depth attenuation factor.

\subsection{Holographic Information Encoding and Projection Operators}
Following Bekenstein-Hawking entropy bounds \cite{hawking1975particle, thooft1993dimensional, susskind1995world}, the information capacity $I_n$ of the child universe is strictly upper-bounded by the horizon area of the parent system:
\begin{equation}
I_n \le \frac{A_{\text{horizon}}(n-1)}{4 \ell_p^2}, \quad \ell_p = \sqrt{\frac{\hbar G}{c^3}}
\end{equation}
Energy-information conservation across the boundary interface satisfies:
\begin{equation}
E_{\text{parent}} = \int_{\partial \mathcal{M}} T_{\mu\nu}^{\text{boundary}} dA^{\mu\nu} = M c^2 = I_{\text{child}} \cdot k_B T_{\text{Hawking}}
\end{equation}
where $T_{\text{Hawking}} = \frac{\hbar c^3}{8\pi G M k_B}$. Bulk quantum states $\Psi_{\text{bulk}}$ inside the child cosmos emerge from boundary configurations $\Psi_{\text{boundary}}$ through a holographic projection integral kernel $K$:
\begin{equation}
\Psi_{\text{bulk}}(r, \theta, \phi, t) = \iint_{\partial \mathcal{M}} K(r, \theta, \phi \mid \theta', \phi') \Psi_{\text{boundary}}(\theta', \phi', t) d\theta' d\phi'
\end{equation}

\subsection{Modified Einstein Field Equations with Boundary Stress-Energy}
The effective gravitational field equations within the interior child cosmos take the form:
\begin{equation}
G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} \left[ T_{\mu\nu}^{\text{matter}} + T_{\mu\nu}^{\text{recursive}} \right]
\end{equation}
The boundary-induced stress-energy tensor $T_{\mu\nu}^{\text{recursive}}$ arises from the boundary extrinsic curvature constraints:
\begin{equation}
T_{\mu\nu}^{\text{recursive}} = \frac{1}{8\pi G} \left[ R_{\text{parent}}(r_h) g_{\mu\nu} - \left.G_{\mu\nu}^{\text{parent}}\right|_{\partial\mathcal{M}} \right]
\end{equation}
At the cosmological boundary horizon $r = r_{\text{cosmic}}$, the boundary condition ensures metric continuity:
\begin{equation}
g_{\mu\nu}(r_{\text{cosmic}}) = \eta_{\mu\nu} + h_{\mu\nu}^{\text{boundary}}
\end{equation}
where $h_{\mu\nu}^{\text{boundary}}$ preserves the trace of progenitor rotational and informational multipoles.

\subsection{Multi-Level Quantum State Evolution and Decoherence}
Quantum states defined across the hierarchy evolve via a coupled recursive Hamiltonian:
\begin{equation}
i\hbar \frac{\partial \Psi_n}{\partial t} = \hat{H}_n \Psi_n + \hat{V}_{\text{rec}}(n \to n+1)\Psi_{n+1} + \hat{V}_{\text{rec}}(n \to n-1)\Psi_{n-1}
\end{equation}
The inter-universal entanglement entropy between levels $n$ and $n+1$ reproduces the area law:
\begin{equation}
S_{\text{ent}}(n, n+1) = -\text{Tr}[\rho_n \log \rho_n] = \frac{A_{\text{horizon}}(n)}{4G} + \mathcal{O}(\log A_{\text{horizon}})
\end{equation}
Coupling across the horizon produces an intrinsic fundamental decoherence timescale $\tau_{\text{dec}}$:
\begin{equation}
\tau_{\text{dec}} = \frac{\hbar}{k_B T_{\text{Hawking}}} = \frac{8\pi G M}{c^3}
\end{equation}
which corresponds precisely to the light-crossing timescale of the progenitor horizon boundary.

\subsection{Vacuum Energy Renormalization}
The observed cosmological constant is non-trivially suppressed relative to Planck-scale naive estimates through recursive horizon attenuation:
\begin{equation}
\Lambda_{\text{obs}}(n) = \Lambda_{\text{bare}} \prod_{i=0}^n \mathcal{F}_{\text{filter}}(M_i, a_i)
\end{equation}
where the horizon boundary filtering factor is given by:
\begin{equation}
\mathcal{F}_{\text{filter}}(M, a) = \exp\left(-\frac{\pi M^2 \ell_p^2}{\hbar c}\right) J_{\text{boundary}}\left(\frac{a}{M}\right)
\end{equation}
This naturally suppresses the high vacuum energy divergence through cascaded horizon boundary filtration.

\section{Predictions and Testable Implications}
""" + predictions_clean + r"""

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth]{figures/temporal_recursion.png}
    \caption{Temporal recursion dynamics: time manifests as the true expanding coordinate proceeding inward along the radial horizon gradient.}
    \label{fig:temporal_recursion}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth]{figures/cmb_lensing.png}
    \caption{Observable boundary signatures in CMB low-$\ell$ multipoles and anomalous gravitational lensing without particulate dark matter halos.}
    \label{fig:cmb_lensing}
\end{figure}

\section{Comparative Analysis with Standard Cosmology}
""" + comparison_clean + r"""

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{figures/comparison_chart.png}
    \caption{Structural and empirical comparison: RBHC vs $\Lambda$CDM paradigm across singularity handling, dark sector origin, and arrow of time.}
    \label{fig:comparison_chart}
\end{figure}

\section{Philosophical and Epistemological Implications}
""" + philosophy_clean + r"""

\section{Future Work and Experimental Pathways}
""" + futurework_clean + r"""

\section{Conclusion}
""" + conclusion_clean + r"""

\bibliographystyle{ieeetr}
\bibliography{references}

\end{document}
"""

with open(os.path.join(base_dir, "main.tex"), "w", encoding="utf-8") as f:
    f.write(main_tex)

print("Wrote main.tex for RBHC successfully!")

# Also generate paper.md for README/online browsing
md_content = f"""# Recursive Black Hole Cosmology: A Boundary-Driven Framework for Time, Space, and Information

**Author:** Larry Arnold  
**Affiliation:** Independent Researcher in Theoretical Physics, Information Theory, and Machine Learning — LA Builds  
**Date:** July 2025 (Revised: October 2026)  
**Target Venue:** arXiv preprint (`gr-qc` / `physics.gen-ph`) & Academic Journal Submission  

---

## Abstract

{abstract_txt}

**Keywords:** Black hole cosmology, Holographic principle, Quantum gravity, Information theory, Metric inversion, Dark energy, Emergent spacetime.

---

## 1. Introduction

{intro_clean}

---

## 2. Core Theoretical Framework

{framework_clean}

![Recursive Hierarchy](figures/recursion_diagram.png)
*Figure 1: Hierarchical architecture of nested universes: parent black hole collapse generates child spacetime interior manifolds recursively unfolding inward.*

![Boundary Encoding](figures/boundary_encoding.png)
*Figure 2: Holographic boundary encoding at the event horizon. Information is mapped via boundary degrees of freedom into bulk emergent spacetime.*

---

## 3. Mathematical Foundations of Recursive Metric and Information Dynamics

### 3.1 Parent-Child Metric Transformation
Consider a rotating Kerr black hole in a parent universe of recursion index $n-1$, parameterized in Boyer-Lindquist coordinates:

$$ds^2_{{n-1}} = -\\left(1 - \\frac{{2Mr}}{{\\Sigma}}\\right)dt^2 + \\frac{{4Mar \\sin^2\\theta}}{{\\Sigma}} dt\\,d\\phi + \\frac{{\\Sigma}}{{\\Delta}} dr^2 + \\Sigma d\\theta^2 + \\sin^2\\theta\\left(r^2 + a^2 + \\frac{{2Ma^2r \\sin^2\\theta}}{{\\Sigma}}\\right)d\\phi^2$$

where $\\Sigma = r^2 + a^2 \\cos^2\\theta$, $\\Delta = r^2 - 2Mr + a^2$, $M$ represents progenitor black hole mass, and $a = J/M$ is angular momentum per unit mass.

Across the outer event horizon $r_+ = M + \\sqrt{{M^2 - a^2}}$, the signature of the radial and temporal coordinates undergoes an inversion. The emergent child universe (recursion level $n$) is described by a Robertson-Walker interior metric:

$$ds^2_n = -dt^2 + a(t)^2 \\left[\\frac{{dr^2}}{{1 - kr^2}} + r^2(d\\theta^2 + \\sin^2\\theta\\, d\\phi^2)\\right]$$

Boundary matching across the horizon boundary requires:

$$R_H(n-1) = c\\, t_0(n)$$

where $R_H$ is the horizon radius of the progenitor black hole and $t_0$ is the characteristic expansion scale (cosmic epoch) of the interior child universe.

### 3.2 Modified Friedmann Expansion and Recursive Density
The evolution of the cosmic scale factor $a(t)$ within recursion level $n$ obeys a modified Friedmann equation incorporating recursive horizon contributions:

$$\\left(\\frac{{\\dot{{a}}}}{{a}}\\right)^2 = \\frac{{8\\pi G}}{{3}} \\rho_{{\\text{{eff}}}} - \\frac{{k}}{{a^2}} + \\frac{{\\Lambda_{{\\text{{rec}}}}}}{{3}}$$

The effective energy density $\\rho_{{\\text{{eff}}}}$ integrates baryonic, radiation, and inherited recursive boundary pressure:

$$\\rho_{{\\text{{eff}}}} = \\rho_{{\\text{{matter}}}} + \\rho_{{\\text{{radiation}}}} + \\rho_{{\\text{{recursive}}}}$$

where the recursive boundary coupling term is formalized by:

$$\\rho_{{\\text{{recursive}}}} = \\left(\\frac{{\\hbar c}}{{8\\pi G}}\\right) \\left(\\frac{{A_{{\\text{{horizon}}}}}}{{V_{{\\text{{universe}}}}}}\\right) f_{{\\text{{rec}}}}(n)$$

Here $A_{{\\text{{horizon}}}}$ is the progenitor event horizon surface area, $V_{{\\text{{universe}}}}$ is the interior comoving volume, and $f_{{\\text{{rec}}}}(n)$ is a normalized recursion depth attenuation factor.

### 3.3 Holographic Information Encoding and Projection Operators
Following Bekenstein-Hawking entropy bounds, the information capacity $I_n$ of the child universe is strictly upper-bounded by the horizon area of the parent system:

$$I_n \\le \\frac{{A_{{\\text{{horizon}}}}(n-1)}}{{4 \\ell_p^2}}, \\quad \\ell_p = \\sqrt{{\\frac{{\\hbar G}}{{c^3}}}}$$

Energy-information conservation across the boundary interface satisfies:

$$E_{{\\text{{parent}}}} = \\int_{{\\partial \\mathcal{{M}}}} T_{{\\mu\\nu}}^{{\\text{{boundary}}}} dA^{{\\mu\\nu}} = M c^2 = I_{{\\text{{child}}}} \\cdot k_B T_{{\\text{{Hawking}}}}$$

where $T_{{\\text{{Hawking}}}} = \\frac{{\\hbar c^3}}{{8\\pi G M k_B}}$. Bulk quantum states $\\Psi_{{\\text{{bulk}}}}$ inside the child cosmos emerge from boundary configurations $\\Psi_{{\\text{{boundary}}}}$ through a holographic projection integral kernel $K$:

$$\\Psi_{{\\text{{bulk}}}}(r, \\theta, \\phi, t) = \\iint_{{\\partial \\mathcal{{M}}}} K(r, \\theta, \\phi \\mid \\theta', \\phi') \\Psi_{{\\text{{boundary}}}}(\\theta', \\phi', t) d\\theta' d\\phi'$$

### 3.4 Modified Einstein Field Equations with Boundary Stress-Energy
The effective gravitational field equations within the interior child cosmos take the form:

$$G_{{\\mu\\nu}} + \\Lambda g_{{\\mu\\nu}} = \\frac{{8\\pi G}}{{c^4}} \\left[ T_{{\\mu\\nu}}^{{\\text{{matter}}}} + T_{{\\mu\\nu}}^{{\\text{{recursive}}}} \\right]$$

The boundary-induced stress-energy tensor $T_{{\\mu\\nu}}^{{\\text{{recursive}}}}$ arises from the boundary extrinsic curvature constraints:

$$T_{{\\mu\\nu}}^{{\\text{{recursive}}}} = \\frac{{1}}{{8\\pi G}} \\left[ R_{{\\text{{parent}}}}(r_h) g_{{\\mu\\nu}} - \\left.G_{{\\mu\\nu}}^{{\\text{{parent}}}}\\right|_{{\\partial\\mathcal{{M}}}} \\right]$$

### 3.5 Multi-Level Quantum State Evolution and Decoherence
Quantum states defined across the hierarchy evolve via a coupled recursive Hamiltonian:

$$i\\hbar \\frac{{\\partial \\Psi_n}}{{\\partial t}} = \\hat{{H}}_n \\Psi_n + \\hat{{V}}_{{\\text{{rec}}}}(n \\to n+1)\\Psi_{{n+1}} + \\hat{{V}}_{{\\text{{rec}}}}(n \\to n-1)\\Psi_{{n-1}}$$

Inter-universal entanglement entropy between levels $n$ and $n+1$ satisfies:

$$S_{{\\text{{ent}}}}(n, n+1) = -\\text{{Tr}}[\\rho_n \\log \\rho_n] = \\frac{{A_{{\\text{{horizon}}}}(n)}}{{4G}} + \\mathcal{{O}}(\\log A_{{\\text{{horizon}}}})$$

Coupling across the horizon produces an intrinsic fundamental decoherence timescale $\\tau_{{\\text{{dec}}}}$:

$$\\tau_{{\\text{{dec}}}} = \\frac{{\\hbar}}{{k_B T_{{\\text{{Hawking}}}}}} = \\frac{{8\\pi G M}}{{c^3}}$$

### 3.6 Vacuum Energy Renormalization
The observed cosmological constant is non-trivially suppressed relative to Planck-scale naive estimates through recursive horizon attenuation:

$$\\Lambda_{{\\text{{obs}}}}(n) = \\Lambda_{{\\text{{bare}}}} \\prod_{{i=0}}^n \\mathcal{{F}}_{{\\text{{filter}}}}(M_i, a_i)$$

where the horizon boundary filtering factor is given by:

$$\\mathcal{{F}}_{{\\text{{filter}}}}(M, a) = \\exp\\left(-\\frac{{\\pi M^2 \\ell_p^2}}{{\\hbar c}}\\right) J_{{\\text{{boundary}}}}\\left(\\frac{{a}}{{M}}\\right)$$

---

## 4. Predictions and Testable Implications

{predictions_clean}

![Temporal Recursion](figures/temporal_recursion.png)
*Figure 3: Temporal recursion dynamics: time manifests as the true expanding coordinate proceeding inward along the radial horizon gradient.*

![CMB and Lensing](figures/cmb_lensing.png)
*Figure 4: Observable boundary signatures in CMB low-l multipoles and anomalous gravitational lensing without particulate dark matter halos.*

---

## 5. Comparative Analysis with Standard Cosmology

{comparison_clean}

![Comparison Chart](figures/comparison_chart.png)
*Figure 5: Structural and empirical comparison: RBHC vs LCDM paradigm across singularity handling, dark sector origin, and arrow of time.*

---

## 6. Philosophical and Epistemological Implications

{philosophy_clean}

---

## 7. Future Work and Experimental Pathways

{futurework_clean}

---

## 8. Conclusion

{conclusion_clean}

---

## References

1. G. 't Hooft, "Dimensional Reduction in Quantum Gravity," *arXiv:gr-qc/9310026* (1993).
2. L. Susskind, "The World as a Hologram," *Journal of Mathematical Physics*, 36(11):6377–6396 (1995).
3. S. W. Hawking, "Particle Creation by Black Holes," *Communications in Mathematical Physics*, 43(3):199–220 (1975).
4. S. Wolfram, *A New Kind of Science*, Wolfram Media (2002).
5. A. Borde, A. H. Guth, and A. Vilenkin, "Inflationary Spacetimes are Incomplete in Past Directions," *Physical Review Letters*, 90(15):151301 (2003).
6. S. Carroll, *From Eternity to Here: The Quest for the Ultimate Theory of Time*, Dutton (2010).
7. E. Verlinde, "On the Origin of Gravity and the Laws of Newton," *Journal of High Energy Physics*, 2011(4):29 (2011).
8. W. G. Unruh, "Experimental Black-Hole Evaporation?" *Physical Review Letters*, 46(21):1351 (1981).
9. L. Smolin, "Did the Universe Evolve?" *Classical and Quantum Gravity*, 9(1):173 (1992).
10. R. Bousso, "The Holographic Principle," *Reviews of Modern Physics*, 74(3):825 (2002).
"""

with open(os.path.join(base_dir, "paper.md"), "w", encoding="utf-8") as f:
    f.write(md_content)

print("Wrote paper.md for RBHC successfully!")
