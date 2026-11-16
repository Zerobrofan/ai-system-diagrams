# AI Prompt Templates: UML Class Diagrams

Use these structured prompts when asking AI models to generate object-oriented domain class diagrams.

---

## 1. PlantUML Prompt

```text
Act as an Object-Oriented Design Architect. Create a detailed domain Class Diagram for [Domain Name, e.g. Hospital Management System].

Requirements:
1. Output ONLY valid PlantUML enclosed within @startuml and @enduml.
2. Modeling Elements:
   - At least 1 abstract class with abstract methods.
   - Distinct visibility modifiers for all fields and methods: '-' private, '#' protected, '+' public.
   - Show parameter names and return types for methods.
3. Relationship Vocabulary:
   - Generalization / Inheritance: '<|--'
   - Composition (strong lifecycle ownership): '*--'
   - Aggregation (independent lifecycle): 'o--'
   - Association with multiplicities on BOTH ends: e.g., '1' -- '0..*'
4. Styling:
   - 'skinparam classAttributeIconSize 0' (use +/-/# text icons instead of circles).
   - 'skinparam shadowing false', modern rounded borders.
```

---

## 2. Mermaid.js Prompt

```text
Act as a Software Architect. Generate a valid Mermaid.js Class Diagram for [Domain Name].

Requirements:
1. Output ONLY valid Mermaid syntax starting with 'classDiagram' and 'direction TB'.
2. Syntax Rules:
   - Abstract classes must include '<<abstract>>'.
   - Visibility modifiers: '+' public, '-' private, '#' protected.
   - IMPORTANT: For generic types (like List, Map, Set), use tildes instead of angle brackets to prevent parsing errors (e.g., 'List~MedicalRecord~', NOT 'List<MedicalRecord>').
3. Relationships & Multiplicities:
   - Inheritance: '<|--'
   - Composition: '*--'
   - Aggregation: 'o--'
   - Association with multiplicities: ClassA "1" --> "0..*" ClassB : label
```

---

## 3. diagram-design Prompt (Editorial HTML + SVG)

```text
Act as an editorial information designer adhering strictly to the 'type-uml-class.md' diagram-design specification. Generate a standalone HTML file with inline SVG for [Domain Name].

Requirements:
1. Visual Rules:
   - Each class is a single card (rx=6) divided by 1px horizontal hairlines into 3 compartments: Name (centered, 12px weight 600), Attributes (+ name: Type, left-aligned, 9px mono), and Operations (+ method(): Return, left-aligned, 9px mono).
   - Do NOT pad cards to equal height; card height must strictly match its members.
   - Max 6 to 7 classes to prevent visual clutter.
   - Reserve coral (#bf4520) accent fill/stroke for the single focal class of the domain.
2. Relationship Markers in <defs>:
   - uml-triangle: hollow triangle for inheritance.
   - uml-diamond-filled: black filled diamond at the owner end for composition.
   - uml-diamond-hollow: hollow diamond at the owner end for aggregation.
   - uml-open: open arrowhead for association.
3. Multiplicities:
   - Place multiplicity numbers ('1', '0..*', '1..*') on opaque background masks over the connector lines.
4. Legend:
   - Include a box in the bottom right corner showing the 4 primary relationship markers and their meanings.
```
