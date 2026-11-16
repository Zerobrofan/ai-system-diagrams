# AI-Assisted System Architecture Diagramming

### A Formal UML 2.5 Specification, Multi-Paradigm Benchmark, and Automated Codebase Reverse-Engineering Framework for Advanced Software Engineering

**Curriculum & Architectural Design:** Eng. Abdallah Amir  
**Academic Course:** Advanced Software Engineering & System Architecture  
**Standards Compliance:** OMG Unified Modeling Language (UML) Specification Version 2.5.1  
**License:** MIT Open-Source License  

---

## 1. Executive Summary

Communicating software architecture through formal visual models is essential for managing complexity, enforcing design invariants, and auditing distributed systems. While modern Large Language Models (LLMs) and AI coding assistants can generate diagrammatic code, naive prompting typically yields unmaintainable outputs characterized by hallucinated syntax, tangled routing, missing multiplicity bounds, and obsolete styling.

This framework provides an engineering-grade laboratory for Advanced Software Engineering students and practitioners. It establishes:

1. **Complete UML 2.5 Taxonomy Coverage**: Formal architectural definitions, engineering objectives, and structured prompt templates across all 14 official UML diagram types (Structure, Behaviour, and Interaction subcategories).
2. **Multi-Paradigm Comparative Benchmark**: Direct comparison between PlantUML (formal DSL), Mermaid.js (markdown-native), and Cathryn Lavery's `diagram-design` (editorial HTML/SVG) across a cohesive case study (the MedPulse Smart Hospital Management System).
3. **Universal Project Integration**: A standardized workflow enabling developers to drop this framework into any existing application repository, allowing AI coding assistants to statically analyze the codebase and synthesize accurate architecture diagrams.
4. **Zero-Dependency Rendering Tooling**: Self-contained Python scripts capable of compiling PlantUML, Mermaid, and diagram-design assets into publication-ready vector SVGs without requiring local Java, Graphviz, or headless browser runtimes.

---

## 2. Complete UML 2.5 Diagram Taxonomy & Architectural Use Cases

The Object Management Group (OMG) specifies 14 formal diagram types categorized into two primary branches: **Structure Diagrams** and **Behaviour Diagrams** (which includes **Interaction Diagrams** as a specialized abstract subcategory).

```
UML 2.5 Diagram Taxonomy
├── Structure Diagrams (Abstract Subcategory)
│   ├── Class Diagram
│   ├── Component Diagram
│   ├── Composite Structure Diagram
│   ├── Deployment Diagram
│   ├── Object Diagram
│   ├── Package Diagram
│   └── Profile Diagram
└── Behaviour Diagrams (Abstract Subcategory)
    ├── Use Case Diagram
    ├── Activity Diagram
    ├── State Machine Diagram
    └── Interaction Diagrams (Abstract Subcategory)
        ├── Sequence Diagram
        ├── Communication Diagram
        ├── Interaction Overview Diagram
        └── Timing Diagram
```

---

### 2.1 Structure Diagrams (Abstract Subcategory)

Structure diagrams capture the static, time-invariant configuration of a system, detailing classes, interfaces, component dependencies, and physical deployment topologies.

