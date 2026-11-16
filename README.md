<div align="center">

# 📐 AI System Diagrams
### Drawing Production Architecture Diagrams with AI for Advanced Software Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Course](https://img.shields.io/badge/Course-Advanced%20Software%20Engineering-1e3a8a.svg?style=for-the-badge)](#)
[![Instructor](https://img.shields.io/badge/Instructor-Eng.%20Abdallah%20Amir-0284c7.svg?style=for-the-badge)](#)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)

<p align="center">
  A practical framework teaching software engineering students how to generate production-quality system diagrams using AI coding assistants across <strong>PlantUML</strong>, <strong>Mermaid.js</strong>, and <strong>diagram-design</strong>.
</p>

[🧭 Overview](#-overview) •
[🖥️ Web Showcase](#️-interactive-web-showcase) •
[⚖️ 3 Approaches](#️-the-3-diagramming-approaches) •
[🏥 Case Study](#-case-study-reference-diagrams) •
[📦 Add to Your Project](#-adding-to-any-existing-project) •
[💬 Agent Prompts](#-prompting-the-ai-agent-choose-your-approach) •
[📋 Prompt Rules](#-essential-ai-prompting-rules)

</div>

---

## 🧭 Overview

When developers ask AI coding tools (ChatGPT, Claude, Gemini, Cursor) to generate system diagrams, the results are frequently broken, misaligned, or poorly formatted. 

This repository solves that by providing **curated templates, zero-dependency rendering scripts, and copy-paste prompt playbooks** across three modern diagramming approaches:

1. **PlantUML**: Formal UML 2.5 standard using plain-text DSL.
2. **Mermaid.js**: Markdown-native syntax rendering directly inside GitHub and Notion.
3. **diagram-design**: Editorial HTML + inline SVG standard by [Cathryn Lavery](https://github.com/cathrynlavery/diagram-design).

All three approaches are demonstrated on a single reference domain: the **MedPulse Smart Hospital Management System**.

---

## 🖥️ Interactive Web Showcase

This repository includes a standalone web app ([`index.html`](index.html)) to compare diagrams side-by-side, inspect raw source code, and copy AI prompts:

```bash
# Launch local preview server
python scripts/serve.py
```
*Or simply open [`index.html`](index.html) directly in any browser.*

---

## ⚖️ The 3 Diagramming Approaches

| Approach | Format | Best For | Key Advantage |
|---|---|---|---|
| **PlantUML** | Plain-text `.puml` | Formal architecture docs & reports | Full UML 2.5 compliance, rich multiplicities |
| **Mermaid.js** | Markdown `.mmd` | GitHub PRs, issues, Notion wikis | Zero build steps, native GitHub rendering |
| **diagram-design** | HTML + inline SVG | Whitepapers, slide decks, blog posts | Publication-grade 1px hairlines, custom typography |

---

## 🏥 Case Study Reference Diagrams

All approaches model the **MedPulse Smart Hospital**:

| Diagram | Focus & Modeling | PlantUML | Mermaid.js | diagram-design |
|---|---|---|---|---|
| **Use Case Diagram** | Actors (Patient, Doctor, Nurse, Admin, Insurance), `<<include>>`, `<<extend>>` | [`use-case.puml`](1-plantuml/use-case.puml) | [`use-case.mmd`](2-mermaid/use-case.mmd) | [`use-case.html`](3-diagram-design/use-case.html) |
| **Class Diagram** | Abstract `User`, `Patient`, `Doctor`, inheritance, aggregation, composition | [`class-diagram.puml`](1-plantuml/class-diagram.puml) | [`class-diagram.mmd`](2-mermaid/class-diagram.mmd) | [`class-diagram.html`](3-diagram-design/class-diagram.html) |
| **Deployment Diagram** | Client edge, Cloudflare WAF, Kubernetes pods, PostgreSQL, Redis, external APIs | [`deployment-diagram.puml`](1-plantuml/deployment-diagram.puml) | [`deployment-diagram.mmd`](2-mermaid/deployment-diagram.mmd) | [`deployment-diagram.html`](3-diagram-design/deployment-diagram.html) |

---

## 📦 Adding to Any Existing Project

You can install this repository into **any existing project** (Python, Java, TypeScript, Go, C#, etc.) in an isolated `ai-system-diagrams` subfolder so that your files remain clean and your AI agent can reference the framework directly.

### 1. Add as a Subfolder
Inside your application's root directory, clone the repository or add it as a Git submodule:

```bash
# Option A: Clone into ai-system-diagrams/
git clone https://github.com/Zerobrofan/ai-system-diagrams.git ai-system-diagrams

# Option B: Add as a Git Submodule
git submodule add https://github.com/Zerobrofan/ai-system-diagrams.git ai-system-diagrams
```

### 2. Resulting Project Structure
```text
your-project/
├── src/                          # Your application source code
├── tests/                        # Your unit & integration tests
├── package.json / pom.xml / etc.
│
└── ai-system-diagrams/           # Cloned framework subfolder
    ├── prompts/                  # AI prompt playbooks & taxonomy specifications
    ├── scripts/                  # Automated Python SVG renderers
    ├── 1-plantuml/               # PlantUML diagrams (.puml) & compiled output/
    ├── 2-mermaid/                # Mermaid diagrams (.mmd) & compiled output/
    ├── 3-diagram-design/         # Editorial HTML/SVG diagrams (.html) & output/
    └── index.html                # Interactive comparison dashboard
```

---

## 💬 Prompting the AI Agent (Choose Your Approach)

When instructing your AI coding assistant (Antigravity, Cursor, Claude Code, GitHub Copilot), you can tell the agent to output the diagrams in **PlantUML**, **Mermaid.js**, or **diagram-design** depending on your project needs:

### 🔵 Option 1: PlantUML (Formal Architecture Docs & UML 2.5)
Use PlantUML when you need standard UML compliance for university reports, technical thesis papers, or formal design documents.

> **Agent Prompt Example:**
> ```text
> Analyze our database models and entity definitions in /src/.
> Using the UML Class Diagram guidelines in ai-system-diagrams/prompts/structure-diagrams.md:
> 1. Extract core domain entities, fields, data types, and method signatures.
> 2. Model inheritance, composition, and associations with proper multiplicities.
> 3. Generate a formal PlantUML diagram and save it to ai-system-diagrams/1-plantuml/class-diagram.puml.
> ```

### 🟢 Option 2: Mermaid.js (GitHub Markdown & Lightweight Documentation)
Use Mermaid when you want diagrams that render directly in GitHub `README.md` files, PR discussions, and Notion pages without compilation steps.

> **Agent Prompt Example:**
> ```text
> Inspect our Dockerfiles, docker-compose.yml, and cloud deployment manifests.
> Using the Deployment Diagram guidelines in ai-system-diagrams/prompts/structure-diagrams.md:
> 1. Model client gateways, reverse proxies, microservices, databases, and message queues.
> 2. Include port mappings and transport protocols (HTTPS, gRPC, TCP).
> 3. Generate a Mermaid.js flowchart diagram and save it to ai-system-diagrams/2-mermaid/deployment-diagram.mmd.
> ```

### 🟣 Option 3: diagram-design (High-Aesthetic Publication & Presentation)
Use diagram-design when preparing presentation slides, pitch decks, blog posts, or project landing pages requiring 1px hairlines, modern dark/light themes, and pill tags.

> **Agent Prompt Example:**
> ```text
> Trace the primary user authentication and transaction workflows in our application.
> Using the editorial design principles in ai-system-diagrams/prompts/behavior-diagrams.md:
> 1. Model the actors, system boundaries, and core use cases.
> 2. Use a modern dark theme (#0d1117), crisp 1px connectors, and colored pill badges.
> 3. Generate an editorial HTML + inline SVG diagram and save it to ai-system-diagrams/3-diagram-design/use-case.html.
> ```

---

## ⚙️ Automated Zero-Dependency SVG Rendering

After the agent writes or updates the diagram files in `ai-system-diagrams/`, compile them into crisp vector SVGs with one command:

```bash
# Render all diagrams across all 3 approaches
python ai-system-diagrams/scripts/render_all.py
```

You can also compile individual formats:
```bash
python ai-system-diagrams/1-plantuml/render.py
python ai-system-diagrams/2-mermaid/render.py
python ai-system-diagrams/3-diagram-design/render.py
```
*(Requires zero local Java, Graphviz, or headless browser installations!)*

---

## 📋 Essential AI Prompting Rules

To prevent AI from generating broken or messy diagrams, include these rules in your prompts:

1. **Mermaid Generics**: In Mermaid `classDiagram`, always instruct the AI to use tildes for generic types (`List~Item~`) instead of angle brackets (`List<Item>`), which crash the parser.
2. **PlantUML Styling**: Tell the AI to include `skinparam shadowing false` and a clean slate palette to avoid outdated yellow-box defaults.
3. **SVG Connectors**: Tell the AI to draw connectors behind node boxes and place text labels on opaque background masks.

Complete prompt templates are available in the [`prompts/`](prompts/) directory.

---

## 📁 Directory Structure

```text
ai-system-diagrams/
├── README.md                          # Project documentation
├── index.html                         # Interactive browser comparison dashboard
├── LICENSE                            # MIT License
├── package.json                       # npm convenience scripts
│
├── 1-plantuml/                        # Approach 1: PlantUML
│   ├── use-case.puml
│   ├── class-diagram.puml
│   ├── deployment-diagram.puml
│   ├── render.py                      # Zero-dependency PlantUML to SVG compiler
│   └── output/                        # Compiled SVGs
│
├── 2-mermaid/                         # Approach 2: Mermaid.js
│   ├── use-case.mmd
│   ├── class-diagram.mmd
│   ├── deployment-diagram.mmd
│   ├── render.py                      # Zero-dependency Mermaid to SVG compiler
│   └── output/                        # Compiled SVGs
│
├── 3-diagram-design/                  # Approach 3: diagram-design
│   ├── use-case.html
│   ├── class-diagram.html
│   ├── deployment-diagram.html
│   ├── render.py                      # SVG extraction script
│   └── output/                        # Compiled SVGs
│
├── prompts/                           # Copy-paste AI prompt templates
│   ├── structure-diagrams.md
│   ├── behavior-diagrams.md
│   ├── interaction-diagrams.md
│   └── agent-codebase-workflow.md
│
└── scripts/
    ├── render_all.py                  # One-command build script
    └── serve.py                       # Local HTTP preview server
```

---

## 👨‍🏫 Author & Course Attribution

- **Curriculum & Architectural Design**: **Eng. Abdallah Amir**
- **Course**: Advanced Software Engineering
- **License**: [MIT License](LICENSE)
