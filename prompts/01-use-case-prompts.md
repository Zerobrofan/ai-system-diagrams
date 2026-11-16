# AI Prompt Templates: Use Case Diagrams

Use these structured prompts when asking AI models (Gemini, Claude, ChatGPT) to generate Use Case diagrams for any software system.

---

## 1. PlantUML Prompt

```text
Act as a Senior Software Architect. Create a formal UML 2.5 Use Case diagram for a [System Name, e.g. Hospital Management System].

Requirements:
1. Output ONLY valid PlantUML code enclosed within @startuml and @enduml.
2. Structure:
   - Use 'left to right direction'.
   - Define a clear system boundary using 'rectangle "..." { ... }'.
   - Define primary actors on the left and secondary/external systems on the right.
   - Use cases must be inside the boundary.
3. Dependencies:
   - Include at least two mandatory dependencies using '..> ... : <<include>>'.
   - Include at least one optional/conditional extension using '..> ... : <<extend>>'.
4. Styling:
   - Add modern skinparams: 'skinparam shadowing false', 'skinparam roundcorner 8'.
   - Use a clean palette (navy blue borders, soft blue fills, slate text).
   - Do NOT use default yellow boxes.
```

---

## 2. Mermaid.js Prompt

```text
Act as a Software Engineering Instructor. Generate a clean Mermaid.js Use Case diagram for a [System Name].

Requirements:
1. Output ONLY valid Mermaid syntax starting with 'flowchart LR'.
2. Structure:
   - Subgraph for "Actors" containing primary human actors.
   - Subgraph for "System Boundary" containing use cases.
   - Subgraph for "External Systems" containing secondary systems.
3. Styling & Syntax:
   - Render all Use Cases as stadium/pill shapes: UC_ID(["Use Case Name"]).
   - Model <<include>> relationships as dotted arrows with label: -.->|&laquo;include&raquo;|
   - Model <<extend>> relationships as dotted arrows with label: -.->|&laquo;extend&raquo;|
   - Define classDef styles for actors (subtle gray), use cases (soft blue), and included cases (amber).
```

---

## 3. diagram-design Prompt (Editorial HTML + SVG)

```text
Act as an editorial information designer following the 'diagram-design' standard. Generate a standalone, publication-ready HTML file containing an inline SVG Use Case diagram for a [System Name].

Requirements:
1. Palette: Paper background (#f5f5f5), charcoal ink (#2d3142), slate muted (#4f5d75), and coral accent (#bf4520).
2. Typography: Load Google Fonts 'Instrument Serif' for the h1, 'Geist Mono' for metadata/eyebrows, and 'Geist' for nodes.
3. Geometry:
   - Draw a crisp 1px hairline system boundary rectangle.
   - Actor cards on the left with 1px borders and mono role badges.
   - Use case nodes as pills (rx=18-20) with 1px borders.
   - Draw connector lines BEFORE node boxes so they pass cleanly underneath.
   - Mask all <<include>> and <<extend>> text labels with opaque white background rectangles so lines do not intersect text.
   - Orthogonal connectors with rounded elbows (rx=8). No drop shadows.
   - Include a relationship legend in the bottom corner.
```
