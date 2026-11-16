# Contributing to AI System Diagrams Laboratory

Welcome! We are thrilled you want to contribute to the **AI System Diagrams Laboratory for Advanced Software Engineering**.

Whether you are adding a new diagram type, contributing a new software system domain (e.g., E-Commerce, Fintech, Ride-Sharing), or optimizing AI prompt templates, your contributions help software engineering students worldwide.

---

## 🚀 How to Contribute

### 1. Adding a New System Domain
If you want to showcase a new domain (e.g., *Smart Library*, *Autonomous Drone Fleet*, *Online Banking*):
1. Create a branch: `git checkout -b feature/domain-name`.
2. Model all three diagrams:
   - **Use Case Diagram** (including `<<include>>` and `<<extend>>`).
   - **Class Diagram** (with inheritance, composition, aggregation, and typed multiplicities).
   - **Deployment Diagram** (with client, edge, compute, data, and external tiers).
3. Provide the source files for all three approaches:
   - PlantUML (`.puml`)
   - Mermaid.js (`.mmd`)
   - diagram-design (`.html`)
4. Ensure the diagrams render cleanly via `python scripts/render_all.py`.

### 2. Improving AI Prompt Templates
If you discovered an effective prompting technique that eliminates AI hallucinations or improves diagram layout:
1. Open [`prompts/`](prompts/).
2. Add your prompt pattern and explain the rationale in `system-prompts-guide.md`.
3. Submit a Pull Request with a clear description and example output.

---

## 🎨 Quality & Anti-Slop Guidelines

1. **No "Mermaid Slop"**: Ensure diagram layouts are bounded and readable. Avoid 30+ node blobs with overlapping connector lines.
2. **Strict UML 2.5 Semantics**:
   - Inheritance: `<|--`
   - Composition: `*--` (the child dies with the whole)
   - Aggregation: `o--` (independent lifetime)
   - Association: `-->` with multiplicities at both ends (`1`, `0..*`, `1..*`).
3. **PlantUML Styling**: Always include `skinparam shadowing false` and a clean, high-contrast palette. Never submit default yellow-box diagrams.
4. **diagram-design Adherence**: Follow Cathryn Lavery's specifications in `diagram-design-framework/`: 1px hairlines, Geist/Instrument typography, `#f5f5f5` paper, `#2d3142` ink, and masked labels.

---

## 📝 Pull Request Checklist

- [ ] Diagrams render to SVG without errors (`python scripts/render_all.py`).
- [ ] Diagram source code is formatted and commented.
- [ ] Prompt templates are included in the `prompts/` directory.
- [ ] `index.html` showcases the newly added diagrams.

Thank you for contributing to modern software engineering education!
