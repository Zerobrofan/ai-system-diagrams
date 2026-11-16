# Approach 1: System Diagrams with PlantUML & AI

PlantUML is the industry standard for textual UML modeling. It excels at formal software architecture documentation because its domain-specific language (DSL) maps directly onto Object Management Group (OMG) UML specifications.

---

## 1. Diagrams in this Directory

| Diagram | Source File | Rendered Output | Focus & Modeling Concept |
|---|---|---|---|
| **Use Case Diagram** | [`use-case.puml`](use-case.puml) | [`output/use-case.svg`](output/use-case.svg) | System boundary, primary & secondary actors, `<<include>>` and `<<extend>>` dependencies |
| **Class Diagram** | [`class-diagram.puml`](class-diagram.puml) | [`output/class-diagram.svg`](output/class-diagram.svg) | OOP domain model: abstract classes, inheritance (`<|--`), aggregation (`o--`), composition (`*--`), multiplicities |
| **Deployment Diagram** | [`deployment-diagram.puml`](deployment-diagram.puml) | [`output/deployment-diagram.svg`](output/deployment-diagram.svg) | Multi-tier topology: mobile/web clients, IoT gateway, Kubernetes ingress & microservice pods, database replication, external SaaS |

---

## 2. How to Render

You do **not** need Java or Graphviz installed locally. Run our zero-dependency Python script:

```bash
python 1-plantuml/render.py
```

This encodes the diagrams into PlantUML standard deflate-base64 streams and retrieves publication-ready SVGs into `output/`.

---

## 3. How to Prompt AI for PlantUML Diagrams

When asking LLMs (Gemini, Claude, GPT) to generate PlantUML, use these proven prompt guidelines:

### System / Persona Prompt:
> *"You are a Principal Software Architect. Write strict, modern PlantUML (`@startuml` ... `@enduml`). Use modern `skinparam shadowing false` and clean monochrome or slate palettes. Never generate obsolete unstyled yellow boxes."*

### Key Rules to Instruct the AI:
1. **Specify Relationship Types Explicitly**:
   - Inheritance: `<|--`
   - Composition: `*--` (the part dies with the whole)
   - Aggregation: `o--` (independent lifetime)
   - Dependency / Uses: `..>`
2. **Always Request Multiplicities**:
   - Instruct the AI: `"Include multiplicity labels at both ends of associations (e.g. '1' -- '0..*')"`
3. **Control Orientation**:
   - For Use Case: specify `left to right direction` to avoid tall, narrow diagrams.
   - For Class Diagrams: let PlantUML auto-rank or use `-up-`, `-down-`, `-left-`, `-right-` hints if layout tangles.

---

## 4. Strengths & Trade-Offs

### Strengths:
- **Strict UML Compliance**: Supports all official UML 2.5 stereotypes, shapes, and relationship types.
- **Rich Class Compartments**: Native support for visibility modifiers (`+`, `-`, `#`, `~`), parameter types, and return values.
- **Diff & Version Control Friendly**: Clean plain-text files that merge effortlessly in Git.

### Limitations:
- **Layout Fiddliness**: Auto-layout algorithms (Graphviz dot engine) can occasionally route connectors in unexpected loops when models exceed 10+ classes.
- **Visual Modernity**: Default PlantUML styling looks dated unless custom `skinparam` or themes (like `puml-themes`) are explicitly applied.
