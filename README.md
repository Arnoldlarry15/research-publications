# Unified Research Manuscripts & Systems Specifications

[![License: CC-BY 4.0 & MIT](https://img.shields.io/badge/License-CC--BY%204.0%20%7C%20MIT-blue.svg)](LICENSE)
[![Author: Larry Arnold](https://img.shields.io/badge/Author-Larry%20Arnold-emerald.svg)](https://github.com/Arnoldlarry15)
[![arXiv: Submission Ready](https://img.shields.io/badge/Preprints-arXiv%20Ready-crimson.svg)](https://arxiv.org)
[![Ecosystem: LA Builds](https://img.shields.io/badge/Ecosystem-LA%20Builds-amber.svg)](https://www.labuilds.xyz)

This repository contains the publication-ready academic manuscripts, mathematical foundations, and enterprise systems specifications authored by **Larry Arnold** ([LA Builds](https://www.labuilds.xyz)). 

The works bridge foundational theoretical physics, mathematics, AI safety evaluation, and cognitive systems architecture. Each project includes complete standalone LaTeX sources (`main.tex`), formatted markdown documents (`paper.md` / `spec.md`), figures, and standard BibTeX bibliographies (`references.bib`).

---

## 📚 Master Research Directory

| # | Research Manuscript / Technical Specification | Primary Domain | Target Submission Venue | Manuscript & Source |
| :-: | :--- | :--- | :--- | :-: |
| **01** | **Recursive Black Hole Cosmology (RBHC): A Boundary-Driven Framework for Time, Space, and Information** | Theoretical Physics & Cosmology | **arXiv preprint** (`gr-qc` / `physics.gen-ph`), *General Relativity & Quantum Cosmology* | [Manuscript](01-rbhc-cosmology/paper.md) · [LaTeX](01-rbhc-cosmology/main.tex) |
| **02** | **Revealing Evaluation Blind Spots in Frontier Models via Adaptive Adversarial Systems** | AI Safety & Adversarial Red-Teaming | **NeurIPS / ICLR Workshop**, **IEEE S&P**, arXiv (`cs.CR` / `cs.AI`) | [Manuscript](02-frontier-model-blind-spots/paper.md) · [LaTeX](02-frontier-model-blind-spots/main.tex) |
| **03** | **AI Control Plane: A First-Principles Architectural Specification for Enterprise AI Governance** | Systems Architecture & AI Governance | **Enterprise Systems Whitepaper**, **IEEE Cloud / Software** (`cs.DC` / `cs.SE`) | [Specification](03-ai-control-plane/spec.md) · [LaTeX](03-ai-control-plane/main.tex) |
| **04** | **SourceOS: A Cognitive Pipeline and Attention Allocation Engine for Human Executive Function Augmentation** | Cognitive HCI & Systems Architecture | **Systems Whitepaper**, **ACM SIGCHI / Human-AI Interaction** (`cs.HC` / `cs.AI`) | [Specification](04-sourceos-system-planning/spec.md) · [LaTeX](04-sourceos-system-planning/main.tex) |
| **05** | **Cognitive Entropy: Measurement Framework Version 0.1 (MF-0.1)** | Measurement Theory & HCI | **ACM SIGCHI**, **IEEE Transactions on Human-Machine Systems** (`cs.HC` / `cs.CY`) | [Manuscript](05-cognitive-entropy-framework/paper.md) · [LaTeX](05-cognitive-entropy-framework/main.tex) |
| **06** | **Entropy as Ontological Substrate: The Informational Origin of Spacetime, Gravity, and the Arrow of Time** | Foundational Physics & Information Theory | **Foundations of Physics**, **Entropy**, arXiv (`physics.gen-ph` / `quant-ph`) | [Manuscript](06-entropy-ontological-substrate/paper.md) · [LaTeX](06-entropy-ontological-substrate/main.tex) |
| **07** | **Prime Numbers as Emergent Attractors: Recursive Information Compression, Quantum Chaos, and the Riemann Hypothesis** | Mathematical Physics & Number Theory | **Journal of Number Theory**, arXiv (`math.NT` / `math-ph`) | [Manuscript](07-riemann-hypothesis-primes-attractor/paper.md) · [LaTeX](07-riemann-hypothesis-primes-attractor/main.tex) |

---

## 🔬 Project Overviews

### 01. Recursive Black Hole Cosmology (RBHC)
* **Core Contribution:** Reframes black hole event horizons not as gateways concealing infinite singularities, but as generative boundary surfaces from which interior universes unfold recursively inward. Replaces spatial expansion with temporal recursion ($r \leftrightarrow t$ coordinate inversion), derives a modified Friedmann expansion equation with boundary density $\rho_{\text{recursive}}$, and proposes a natural solution to the 120-order-of-magnitude vacuum catastrophe through cascaded horizon attenuation.
* **Key Prediction:** Specific CMB angular power spectrum deviations at low multipoles ($\ell < 5$) and apparent gravitational lensing without localized particulate cold dark matter halos.
* **Assets:** Complete LaTeX manuscript, 20 pages of mathematical derivations, 5 embedded diagrams (`recursion_diagram.png`, `boundary_encoding.png`, `temporal_recursion.png`, `cmb_lensing.png`, `comparison_chart.png`), and BibTeX bibliography.

### 02. Revealing Evaluation Blind Spots in Frontier Models
* **Core Contribution:** Demonstrates that static AI safety benchmarks suffer from fundamental structural blind spots (evaluation gaming, deployment divergence, and safety boundary erosion). Presents an adaptive, co-evolving adversarial testing framework.
* **Empirical Validation:** Demonstrated against GPT-4, revealing policy violations and capability escalations at **3–7× the rate** of static benchmarking suites.
* **Assets:** Complete 9-page conference/journal LaTeX manuscript, empirical evaluation tables, dynamic safety metrics (Escalation Rate, Boundary Erosion Index), and BibTeX citations.

### 03. AI Control Plane Architectural Specification
* **Core Contribution:** Resolves enterprise AI vulnerability by strictly decoupling the AI **compute plane** (LLM inference, weights, hosted APIs) from the AI **control plane** (identity registry, declarative machine-enforced policies, choke-point gateway, audit logging, and hardware kill switches).
* **Compliance Alignment:** Formally aligned with NIST AI RMF 1.0, OWASP LLM Top 10, and EU AI Act (Articles 12 & 14). Includes reference Python SDK implementation pattern.
* **Assets:** Formal systems architecture paper in LaTeX, complete architectural specification in Markdown with Mermaid data-flow diagrams.

### 04. SourceOS: Cognitive Pipeline & Attention Allocation Engine
* **Core Contribution:** An externalized digital prefrontal cortex architecture designed to relieve cognitive overload. Ingests raw multimodal stream-of-consciousness data and applies machine reasoning across five pipeline stages to deconstruct inputs into six core primitive classes (Thought, Task, Idea, Goal, Commitment, Person).
* **Key Innovation:** Introduces a dynamic attention priority functional $\mathcal{P}(O, t)$ with temporal memory decay and an **Unresolved Mental Load metric** $\mathcal{L}_{\text{mental}}$ that quantifies latent psychological overhead.
* **Assets:** Systems architecture whitepaper in LaTeX and Markdown with graph lifecycle diagrams and schema tables.

### 05. Cognitive Entropy: Measurement Framework (MF-0.1)
* **Core Contribution:** Establishes the first formal, reproducible, and falsifiable engineering construct for digital workflow friction ($E_c$). Separates systemic coordination overhead (tool switches, logins, context switching) from intrinsic task difficulty and user expertise.
* **Measurement Standard:** Defines an intent-task ontology, three-tiered baselines (Theoretical $B_t$, Reference $B_{\text{ref}}$, Personal $B_u$), eight candidate variables, and explicit falsification criteria under Construct Validity ($\mathcal{H}_0: \text{Corr}(E_c, \text{Task Difficulty}) \ge 0.70$).
* **Assets:** Academic measurement specification in LaTeX and Markdown with complete variable definitions and pilot experimental protocols.

### 06. Entropy as Ontological Substrate
* **Core Contribution:** Inverts the classical ontological hierarchy of physics: entropy is posited not as an epistemic or statistical byproduct of matter, but as the fundamental ontological substrate from which spacetime geometry, inertia, and quantum field configurations emerge.
* **Derivations:** Connects Landauer's principle, Jacobson's thermodynamic field equations, and Verlinde's entropic gravity to derive Newton's gravitational constant and resolve the cosmological constant catastrophe through holographic horizon information saturation.
* **Assets:** Formal theoretical physics preprint in LaTeX and Markdown with mathematical proofs and foundational citations.

### 07. Prime Numbers as Emergent Attractors
* **Core Contribution:** Inquires whether prime numbers are Platonic axioms or universal attractor states of recursive holographic information compression at the boundary of quantum chaos.
* **Formal Model:** Connects the Montgomery-Dyson Gaussian Unitary Ensemble (GUE) correspondence with a multi-objective compression operator $\mathcal{C}: \mathcal{H}_n \to \mathcal{H}_{n+1}$ and an $\alpha$-sweep Hamiltonian interpolating between integrable Many-Body Localization and maximal SYK chaos.
* **Falsification Suite:** Defines three tests (spectral pair-correlation rigidity, autonomous prime counting $\pi^*(x) \sim x / \ln x$, and universality invariance).
* **Assets:** Working paper in LaTeX and Markdown with mathematical loss functions and epistemological implications for Wigner's puzzle.

---

## 🛠️ LaTeX Compilation & Submission Guide

Each directory is completely self-contained. To compile any manuscript to PDF locally:

```bash
# Example: Compiling Recursive Black Hole Cosmology (RBHC)
cd 01-rbhc-cosmology
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or using `latexmk`:
```bash
latexmk -pdf main.tex
```

### Direct Overleaf Import
1. Download or clone this repository.
2. Zip the contents of any project directory (e.g., zip all files in `01-rbhc-cosmology/`, including the `figures/` folder).
3. On [Overleaf](https://www.overleaf.com), select **New Project $\to$ Upload Project** and upload the zip file.
4. Set compiler to **pdfLaTeX** and compile.

### arXiv Preprint Submission
For submissions to [arXiv.org](https://arxiv.org):
1. In the target folder, verify `main.tex` and `references.bib` (or run `pdflatex` + `bibtex` to generate the `.bbl` file).
2. Package `main.tex`, `references.bib` (or `main.bbl`), and any associated `figures/` into a single `.tar.gz` or `.zip` archive.
3. Upload directly to the relevant primary arXiv subject class (listed in the master table above).

---

## 📜 Licensing

This repository uses a dual open-science license:
* **Academic Papers, Manuscripts, and Narrative Specifications:** Licensed under [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the work with attribution.
* **Code, Schemas, and Software Specifications:** Licensed under the [MIT License](LICENSE).

---

## 👤 Author & Contact

**Larry Arnold**  
Founder & Lead Researcher, [LA Builds](https://www.labuilds.xyz)  
- GitHub: [@Arnoldlarry15](https://github.com/Arnoldlarry15)  
- Portfolio & Software Catalog: [labuilds.xyz](https://www.labuilds.xyz)  
- Gumroad Storefront: [larryarnold.gumroad.com](https://larryarnold.gumroad.com)