| Diagram Type | Formal Architectural Purpose | Concrete Software Engineering Use Cases | Specification & Prompts |
|---|---|---|---|
| **Class Diagram** | Models classifiers, attributes, operations, visibility, and typed relationships (generalization, realization, association, aggregation, composition). | Domain-driven design (DDD) entities, Object-Relational Mapping (ORM) schemas, contract interfaces, and object-oriented inheritance hierarchies. | [`prompts/structure-diagrams.md#1-class-diagram`](prompts/structure-diagrams.md#1-class-diagram) |
| **Component Diagram** | Illustrates modular units of functionality, provided interfaces (APIs offered), required interfaces (dependencies), and interconnecting ports. | Microservice boundaries, modular monolith package isolation, API gateway service contracts, and reusable library dependencies. | [`prompts/structure-diagrams.md#2-component-diagram`](prompts/structure-diagrams.md#2-component-diagram) |
| **Composite Structure Diagram** | Deconstructs the internal execution topology of a single classifier, showing internal parts, ports, and connector channels. | Port-and-Adapter (Hexagonal / Clean) architectures, internal event mediator wiring, and complex structural design patterns. | [`prompts/structure-diagrams.md#3-composite-structure-diagram`](prompts/structure-diagrams.md#3-composite-structure-diagram) |
| **Deployment Diagram** | Models the physical and virtual execution environment, hardware nodes, container orchestrators, artifact manifests, and network communication paths. | Kubernetes cluster pod allocations, cloud infrastructure topologies (AWS/Azure/GCP), secure VPC subnets, and high-availability database replication. | [`prompts/structure-diagrams.md#4-deployment-diagram`](prompts/structure-diagrams.md#4-deployment-diagram) |
| **Object Diagram** | Represents a point-in-time snapshot of instantiated objects, concrete attribute state values, and active reference links. | Debugging complex runtime memory allocations, testing edge-case object graphs, and visualizing design pattern state before and after execution. | [`prompts/structure-diagrams.md#5-object-diagram`](prompts/structure-diagrams.md#5-object-diagram) |
| **Package Diagram** | Organizes model elements, namespaces, and source code modules into hierarchical groupings, modeling compile-time dependencies and imports. | Enforcing clean architecture layering (Presentation -> Application -> Domain -> Infrastructure) and preventing circular package dependencies. | [`prompts/structure-diagrams.md#6-package-diagram`](prompts/structure-diagrams.md#6-package-diagram) |
| **Profile Diagram** | A metamodel extension diagram that defines domain-specific stereotypes, tagged values, and constraints to tailor UML to specialized platforms. | Tailoring UML for enterprise frameworks (Spring Boot, .NET, Angular), cloud architectures, or compliance standards (HIPAA, ISO 26262). | [`prompts/structure-diagrams.md#7-profile-diagram`](prompts/structure-diagrams.md#7-profile-diagram) |

---

### 2.2 Behaviour Diagrams (Abstract Subcategory)

Behaviour diagrams specify the dynamic execution, operational workflows, and state lifecycles of a system over time.

| Diagram Type | Formal Architectural Purpose | Concrete Software Engineering Use Cases | Specification & Prompts |
|---|---|---|---|
| **Use Case Diagram** | Specifies system boundary scope, external actors (human users and external third-party services), and functional use cases connected via `<<include>>` and `<<extend>>`. | Requirements engineering, system scoping, defining boundary authentication preconditions, and structuring end-to-end acceptance tests. | [`prompts/behavior-diagrams.md#1-use-case-diagram`](prompts/behavior-diagrams.md#1-use-case-diagram) |
| **Activity Diagram** | Models procedural step-by-step control flows and object flows, incorporating decision branching, concurrency forks/joins, and swimlanes. | Complex transactional workflows, multi-step checkout sagas, asynchronous data transformation pipelines, and cross-departmental operations. | [`prompts/behavior-diagrams.md#2-activity-diagram`](prompts/behavior-diagrams.md#2-activity-diagram) |
| **State Machine Diagram** | Models the discrete event-driven state transitions, triggers, guard conditions `[condition]`, and actions (`entry/`, `do/`, `exit/`) of a reactive classifier. | Entity lifecycles (Order, Ticket, Account, Session), protocol state engines, embedded hardware state tracking, and State pattern implementations. | [`prompts/behavior-diagrams.md#3-state-machine-diagram`](prompts/behavior-diagrams.md#3-state-machine-diagram) |

---

### 2.3 Interaction Diagrams (Abstract Subcategory)

Interaction diagrams are a specialized subset of behaviour diagrams that focus explicitly on message passing, control transfers, and conversational sequencing between collaborating lifelines.

| Diagram Type | Formal Architectural Purpose | Concrete Software Engineering Use Cases | Specification & Prompts |
|---|---|---|---|
| **Sequence Diagram** | Chronologically plots message exchanges between object lifelines, showing synchronous calls, asynchronous events, activation bars, and frames (`alt`, `loop`, `par`). | Multi-service API call chains, authentication handshakes (OAuth2, OIDC, mTLS), distributed transaction tracing, and race condition analysis. | [`prompts/interaction-diagrams.md#1-sequence-diagram`](prompts/interaction-diagrams.md#1-sequence-diagram) |
| **Communication Diagram** | Focuses on structural link topologies between collaborating objects, with hierarchical dot-numbered sequence labels (e.g., `1.1: request()`, `1.2: validate()`). | Evaluating structural coupling between classes, analyzing refactoring candidates with high fan-out, and visualizing network routing paths. | [`prompts/interaction-diagrams.md#2-communication-diagram-collaboration`](prompts/interaction-diagrams.md#2-communication-diagram-collaboration) |
| **Interaction Overview Diagram** | A macro-level composite diagram that combines activity flow nodes with framed interaction occurrences (subordinate sequence flows). | Enterprise business process orchestration, high-level pipeline governance, and navigating complex multi-stage distributed user journeys. | [`prompts/interaction-diagrams.md#3-interaction-overview-diagram`](prompts/interaction-diagrams.md#3-interaction-overview-diagram) |
| **Timing Diagram** | Plots continuous or discrete state changes along a calibrated horizontal time axis, explicitly quantifying duration and latency constraints. | Real-time and safety-critical systems, hardware communication buses (SPI, I2C, CAN), timeout threshold verification, and circuit breaker tuning. | [`prompts/interaction-diagrams.md#4-timing-diagram`](prompts/interaction-diagrams.md#4-timing-diagram) |

---

## 3. Universal Project Integration: Reverse-Engineering Any Codebase

A primary capability of this framework is its portability: developers and students can install this framework directly into **any software application repository** (Java, Python, C#, TypeScript, Go, Rust, etc.) and instruct an AI coding agent to inspect the code and generate architecture diagrams automatically.

### 3.1 Installation into an Existing Project

#### Option A: Git Submodule (Recommended)
From the root of your target application repository, run:
```bash
git submodule add https://github.com/AbdallahAmir/ai-system-diagrams.git docs/diagrams
```

#### Option B: Standalone Directory Copy
Copy the `prompts/`, `scripts/`, `1-plantuml/`, `2-mermaid/`, and `3-diagram-design/` directories into a documentation directory (e.g., `docs/architecture/`):
```text
your-project/
├── src/
├── tests/
├── docs/
│   └── architecture/
│       ├── prompts/
│       ├── scripts/
│       ├── 1-plantuml/
│       ├── 2-mermaid/
│       └── 3-diagram-design/
└── README.md
```

### 3.2 Instructing the AI Agent to Generate Diagrams from Code

Once placed in your project directory, open your AI coding agent (e.g., Antigravity, Claude Code, Cursor, GitHub Copilot) and provide targeted instructions pointing to your source files:

#### Task 1: Generate Class Diagram from Domain Models
```text
Inspect the entity models and database mappings in /src/models.
Using the specification in docs/architecture/prompts/structure-diagrams.md:
1. Identify all core business entities, abstract base classes, and interfaces.
2. Extract fields (with visibility modifiers and data types) and business operations.
3. Determine formal relationship semantics (generalization, composition, aggregation, association with multiplicities).
4. Output the complete diagram as docs/architecture/1-plantuml/class-diagram.puml with modern skinparam styling.
```

#### Task 2: Generate Deployment Diagram from Infrastructure Code
```text
Inspect our infrastructure configurations (Dockerfiles, docker-compose.yml, Kubernetes manifests, Terraform files).
Using the specification in docs/architecture/prompts/structure-diagrams.md:
1. Map out execution tiers: client devices, reverse proxies, microservice containers, databases, caches, and third-party SaaS.
2. Extract port mappings and network protocols (HTTPS, gRPC, JDBC, AMQP).
3. Generate a UML 2.5 Deployment diagram in PlantUML and write it to docs/architecture/1-plantuml/deployment-diagram.puml.
```

#### Task 3: Generate Sequence Diagram from Controller Endpoints
```text
Trace the execution path of the primary checkout endpoint across controllers, services, and external payment APIs.
Using the specification in docs/architecture/prompts/interaction-diagrams.md:
1. Model lifelines with explicit stereotypes (boundary, control, entity, database).
2. Trace synchronous blocking invocations, asynchronous messages, and return payloads.
3. Enclose conditional logic in alt frames and loops in loop frames.
4. Output the diagram as docs/architecture/1-plantuml/sequence-diagram.puml.
```

For complete reverse-engineering guidelines and prompt patterns, refer to [`prompts/agent-codebase-workflow.md`](prompts/agent-codebase-workflow.md).

---

## 4. Multi-Paradigm Comparison: PlantUML vs Mermaid.js vs diagram-design

This framework implements a benchmark across three prominent diagramming paradigms:

| Evaluation Dimension | PlantUML | Mermaid.js | diagram-design |
|---|---|---|---|
| **Authoring Format** | Plain-text Domain-Specific Language (DSL) | Markdown-embedded DSL | Standalone HTML with inline SVG |
| **Standard Adherence** | Full adherence to OMG UML 2.5 metamodel | Pragmatic subset; flowcharts used for Use Cases | Mathematical geometric layout per spec sheet |
| **Rendering Dependencies** | Zero local Java (handled via Deflate HTTP script) | Zero build (renders client-side or via API) | Zero build (opens directly in modern browsers) |
| **GitHub Native Display** | Requires pre-rendered SVG/PNG | Renders natively inside Markdown fences | Embeds exported SVG or links to HTML |
| **Visual Density & Style** | Corporate/Academic clean slate via `skinparam` | Modern default vector flowchart/class styles | Editorial-grade 1px hairlines, Geist & Instrument typography |
| **Maintenance Burden** | Low (compact 20-50 line plain text DSL) | Low (compact 20-50 line plain text DSL) | Moderate (120-250 lines of structured SVG) |
| **Optimal Use Case** | Formal specifications, thesis defense, lab reports | GitHub PRs, Agile documentation, Notion wikis | Executive briefs, conference slides, whitepapers |

---

## 5. Case Study: MedPulse Smart Hospital Management System

To illustrate these paradigms on an identical architectural model, the repository includes complete implementations of three core diagrams for a Smart Hospital Management System:

### 5.1 Use Case Model
- **Boundary**: MedPulse Clinical System Boundary.
- **Actors**: Human users (*Patient, Doctor, Nurse, Hospital Admin*) and secondary systems (*Insurance Clearinghouse*).
- **Dependencies**: Mandatory `<<include>>` (*Verify Identity / 2FA*, *Cross-Check Drug Allergies*) and conditional `<<extend>>` (*Telehealth Video Session*, *Insurance Claim Submission*).
- **Artifacts**:
  - PlantUML: [`1-plantuml/use-case.puml`](1-plantuml/use-case.puml) | [Vector SVG](1-plantuml/output/use-case.svg)
  - Mermaid.js: [`2-mermaid/use-case.mmd`](2-mermaid/use-case.mmd) | [Vector SVG](2-mermaid/output/use-case.svg)
  - diagram-design: [`3-diagram-design/use-case.html`](3-diagram-design/use-case.html) | [Vector SVG](3-diagram-design/output/use-case.svg)

### 5.2 Domain Class Model
- **Entities**: Abstract `User` base class, specialized `Patient`, `Staff`, `Doctor`, and `Nurse` classes.
- **Relationships**: `Department` aggregation (`1` o-- `1..*`), `Appointment` association with multiplicities, and `MedicalRecord` composition (`1` *-- `0..*` `Prescription` *-- `1..*` `PrescriptionItem`).
- **Artifacts**:
  - PlantUML: [`1-plantuml/class-diagram.puml`](1-plantuml/class-diagram.puml) | [Vector SVG](1-plantuml/output/class-diagram.svg)
  - Mermaid.js: [`2-mermaid/class-diagram.mmd`](2-mermaid/class-diagram.mmd) | [Vector SVG](2-mermaid/output/class-diagram.svg)
  - diagram-design: [`3-diagram-design/class-diagram.html`](3-diagram-design/class-diagram.html) | [Vector SVG](3-diagram-design/output/class-diagram.svg)

### 5.3 Physical Deployment Model
- **Tiers**: Client Edge (*Flutter, React 19, Bedside IoT*), Edge/DMZ (*Cloudflare WAF*), Kubernetes Cluster (*Spring Gateway, Go, Java, Python microservices*), Encrypted Data Tier (*PostgreSQL Primary-Replica, Redis, S3*), and External SaaS (*FHIR v4, Stripe*).
- **Artifacts**:
  - PlantUML: [`1-plantuml/deployment-diagram.puml`](1-plantuml/deployment-diagram.puml) | [Vector SVG](1-plantuml/output/deployment-diagram.svg)
  - Mermaid.js: [`2-mermaid/deployment-diagram.mmd`](2-mermaid/deployment-diagram.mmd) | [Vector SVG](2-mermaid/output/deployment-diagram.svg)
  - diagram-design: [`3-diagram-design/deployment-diagram.html`](3-diagram-design/deployment-diagram.html) | [Vector SVG](3-diagram-design/output/deployment-diagram.svg)

---

## 6. Execution and Rendering Commands

All rendering scripts are built in pure Python using built-in standard libraries (`zlib`, `urllib`, `base64`), eliminating external binary dependencies:

```bash
# Render all diagrams across all approaches in a single pass
python scripts/render_all.py

# Launch the local interactive comparison dashboard
python scripts/serve.py

# Render individual approaches independently
python 1-plantuml/render.py
python 2-mermaid/render.py
python 3-diagram-design/render.py
```

---

## 7. Directory Structure

```text
ai-system-diagrams/
├── README.md                          # Master architectural guide and curriculum documentation
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Guidelines for contributing new domains and prompts
├── SECURITY.md                        # Architecture sanitization and secret handling policy
├── package.json                       # Automation scripts for Node/npm toolchains
├── index.html                         # Interactive multi-view comparison dashboard
│
├── 1-plantuml/                        # Approach 1: PlantUML Implementation
│   ├── README.md                      # PlantUML skinparam configurations and DSL rules
│   ├── use-case.puml                  # MedPulse Use Case diagram source
│   ├── class-diagram.puml             # MedPulse Domain Class diagram source
│   ├── deployment-diagram.puml        # MedPulse Deployment diagram source
│   ├── render.py                      # Pure-Python PlantUML Deflate-to-SVG compiler
│   └── output/                        # Compiled vector SVGs
│
├── 2-mermaid/                         # Approach 2: Mermaid.js Implementation
│   ├── README.md                      # Mermaid syntax guide and generic type rules
│   ├── use-case.mmd                   # MedPulse Use Case diagram source
│   ├── class-diagram.mmd              # MedPulse Domain Class diagram source
│   ├── deployment-diagram.mmd         # MedPulse Deployment diagram source
│   ├── preview.html                   # Client-side live browser viewer
│   ├── render.py                      # Pure-Python Mermaid-to-SVG compiler
│   └── output/                        # Compiled vector SVGs
│
├── 3-diagram-design/                  # Approach 3: diagram-design Implementation
│   ├── README.md                      # Editorial design rules and typography specs
│   ├── use-case.html                  # Editorial Use Case diagram source
│   ├── class-diagram.html             # Editorial UML Class diagram source
│   ├── deployment-diagram.html        # Editorial Deployment diagram source
│   ├── render.py                      # SVG extraction script
│   └── output/                        # Extracted standalone vector SVGs
│
├── prompts/                           # Structured Prompt Templates and Taxonomy Specifications
│   ├── structure-diagrams.md          # Class, Component, Composite, Deployment, Object, Package, Profile
│   ├── behavior-diagrams.md           # Use Case, Activity, State Machine
│   ├── interaction-diagrams.md        # Sequence, Communication, Interaction Overview, Timing
│   ├── agent-codebase-workflow.md     # Codebase reverse-engineering instructions for AI agents
│   ├── 01-use-case-prompts.md         # Dedicated Use Case prompt variants
│   ├── 02-class-diagram-prompts.md    # Dedicated Class diagram prompt variants
│   ├── 03-deployment-diagram-prompts.md # Dedicated Deployment diagram prompt variants
│   └── system-prompts-guide.md        # Master system prompts and anti-hallucination rules
│
├── scripts/                           # Central Automation Tooling
│   ├── render_all.py                  # One-command compiler for all 9 diagrams
│   └── serve.py                       # Lightweight local HTTP server
│
└── diagram-design-framework/          # Reference assets, style guides, and extractor scripts
```

---

## 8. Author Attribution and License

- **Architectural Curriculum & Design:** Eng. Abdallah Amir
- **Course:** Advanced Software Engineering
- **License:** Licensed under the [MIT License](LICENSE). Academic institutions, students, and software engineers are permitted to use, modify, and adapt this framework in software engineering courses and commercial projects.
