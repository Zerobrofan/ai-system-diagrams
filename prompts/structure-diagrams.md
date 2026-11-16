# UML 2.5 Structure Diagrams: Specifications and Prompt Templates

Structure diagrams represent the static aspects of a software system. They model the entities, interfaces, packages, components, and physical hardware nodes that exist across the software lifecycle, independent of time.

---

## Taxonomy of Structure Diagrams

```
Structure Diagram (Abstract Classification)
├── Class Diagram
├── Component Diagram
├── Composite Structure Diagram
├── Deployment Diagram
├── Object Diagram
├── Package Diagram
└── Profile Diagram
```

---

## 1. Class Diagram

### Engineering Purpose
Captures the object-oriented domain model, data contracts, and class relationships. It models class attributes, operations, visibility constraints, inheritance hierarchies, interface realizations, aggregations, and compositions.

### When to Select
- Defining domain-driven design (DDD) entities and value objects.
- Establishing formal object models before implementation.
- Documenting database ORM entity mappings and relationships.

### AI Prompt Template
```text
Act as a Principal Software Architect. Analyze the provided system architecture and generate a formal UML 2.5 Class Diagram in PlantUML.

Context / Codebase:
[Insert class definitions, models, or architectural requirements]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Modeling Elements:
   - Identify abstract and concrete classes. Label interfaces with «interface».
   - Include attributes with visibility modifiers (- private, # protected, + public) and explicit types.
   - Include operations with parameter lists and return types. Omit trivial getters and setters.
3. Relationship Semantics:
   - Generalization / Inheritance: <|--
   - Realization / Interface Implementation: <|..
   - Composition (strict lifecycle ownership): *--
   - Aggregation (independent lifecycle): o--
   - Association: --> with explicit multiplicities on both ends (e.g., "1" -- "0..*").
4. Styling:
   - Set 'skinparam classAttributeIconSize 0' and 'skinparam shadowing false'.
   - Apply a professional monochrome or slate palette.
```

---

## 2. Component Diagram

### Engineering Purpose
Illustrates the modular decomposition of a software system. It highlights autonomous software components, provided interfaces (APIs offered), required interfaces (dependencies needed), internal subcomponents, and network ports.

### When to Select
- Architecting microservices and modular monoliths.
- Specifying API contracts and shared component libraries.
- Defining dependency boundaries between subsystems.

### AI Prompt Template
```text
Act as a Solutions Architect. Generate a UML 2.5 Component Diagram in PlantUML modeling the modular structure of the target system.

Context / Codebase:
[Insert system components, package definitions, or microservices]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Structure:
   - Define major functional subsystems using [component] syntax.
   - Use provided interface lollipop notation ()- and required interface socket notation -( to represent service contracts.
   - Specify communication ports and protocols (REST/JSON, gRPC, AMQP, GraphQL).
3. Relationships:
   - Connect required interfaces to provided interfaces using dependency arrows (..>).
   - Group internal components into bounded subsystems.
4. Styling:
   - Disable drop shadows ('skinparam shadowing false').
   - Use clean rectangular borders with distinct interface pins.
```

---

## 3. Composite Structure Diagram

### Engineering Purpose
Details the internal collaboration of an individual classifier (such as a complex service or subsystem). It exposes internal parts, ports, execution roles, and connector channels without exposing external implementation details.

### When to Select
- Modeling the internal wiring of an event-driven microservice.
- Documenting complex design patterns (e.g., Mediator, Observer, Pipeline).
- Visualizing port-and-adapter (Hexagonal / Clean) architectures.

### AI Prompt Template
```text
Act as a Software Systems Engineer. Generate a UML 2.5 Composite Structure Diagram in PlantUML illustrating the internal structure of [Classifier/Service Name].

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Structure:
   - Encapsulate the primary classifier within a class or component frame.
   - Model external interaction entry points as typed ports (port [PortName]).
   - Define internal parts with role names and multiplicities (part : ClassifierType [multiplicity]).
   - Model internal connectors binding internal parts to ingress/egress ports.
3. Enforce strict black-box encapsulation with labeled message delegations.
```

---

## 4. Deployment Diagram

### Engineering Purpose
Models the physical and virtual hardware environment where software artifacts are deployed and executed. Specifies nodes (servers, VMs, containers, edge devices), artifacts (binaries, packages, container images), storage tiers, and network transmission protocols.

