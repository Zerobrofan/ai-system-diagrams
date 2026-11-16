# Advanced Software Engineering: AI System Prompting Guide

When leveraging Large Language Models (LLMs) like Claude, Gemini, or GPT to produce architectural diagrams, generic prompts (`"draw me a class diagram"`) almost always yield poor, unmaintainable results.

This guide provides the foundational rules, persona system prompts, and common failure modes to avoid.

---

## 1. Master System Prompt for Coding Assistants

Set this as your Custom Instructions or System Prompt in your AI assistant:

```text
You are an expert Software Architect and Information Designer specializing in Advanced Software Engineering modeling.

When asked to generate system diagrams:
1. Always adhere to strict, formal UML 2.5 semantics for relationship types (inheritance, realization, composition, aggregation, association, dependency).
2. Choose the appropriate tool syntax requested:
   - For PlantUML: Write valid @startuml ... @enduml with modern skinparam styling (shadowing false, no default yellow).
   - For Mermaid: Write idiomatic Mermaid. Never invent non-existent diagram keywords; for Use Cases, use flowchart LR with subgraphs and stadium nodes. For class generic types, always use tildes (List~T~) rather than angle brackets.
   - For diagram-design: Produce publication-grade, self-contained HTML + SVG with 1px hairlines, Geist & Instrument Serif fonts, #f5f5f5 paper palette, orthogonal rounded elbows, and masked labels.
3. Keep complexity bounded: Focus on core domain behavior rather than dumping trivial getters/setters or every database column.
4. Always provide source code enclosed in proper markdown fences.
```

---

## 2. Common AI Diagramming Failure Modes & How to Fix Them

| Failure Mode | Why AI Does It | How to Prevent It |
|---|---|---|
| **Angle Brackets in Mermaid Generics** (`List<Patient>`) | AI defaults to Java/C# syntax, which causes the Mermaid tokenizer to fail. | Instruct: *"Use tildes for Mermaid generic types: `List~Patient~`"*. |
| **Interchangeable Composition & Aggregation** | LLMs often confuse black filled diamonds (`*--`) with hollow diamonds (`o--`). | Explicitly state: *"Use composition only when the child lifecycle depends entirely on the parent; otherwise use aggregation or association."* |
| **Blob / Monolith Class Diagrams** | LLM dumps 30 attributes and 20 getters/setters per class, creating unreadable diagrams. | Instruct: *"Show maximum 4-5 key business attributes and 2-3 behavioral domain methods per class. Omit trivial getters and setters."* |
| **Tangled Diagonals in SVG / HTML** | Auto-generating SVG without layout constraints produces criss-crossing diagonals over text. | Instruct: *"All connectors must use orthogonal 90-degree paths with rounded elbows (`rx=8`) and pass behind node cards."* |
| **Outdated PlantUML Skins** | PlantUML defaults to 1990s yellow gradients and drop shadows. | Instruct: *"Include modern skinparam with `shadowing false` and clean monochrome or slate palette."* |

---

## 3. Tool Selection Decision Matrix

```
                                  DO YOU NEED...
                                        │
           ┌────────────────────────────┼────────────────────────────┐
           ▼                            ▼                            ▼
  Strict UML 2.5 Standard      Fast Markdown / GitHub      Publication / Presentation
  Formal Academic & Enterprise PRs, Issues, Notion docs   Whitepapers, Slidedecks, Web
           │                            │                            │
           ▼                            ▼                            ▼
     [PlantUML]                    [Mermaid.js]               [diagram-design]
  (DSL · Rich UML types)      (Markdown-native · Zero build)  (Editorial HTML+SVG · 1px)
```
