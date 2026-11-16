# Automated Codebase Reverse-Engineering: AI Agent Workflow

This guide details how students and software engineers can install this repository into **any existing software application** inside an `ai-system-diagrams` directory, and instruct an AI coding agent (e.g., Antigravity, Claude Code, GitHub Copilot, Cursor) to inspect the codebase and generate diagrams in **PlantUML**, **Mermaid.js**, or **diagram-design** based on the application's actual architecture.

---

## 1. Installation into an Existing Project

Integrate this framework into any existing repository (Python, Java, C#, Go, TypeScript, Rust, etc.) as an isolated `ai-system-diagrams` subfolder:

### Quick Install
Navigate to your application root directory and run:

```bash
# Option A: Clone into ai-system-diagrams
git clone https://github.com/Zerobrofan/ai-system-diagrams.git ai-system-diagrams

# Option B: Add as a Git Submodule
git submodule add https://github.com/Zerobrofan/ai-system-diagrams.git ai-system-diagrams
```

### Resulting Project Structure
```text
your-project/
├── src/                          # Your application source code
├── tests/                        # Your unit/integration tests
├── package.json / pom.xml / etc.
│
└── ai-system-diagrams/           # Isolated framework directory
    ├── prompts/                  # Architecture diagram specifications & AI prompt rules
    │   ├── structure-diagrams.md
    │   ├── behavior-diagrams.md
    │   ├── interaction-diagrams.md
    │   └── agent-codebase-workflow.md
    ├── scripts/                  # Zero-dependency Python SVG rendering scripts
    │   ├── render_all.py
    │   └── serve.py
    ├── 1-plantuml/               # PlantUML diagrams (.puml) & compiled output/
    ├── 2-mermaid/                # Mermaid diagrams (.mmd) & compiled output/
    ├── 3-diagram-design/         # Editorial HTML/SVG diagrams (.html) & compiled output/
    └── index.html                # Interactive viewer dashboard
```

---

## 2. Agent Execution Workflow

Once installed, open your AI coding assistant within your project workspace. Because the AI agent has read access to your source code, you can instruct it to perform static code analysis and generate diagrams automatically.

### Workflow Step-by-Step

```
┌───────────────────────────────────────────────┐
│ 1. Agent Scans Repository Codebase            │  (Reads models, controllers, schemas, IaC)
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│ 2. Agent Reads Taxonomy Specifications         │  (Reads ai-system-diagrams/prompts/...)
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│ 3. Agent Generates Architectural DSL           │  (Writes .puml, .mmd, or .html)
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│ 4. Local CLI Renders Vector Artifact          │  (Executes python ai-system-diagrams/scripts/render_all.py)
└───────────────────────────────────────────────┘
```

---

## 3. Ready-to-Use Agent Prompts by Approach

You can prompt your AI agent to produce diagrams using any of the 3 supported approaches:

### Approach A: PlantUML (Formal Architecture Docs & UML 2.5)

#### Class Diagram from Code:
```text
Analyze the domain models, entity definitions, and database schemas in this project (e.g., in /src/models or /entities).

Using the UML Class Diagram specification defined in ai-system-diagrams/prompts/structure-diagrams.md:
1. Identify all core business entities, abstract base classes, and interfaces.
2. Extract fields (with visibility modifiers and data types) and business operations.
3. Determine formal relationship semantics (generalization, composition, aggregation, association with multiplicities).
4. Output the complete diagram as ai-system-diagrams/1-plantuml/class-diagram.puml with modern skinparam styling.
```

#### Sequence Diagram from Endpoints:
```text
Trace the execution flow of the [User Registration / Checkout / Authentication] endpoint across our controllers, services, repositories, and third-party gateways.

Using the Sequence Diagram specification defined in ai-system-diagrams/prompts/interaction-diagrams.md:
1. Model all participating lifelines with accurate stereotypes (actor, boundary, control, entity, database).
2. Detail the exact method invocations, synchronous requests, database queries, and return responses.
3. Enclose conditional logic within alt/else frames and loops within loop frames.
4. Output the diagram as ai-system-diagrams/1-plantuml/sequence-diagram.puml.
```

---

### Approach B: Mermaid.js (Markdown-Native & GitHub PRs)

#### Deployment Flowchart from Infrastructure:
```text
Inspect our infrastructure configuration files (e.g., Dockerfiles, docker-compose.yml, Kubernetes manifests).

Using the Deployment Diagram specification defined in ai-system-diagrams/prompts/structure-diagrams.md:
1. Map out execution nodes: reverse proxy/edge, microservice containers, databases, caches, and third-party APIs.
2. Identify container port allocations and network transport protocols (HTTPS, gRPC, JDBC).
3. Generate a Mermaid.js flowchart (flowchart TD) with subgraphs for network zones and save it to ai-system-diagrams/2-mermaid/deployment-diagram.mmd.
```

---

### Approach C: diagram-design (Publication & Slide Decks)

#### Editorial Use Case Diagram:
```text
Trace the primary user workflows and roles in our application (e.g., Patient, Doctor, Administrator).

Using the editorial design guidelines in ai-system-diagrams/prompts/behavior-diagrams.md:
1. Model user actors, system boundary containers, and core use case nodes.
2. Render crisp 1px connectors behind nodes and include colored pill badges for statuses/types.
3. Apply a clean dark aesthetic (#0d1117 background) and output the standalone HTML file to ai-system-diagrams/3-diagram-design/use-case.html.
```

---

## 4. Automated CLI Rendering

After the agent creates or modifies diagram files in `ai-system-diagrams/`, compile them into high-resolution vector SVGs by running:

```bash
# Render all diagrams across all approaches
python ai-system-diagrams/scripts/render_all.py
```

The resulting vector `.svg` files can then be directly embedded into your project's main `README.md`, technical design documents (TDDs), or PR descriptions.