### When to Select
- Documenting cloud infrastructure topologies (AWS, Azure, GCP, Kubernetes).
- Specifying network security perimeters, reverse proxies, and DMZ boundaries.
- Verifying high-availability, replication topologies, and disaster recovery architectures.

### AI Prompt Template
```text
Act as a Cloud Infrastructure Architect. Generate a UML 2.5 Deployment Diagram in PlantUML for the system architecture.

Context / Infrastructure:
[Insert Dockerfiles, Kubernetes manifests, Terraform specs, or architecture text]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Infrastructure Tiers:
   - Client Tier: End-user workstations, mobile devices, hardware controllers.
   - Edge Tier: Reverse proxies, load balancers, CDN/WAF appliances.
   - Compute Tier: Containerized execution environments (e.g., Kubernetes pods, microservice nodes).
   - Persistence Tier: Primary relational databases, read replicas, distributed caches, object storage.
   - External SaaS Tier: Third-party payment gateways, identity providers, notification services.
3. Execution Manifests:
   - Place execution artifacts within their hosting nodes using artifact syntax.
   - Label communication channels with transport protocols and port numbers (e.g., HTTPS:443, gRPC:50051, JDBC:5432).
4. Styling:
   - Set 'skinparam shadowing false', round corners, and clean typography.
```

---

## 5. Object Diagram

### Engineering Purpose
Depicts a point-in-time snapshot of instantiated objects, their runtime attribute values, and link instances. Unlike class diagrams which represent abstractions, object diagrams represent concrete runtime state.

### When to Select
- Verifying complex object graphs and memory allocations during runtime.
- Debugging specific corner cases or edge-case execution snapshots.
- Explaining design pattern state changes before and after an operation.

### AI Prompt Template
```text
Act as a Software Architect. Generate a UML 2.5 Object Diagram in PlantUML illustrating a concrete runtime execution state for [System/Workflow Name].

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Structure:
   - Model objects using 'object "instanceName : ClassName" as alias' syntax.
   - Populated internal state: list key attributes with their concrete runtime values (e.g., status = "PENDING_APPROVAL", retryCount = 3).
   - Model links between instantiated objects representing active pointer references or associations.
3. Focus on a specific business scenario (e.g., an order currently undergoing payment validation).
```

---

## 6. Package Diagram

### Engineering Purpose
Organizes model elements, source code packages, modules, or namespaces into hierarchical namespaces. It defines compile-time dependencies, import relationships, and package access levels.

### When to Select
- Enforcing architectural layering (e.g., Presentation -> Application -> Domain -> Infrastructure).
- Detecting circular package dependencies in large-scale codebases.
- Structuring multi-project monorepos or microservice boundaries.

### AI Prompt Template
```text
Act as an Architectural Auditor. Generate a UML 2.5 Package Diagram in PlantUML analyzing the module organization of the target codebase.

Context / Codebase:
[Insert directory structure, namespace imports, or build configuration]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Structure:
   - Group related components into packages using 'package "PackageName" { ... }'.
   - Model package dependencies using dashed arrows with stereotypes (..> : «import», «access», «use»).
   - Enforce architectural layers: prevent illegal upward dependencies from Domain to Presentation.
3. Highlight any architectural boundary violations or cyclic dependencies if discovered.
```

---

## 7. Profile Diagram

### Engineering Purpose
A metamodel diagram that defines custom stereotypes, tagged values, and constraints to tailor the Unified Modeling Language (UML) to specialized domains or programming platforms.

### When to Select
- Customizing UML for specific frameworks (e.g., Spring Boot, Angular, Django).
- Modeling domain-specific requirements (e.g., Safety-Critical Automotive, Aerospace, Healthcare FHIR).
- Defining platform-specific architectural modeling rules.

### AI Prompt Template
```text
Act as a Metamodel Architect. Generate a UML 2.5 Profile Diagram in PlantUML tailoring UML for [Domain or Framework, e.g., Spring Boot Microservices / Cloud-Native Applications].

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Metamodel Elements:
   - Model standard UML metaclasses (Class, Property, Operation, Component).
   - Define custom stereotypes using 'class StereotypeName <<stereotype>>'.
   - Connect stereotypes to metaclasses using extension arrows (<|-- or «extend»).
   - Add tagged values (attributes) defining metadata properties required by the framework.
```
