<div align="center">

# AI System Diagrams Laboratory
### Drawing Architecture Diagrams with AI for Advanced Software Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Course](https://img.shields.io/badge/Course-Advanced%20Software%20Engineering-1e3a8a.svg?style=for-the-badge)](#)
[![Curriculum](https://img.shields.io/badge/Curriculum-Eng.%20Abdallah%20Amir-0284c7.svg?style=for-the-badge)](#)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)

<p align="center">
  A practical framework teaching software engineering students how to generate production-quality system diagrams using AI coding assistants across <strong>PlantUML</strong>, <strong>Mermaid.js</strong>, and <strong>diagram-design</strong>.
</p>

[Live Showcase](#interactive-web-showcase) •
[The 3 Approaches](#the-3-approaches) •
[Showcase Diagrams](#case-study-diagrams) •
[Using in Any Project](#using-this-in-any-project) •
[AI Prompt Rules](#essential-ai-prompting-rules)

</div>

---

## Overview

When developers ask AI tools (ChatGPT, Claude, Gemini, Cursor) to generate system diagrams, the output is often messy or invalid. 

This repository provides **templates, zero-dependency rendering scripts, and copy-paste prompt playbooks** across three modern diagramming approaches:

1. **PlantUML**: Formal UML 2.5 standard using plain-text DSL.
2. **Mermaid.js**: Markdown-native syntax that renders directly on GitHub and Notion.
3. **diagram-design**: Editorial HTML + inline SVG standard by [Cathryn Lavery](https://github.com/cathrynlavery/diagram-design).

All three approaches are demonstrated on a single reference domain: the **MedPulse Smart Hospital Management System**.

---

## Interactive Web Showcase

This repository includes a standalone web app ([`index.html`](index.html)) to compare diagrams side-by-side, inspect raw source code, and copy AI prompts:

```bash
# Launch local server
python scripts/serve.py
```
*Or simply open [`index.html`](index.html) directly in any browser.*

---

## The 3 Approaches

| Approach | Format | Best For | Key Advantage |
|---|---|---|---|
| **PlantUML** | Plain-text `.puml` | Formal architecture docs & reports | Full UML 2.5 compliance, rich multiplicities |
| **Mermaid.js** | Markdown `.mmd` | GitHub PRs, issues, Notion wikis | Zero build steps, native GitHub rendering |
| **diagram-design** | HTML + inline SVG | Whitepapers, slide decks, blog posts | Publication-grade 1px hairlines, custom typography |

---

## Case Study Diagrams

All approaches model the **MedPulse Smart Hospital**:

| Diagram | Focus & Modeling | PlantUML | Mermaid.js | diagram-design |
|---|---|---|---|---|
| **Use Case Diagram** | Actors (Patient, Doctor, Nurse, Admin, Insurance), `<<include>>`, `<<extend>>` | [`use-case.puml`](1-plantuml/use-case.puml) | [`use-case.mmd`](2-mermaid/use-case.mmd) | [`use-case.html`](3-diagram-design/use-case.html) |
| **Class Diagram** | Abstract `User`, `Patient`, `Doctor`, inheritance, aggregation, composition | [`class-diagram.puml`](1-plantuml/class-diagram.puml) | [`class-diagram.mmd`](2-mermaid/class-diagram.mmd) | [`class-diagram.html`](3-diagram-design/class-diagram.html) |
| **Deployment Diagram** | Client edge, Cloudflare WAF, Kubernetes pods, PostgreSQL, Redis, external APIs | [`deployment-diagram.puml`](1-plantuml/deployment-diagram.puml) | [`deployment-diagram.mmd`](2-mermaid/deployment-diagram.mmd) | [`deployment-diagram.html`](3-diagram-design/deployment-diagram.html) |

---

## Using this in Any Project

You can install this repository into **any application directory** (e.g., your semester project or company codebase) and have your AI coding agent generate diagrams from your actual code:

### 1. Add to Your Application
Clone or copy this folder into your project (e.g., inside `docs/architecture/`):
```bash
git submodule add https://github.com/AbdallahAmir/ai-system-diagrams.git docs/architecture
```

### 2. Ask the AI Agent to Generate Diagrams
Open your AI coding assistant (Antigravity, Cursor, Claude Code, Copilot) in your project and prompt it:

- **For Class Diagrams**:
  > *"Inspect the models and database schemas in `/src/models` and generate a PlantUML Class Diagram based on our system architecture using the rules in `docs/architecture/prompts/`."*
- **For Deployment Diagrams**:
  > *"Inspect our `Dockerfile`, `docker-compose.yml`, and cloud configs, and create a Deployment Diagram matching our actual infrastructure."*
- **For Use Case / Sequence Diagrams**:
  > *"Trace our authentication and checkout endpoints and generate the Use Case and Sequence diagrams in PlantUML."*

### 3. One-Click Compile to Vector SVG
Run the built-in script to compile all diagrams into high-resolution SVGs:
```bash
python scripts/render_all.py
```
*(Requires zero local Java or Graphviz installations!)*

---

## Essential AI Prompting Rules

To prevent AI from generating broken or messy diagrams, include these rules in your prompts:

1. **Mermaid Generics**: In Mermaid `classDiagram`, always instruct the AI to use tildes for generic types (`List~Item~`) instead of angle brackets (`List<Item>`), which crash the parser.
2. **PlantUML Styling**: Tell the AI to include `skinparam shadowing false` and a clean slate palette to avoid outdated yellow-box defaults.
3. **SVG Connectors**: Tell the AI to draw connectors behind node boxes and place text labels on opaque background masks.

Complete prompt templates are available in the [`prompts/`](prompts/) directory.

---

## Directory Structure

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

## Author & License

- **Curriculum & Architectural Design**: **Eng. Abdallah Amir**
- **Course**: Advanced Software Engineering
- **License**: [MIT License](LICENSE)
