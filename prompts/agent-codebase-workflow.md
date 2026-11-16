# Automated Codebase Reverse-Engineering: AI Agent Workflow

This guide details how students and software engineers can install this repository into **any existing software application** and instruct an AI coding agent (e.g., Antigravity, Claude Code, GitHub Copilot, Cursor) to inspect the codebase and generate diagrams based on the application's actual architecture.

---

## 1. Installation into an Existing Project

You can integrate this framework into any existing repository (Python, Java, C#, Go, TypeScript, Rust, etc.) using one of three methods:

### Method A: Git Submodule (Recommended for Version Control)
Navigate to your application root directory and run:
```bash
git submodule add https://github.com/AbdallahAmir/ai-system-diagrams.git docs/diagrams
```

### Method B: Directory Copy
Copy the `prompts/`, `scripts/`, `1-plantuml/`, `2-mermaid/`, and `3-diagram-design/` directories directly into a dedicated documentation folder within your project:
```text
your-application/
├── src/
├── tests/
├── docs/
│   └── architecture/          <-- Placed here
│       ├── prompts/
│       ├── scripts/
│       ├── 1-plantuml/
│       ├── 2-mermaid/
│       └── 3-diagram-design/
└── README.md
```

---

## 2. Agent Execution Workflow

Once installed, open your AI coding assistant within your project workspace. Because the AI agent has read access to your source code, you can instruct it to perform static code analysis and generate diagrams automatically.

### Workflow Step-by-Step

```
┌───────────────────────────────────────┐
│ 1. Agent Scans Repository Codebase    │  (Reads models, controllers, schemas, IaC)
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ 2. Agent Reads Taxonomy Specifications │  (Reads prompts/structure-diagrams.md, etc.)
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ 3. Agent Generates Architectural DSL   │  (Writes .puml, .mmd, or .html)
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ 4. Local CLI Renders Vector Artifact  │  (Executes python scripts/render_all.py)
└───────────────────────────────────────┘
```

---

## 3. Ready-to-Use Agent Prompts

Copy and paste these exact instructions into your AI coding assistant in your project:

### Prompt 1: Reverse-Engineer Domain Class Diagram from Code
```text
Analyze the domain models, entity definitions, and database schemas in this project (e.g., in /src/models or /entities).

Using the UML Class Diagram specification defined in docs/diagrams/prompts/structure-diagrams.md:
1. Identify all core business entities, abstract base classes, and interfaces.
2. Extract fields (with visibility modifiers and data types) and business operations.
3. Determine formal relationship semantics (generalization, composition, aggregation, association with multiplicities).
4. Output the complete diagram as docs/diagrams/1-plantuml/class-diagram.puml with modern skinparam styling.
```

### Prompt 2: Extract Deployment Architecture from Infrastructure Code
```text
Inspect our infrastructure configuration files (e.g., Dockerfiles, docker-compose.yml, Kubernetes manifests, Terraform files, Helm charts).

Using the Deployment Diagram specification defined in docs/diagrams/prompts/structure-diagrams.md:
1. Map out all execution nodes: client tier, reverse proxy / edge, compute microservice containers, persistence databases, caches, and external third-party APIs.
2. Identify container port allocations and network transport protocols (HTTPS, gRPC, JDBC, AMQP).
3. Generate a UML 2.5 Deployment diagram in PlantUML and write it to docs/diagrams/1-plantuml/deployment-diagram.puml.
```

### Prompt 3: Reverse-Engineer Transaction Sequence Diagram from Endpoints
```text
Trace the execution flow of the [User Registration / Checkout / Authentication] endpoint across our controllers, services, repositories, and third-party gateways.

Using the Sequence Diagram specification defined in docs/diagrams/prompts/interaction-diagrams.md:
1. Model all participating lifelines with accurate stereotypes (actor, boundary, control, entity, database).
2. Detail the exact method invocations, synchronous requests, database queries, and return responses.
3. Enclose conditional logic within alt/else frames and loops within loop frames.
4. Output the diagram as docs/diagrams/1-plantuml/sequence-diagram.puml.
```

### Prompt 4: Reverse-Engineer Entity State Machine from Lifecycle Enums
```text
Inspect the lifecycle states and status transitions of the [Order / Ticket / Account / Task] entity in our codebase.

Using the State Machine specification defined in docs/diagrams/prompts/behavior-diagrams.md:
1. Identify all enum values representing states.
2. Identify all service methods and event listeners that trigger state transitions.
3. Extract guard conditions and transition effects.
4. Generate a formal State Machine diagram in PlantUML and write it to docs/diagrams/1-plantuml/state-machine.puml.
```

---

## 4. Automated CLI Rendering

After the agent creates or modifies the `.puml`, `.mmd`, or `.html` files in your project, render the high-resolution vector SVGs by running:

```bash
# Render all diagrams across all approaches
python docs/diagrams/scripts/render_all.py
```

The resulting vector `.svg` files can then be directly embedded into your project's main `README.md`, technical design documents (TDDs), or PR descriptions.
