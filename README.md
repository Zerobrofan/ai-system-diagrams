<div align="center">

# 📐 AI System Diagrams Laboratory
### Drawing Production-Grade Architecture Diagrams with AI for Advanced Software Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Course](https://img.shields.io/badge/Course-Advanced%20Software%20Engineering-1e3a8a.svg?style=for-the-badge)](#)
[![Instructor](https://img.shields.io/badge/Curriculum-Eng.%20Abdallah%20Amir-0284c7.svg?style=for-the-badge)](#)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![UML 2.5](https://img.shields.io/badge/Standard-UML%202.5-f97316.svg?style=for-the-badge)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-10b981.svg?style=for-the-badge)](CONTRIBUTING.md)

<p align="center">
  A pedagogical open-source laboratory and practical framework teaching computer science and software engineering students how to leverage Artificial Intelligence (LLMs) to design, specify, and render publication-quality system architecture diagrams.
</p>

[🌐 Live Showcase Portal](#-interactive-web-showcase) •
[⚖️ 3-Way Comparative Overview](#-the-3-diagramming-approaches) •
[🩺 Case Study Diagrams](#-the-3-case-study-diagrams) •
[🚀 Student Quickstart](#-how-to-use-this-in-your-own-project) •
[🤖 AI Prompt Playbook](#-ai-prompting-playbook)

</div>

---

## 📖 Overview

In modern software engineering, communicating system architecture is as vital as writing clean code. However, when software engineering students ask AI assistants (*ChatGPT, Claude, Gemini, Copilot*) to draw system diagrams, the results are frequently **generic, tangled, or visually broken** ("AI slop") — featuring hallucinated syntax, missing multiplicity constraints, overlapping lines, or obsolete 1990s styling.

This repository provides **battle-tested templates, zero-dependency rendering scripts, and copy-paste prompt playbooks** across **three major diagramming paradigms**:

1. 🌿 **PlantUML**: The formal enterprise standard for strict OMG UML 2.5 compliance.
2. 🧜 **Mermaid.js**: The markdown-native standard rendering natively in GitHub, Notion, and Obsidian.
3. 🖋️ **diagram-design**: The editorial, publication-grade HTML + SVG framework created by [Cathryn Lavery](https://github.com/cathrynlavery/diagram-design) to eliminate "Mermaid slop".

All three paradigms are benchmarked against a single, cohesive enterprise domain: the **MedPulse Smart Hospital Management System**.

---

## 🌐 Interactive Web Showcase

This repository includes a standalone, zero-setup interactive web application ([`index.html`](index.html)). Students can open it in any browser to:
- Compare all 3 approaches **side-by-side** for any diagram.
- Toggle between live **vector SVG previews** and raw **source code**.
- Copy battle-tested **AI prompt templates** with a single click.
- Explore the **architectural decision matrix**.

```bash
# Launch the interactive showcase locally
python scripts/serve.py
```
*Or simply double-click [`index.html`](index.html) in your file explorer!*

---

## ⚖️ The 3 Diagramming Approaches

| Feature / Dimension | 🌿 PlantUML | 🧜 Mermaid.js | 🖋️ diagram-design |
|---|---|---|---|
| **Primary Philosophy** | Strict UML 2.5 formal specification via DSL | Markdown-native, zero-build simplicity | Editorial, publication-grade typography & precision |
| **Engine / Renderer** | Deflate-base64 HTTP service (zero Java needed) | Client-side JS / `mermaid.ink` API | Standalone HTML + inline SVG |
| **GitHub Native Preview** | Requires pre-rendered SVG/PNG | **Yes** (renders directly in Markdown fences) | Opens in any browser; embeds SVG into Markdown |
| **Visual Aesthetics** | Modern slate & blue (via custom `skinparam`) | Clean modern vector flowchart / class blocks | Hairline 1px borders, Geist/Instrument Serif typography |
| **UML Semantic Depth** | **100%**: Native interfaces, stereotypes, multiplicity | **Partial**: Great for classes; flowcharts for use cases | **100%**: Pixel-level markers, masks, and compartments |
| **Git Diff Friendliness** | **High**: 20–45 lines of plain text DSL | **High**: 20–50 lines of plain text DSL | **Moderate**: 120–260 lines of structured HTML/SVG |
| **Best Used For** | Formal architectural specifications & lab reports | GitHub PRs, Agile documentation, Notion wikis | Whitepapers, conference slides, and tech blogs |

---

## 🩺 The 3 Case Study Diagrams

All approaches are showcased using the **MedPulse Smart Hospital Management System**:

### 1. 🩺 Use Case Diagram
- **Domain Focus**: Human actors (*Patient, Doctor, Nurse, Hospital Admin*) and secondary systems (*Insurance Clearinghouse*).
- **Core Semantics**: System boundary encapsulation, mandatory `<<include>>` preconditions (*Verify Identity / 2FA*, *Cross-Check Drug Allergies*), and conditional `<<extend>>` branches (*Telehealth Video Session*, *Insurance Claim Submission*).
- **Diagram Files**:
  - 🌿 **PlantUML**: [`1-plantuml/use-case.puml`](1-plantuml/use-case.puml) → [Rendered SVG](1-plantuml/output/use-case.svg)
  - 🧜 **Mermaid.js**: [`2-mermaid/use-case.mmd`](2-mermaid/use-case.mmd) → [Rendered SVG](2-mermaid/output/use-case.svg)
  - 🖋️ **diagram-design**: [`3-diagram-design/use-case.html`](3-diagram-design/use-case.html) → [Rendered SVG](3-diagram-design/output/use-case.svg)

### 2. 🏛️ Domain Class Diagram
- **Domain Focus**: Object-oriented domain modeling with clean architectural separation.
- **Core Semantics**: 
  - Abstract base class: `User` (`#id`, `#fullName`, `+authenticate()`).
  - Inheritance: `Patient`, `Staff`, `Doctor`, `Nurse`.
  - Aggregation: `Department` (`1`) o-- (`1..*`) `Doctor`.
  - Association with Multiplicities: `Patient` (`1`) -- (`0..*`) `Appointment` (`0..1`) --> (`1`) `MedicalRecord`.
  - Composition: `MedicalRecord` (`1`) *-- (`0..*`) `Prescription` (`1`) *-- (`1..*`) `PrescriptionItem`.
- **Diagram Files**:
  - 🌿 **PlantUML**: [`1-plantuml/class-diagram.puml`](1-plantuml/class-diagram.puml) → [Rendered SVG](1-plantuml/output/class-diagram.svg)
  - 🧜 **Mermaid.js**: [`2-mermaid/class-diagram.mmd`](2-mermaid/class-diagram.mmd) → [Rendered SVG](2-mermaid/output/class-diagram.svg)
  - 🖋️ **diagram-design**: [`3-diagram-design/class-diagram.html`](3-diagram-design/class-diagram.html) → [Rendered SVG](3-diagram-design/output/class-diagram.svg)

### 3. ☁️ Physical Deployment Diagram
- **Domain Focus**: Enterprise multi-tier cloud and hardware infrastructure.
- **Core Semantics**:
  - **Tier 1 (Client Edge)**: Flutter Mobile App, React 19 EHR Web Portal, Bedside IoT Daemon.
  - **Tier 2 (Edge & DMZ)**: Cloudflare WAF, DDoS Shield, Anycast SSL Offload.
  - **Tier 3 (Compute Cluster)**: Kubernetes cluster with Traefik Ingress, Spring Cloud API Gateway, Java EHR Pods, Go Scheduling Pods, and Python FastAPI Claims Workers.
  - **Tier 4 (Data & Storage)**: PostgreSQL 16 (Primary & Streaming WAL Standby Replica), Redis 7 Cache, MinIO/S3 Encrypted Scan Store.
  - **Tier 5 (External SaaS)**: Insurance FHIR v4 API, Stripe PCI-DSS Gateway, Twilio Alerts.
- **Diagram Files**:
  - 🌿 **PlantUML**: [`1-plantuml/deployment-diagram.puml`](1-plantuml/deployment-diagram.puml) → [Rendered SVG](1-plantuml/output/deployment-diagram.svg)
  - 🧜 **Mermaid.js**: [`2-mermaid/deployment-diagram.mmd`](2-mermaid/deployment-diagram.mmd) → [Rendered SVG](2-mermaid/output/deployment-diagram.svg)
  - 🖋️ **diagram-design**: [`3-diagram-design/deployment-diagram.html`](3-diagram-design/deployment-diagram.html) → [Rendered SVG](3-diagram-design/output/deployment-diagram.svg)

---

## 🚀 How to Use This in Your Own Project

Students can apply this framework to their semester projects (*E-Commerce, Banking, Social Network, IoT Platform*) in 4 simple steps:

```
┌──────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐      ┌────────────────────────┐
│  1. Pick System  │ ---> │  2. Copy Prompt Template│ ---> │  3. Feed to AI (LLM)    │ ---> │  4. 1-Click SVG Render │
│     & Domain     │      │     from /prompts/      │      │  (Claude, Gemini, GPT)  │      │     via Python CLI     │
└──────────────────┘      └─────────────────────────┘      └─────────────────────────┘      └────────────────────────┘
```

### Step 1: Clone the Repository
```bash
git clone https://github.com/AbdallahAmir/ai-system-diagrams.git
cd ai-system-diagrams
```

### Step 2: Choose Your Diagram & Copy the Prompt Template
Open the [`prompts/`](prompts/) directory and copy the template matching your required diagram:
- Use Case Prompts: [`prompts/01-use-case-prompts.md`](prompts/01-use-case-prompts.md)
- Class Diagram Prompts: [`prompts/02-class-diagram-prompts.md`](prompts/02-class-diagram-prompts.md)
- Deployment Diagram Prompts: [`prompts/03-deployment-diagram-prompts.md`](prompts/03-deployment-diagram-prompts.md)
- System Persona Rules: [`prompts/system-prompts-guide.md`](prompts/system-prompts-guide.md)

### Step 3: Paste into Your AI Coding Assistant
Replace `[System Name]` and your domain details in the prompt and ask the AI model to generate the source code.

### Step 4: Render to High-Resolution SVG
Save your generated code into the corresponding folder and execute:
```bash
# Render all diagrams in one command
python scripts/render_all.py

# Or render an individual approach:
python 1-plantuml/render.py
python 2-mermaid/render.py
python 3-diagram-design/render.py
```
> **Note**: All rendering scripts in this repository are **zero-dependency** — you do **NOT** need Java, Graphviz, or headless Chrome installed locally!

---

## 🤖 AI Prompting Playbook: Essential Rules

To ensure LLMs produce flawless diagram code without syntax errors or hallucinated layouts, enforce these rules:

### 1. The Mermaid Generic Type Rule
> ⚠️ **Problem**: When asked for a Class diagram, AI models default to Java/C# generics (`List<Patient>`), which causes the Mermaid parser to crash.  
> 💡 **Prompt Directive**: *"In Mermaid `classDiagram`, always use tildes for generic types (e.g., `List~Patient~`), NEVER angle brackets."*

### 2. The PlantUML Modern Skin Rule
> ⚠️ **Problem**: Default PlantUML renders dated 1990s yellow gradients with blurry drop shadows.  
> 💡 **Prompt Directive**: *"Apply modern skinparams: `skinparam shadowing false`, `skinparam roundcorner 6`, and a clean navy/slate palette. Never output unstyled yellow boxes."*

### 3. The diagram-design Mask Rule
> ⚠️ **Problem**: AI-generated SVG connectors frequently slice right through text labels.  
> 💡 **Prompt Directive**: *"Draw connector paths behind node cards. Place all connector labels on opaque background mask rectangles, and use orthogonal rounded elbows (`rx=8`)."*

---

## 📁 Repository Directory Structure

```text
ai-system-diagrams/
├── README.md                          # Master course laboratory guide
├── LICENSE                            # MIT Open-Source License (Eng. Abdallah Amir)
├── CONTRIBUTING.md                    # Guidelines for contributing new domains
├── SECURITY.md                        # Security & secret sanitization guide
├── package.json                       # Quick-run npm scripts
├── index.html                         # Interactive multi-view comparison dashboard
│
├── 1-plantuml/                        # Approach 1: PlantUML (Generated with AI)
│   ├── README.md                      # Detailed syntax guide & skinparam configurations
│   ├── use-case.puml                  # MedPulse Use Case diagram
│   ├── class-diagram.puml             # MedPulse Domain Class diagram
│   ├── deployment-diagram.puml        # MedPulse Multi-Tier Deployment diagram
│   ├── render.py                      # Zero-dependency PlantUML HTTP SVG renderer
│   └── output/                        # Rendered vector SVGs
│
├── 2-mermaid/                         # Approach 2: Mermaid.js (Generated with AI)
│   ├── README.md                      # Detailed guide & markdown integration tips
│   ├── use-case.mmd                   # MedPulse Use Case (Flowchart LR convention)
│   ├── class-diagram.mmd              # MedPulse Domain Class (native classDiagram)
│   ├── deployment-diagram.mmd         # MedPulse Infrastructure topology (Flowchart TB)
│   ├── preview.html                   # Client-side Mermaid live browser viewer
│   ├── render.py                      # Zero-dependency Mermaid SVG renderer
│   └── output/                        # Rendered vector SVGs
│
├── 3-diagram-design/                  # Approach 3: cathrynlavery/diagram-design
│   ├── README.md                      # Editorial standards, palette & anti-slop rules
│   ├── use-case.html                  # Editorial Use Case diagram (HTML + SVG)
│   ├── class-diagram.html             # Editorial UML Class diagram (HTML + SVG)
│   ├── deployment-diagram.html        # Editorial Deployment diagram (HTML + SVG)
│   ├── render.py                      # SVG extraction script
│   └── output/                        # Extracted standalone vector SVGs
│
├── prompts/                           # Copy-paste prompt templates for students
│   ├── 01-use-case-prompts.md         # Prompts for Use Case diagrams
│   ├── 02-class-diagram-prompts.md    # Prompts for Class diagrams
│   ├── 03-deployment-diagram-prompts.md # Prompts for Deployment diagrams
│   └── system-prompts-guide.md        # Master AI Persona prompt & anti-hallucination rules
│
├── scripts/                           # Central automated tooling
│   ├── render_all.py                  # One-command build script for all 9 diagrams
│   └── serve.py                       # Lightweight local HTTP preview server
│
└── diagram-design-framework/          # Cloned reference assets & spec from GitHub
```

---

## 👨‍🏫 Curriculum & Author Attribution

- **Curriculum Presentation & Architectural Design**: **Eng. Abdallah Amir**
- **Course**: Advanced Software Engineering & System Architecture
- **Framework Inspiration**: Built upon formal OMG UML 2.5 standards, Mermaid.js community standards, and [Cathryn Lavery's diagram-design](https://github.com/cathrynlavery/diagram-design) editorial standard.

---

## 📄 License

This project is open-source software licensed under the **[MIT License](LICENSE)**. Students and instructors are welcome to use, modify, and integrate these diagrams and prompt templates in their academic and commercial software projects.
