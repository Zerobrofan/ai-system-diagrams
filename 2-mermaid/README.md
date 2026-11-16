# Approach 2: System Diagrams with Mermaid.js & AI

Mermaid.js is the de facto standard for markdown-native diagramming. It is natively rendered by GitHub, GitLab, Notion, Obsidian, Azure DevOps, and ChatGPT/Claude web interfaces without requiring any compilation step.

---

## 1. Diagrams in this Directory

| Diagram | Source File | Rendered Output | Focus & Modeling Concept |
|---|---|---|---|
| **Use Case Diagram** | [`use-case.mmd`](use-case.mmd) | [`output/use-case.svg`](output/use-case.svg) | Modeled via `flowchart LR` with subgraphs, actor nodes, stadium use cases `([ ... ])`, `<<include>>` and `<<extend>>` dotted links |
| **Class Diagram** | [`class-diagram.mmd`](class-diagram.mmd) | [`output/class-diagram.svg`](output/class-diagram.svg) | Native `classDiagram`: inheritance (`<|--`), aggregation (`o--`), composition (`*--`), typed methods, visibility modifiers (`+`, `-`, `#`) |
| **Deployment Diagram** | [`deployment-diagram.mmd`](deployment-diagram.mmd) | [`output/deployment-diagram.svg`](output/deployment-diagram.svg) | Structured `flowchart TB` subgraphs: Client tier, Cloudflare WAF/Edge, Kubernetes pods, encrypted PostgreSQL/Redis/S3 data tier, third-party APIs |

---

## 2. How to View & Render

### Option A: Open the Interactive Local Preview (Recommended)
Open [`preview.html`](preview.html) directly in any modern web browser. It renders the `.mmd` diagrams using the official client-side Mermaid engine with live tab switching.

### Option B: Export Standalone SVGs via Python
Run the zero-dependency Python script:

```bash
python 2-mermaid/render.py
```

This retrieves standalone, vector SVGs into `output/` using base64 URL encoding.

---

## 3. How to Prompt AI for Mermaid Diagrams

When working with LLMs for Mermaid code, follow these techniques:

### Critical Prompt Instructions:
1. **Use Case Workaround**:
   > *"Mermaid has no native `usecase` diagram keyword. Model Use Cases using `flowchart LR`. Place actors in an Actors subgraph on the left, use stadium shapes `([Use Case Name])` inside a System Boundary subgraph, and label dotted relations with `-.->|&laquo;include&raquo;|`."*
2. **Class Diagram Generic Types**:
   > *"In Mermaid `classDiagram`, generic collections must use tildes rather than angle brackets (e.g., `List~MedicalRecord~` instead of `List<MedicalRecord>`), otherwise the Mermaid parser crashes."*
3. **Control Visual Hierarchy with Subgraphs**:
   > *"Group deployment nodes into nested `subgraph` blocks with clear directions (`direction TB` or `direction LR`) and assign semantic classDef styles."*

---

## 4. Strengths & Trade-Offs

### Strengths:
- **Zero-Build Markdown Integration**: Pastes directly into GitHub markdown files (` ```mermaid `) and renders immediately in GitHub pull requests, issues, and READMEs.
- **Widespread Tooling Support**: Supported in IDE extensions (VS Code Markdown Preview Mermaid Support, JetBrains, Obsidian).
- **Lightweight Syntax**: Highly readable, concise text syntax.

### Limitations:
- **No Native Use Case Grammar**: Requires convention-based flowchart adaptation.
- **Complex Edge Routing**: Large class diagrams with many cross-cutting dependencies can produce overlapping or tangled connector lines.
- **Limited Styling Customization**: Less pixel-level visual control compared to SVG/editorial design systems.
