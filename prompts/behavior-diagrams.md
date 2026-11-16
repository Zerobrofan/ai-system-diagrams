# UML 2.5 Behaviour Diagrams: Specifications and Prompt Templates

Behaviour diagrams model the dynamic aspects of a software system. They illustrate how system elements collaborate, change state, and execute workflows in response to external stimuli and internal triggers over time.

---

## Taxonomy of Behaviour Diagrams

```
Behaviour Diagram (Abstract Classification)
├── Use Case Diagram
├── Activity Diagram
├── State Machine Diagram
└── Interaction Diagram (Abstract Subcategory)
    ├── Sequence Diagram
    ├── Communication Diagram
    ├── Interaction Overview Diagram
    └── Timing Diagram
```

*(Note: Interaction diagrams are an abstract subcategory of behaviour diagrams and are documented in detail in `prompts/interaction-diagrams.md`).*

---

## 1. Use Case Diagram

### Engineering Purpose
Defines the functional requirements and system scope from the viewpoint of external actors. It captures system boundaries, actor interactions, mandatory inclusion workflows (`<<include>>`), and conditional extensions (`<<extend>>`).

### When to Select
- Requirements elicitation and functional scope definition.
- Identifying primary human actors and secondary external integrations.
- Structuring acceptance criteria and end-to-end integration test suites.

### AI Prompt Template
```text
Act as a Senior Software Systems Analyst. Analyze the provided requirements and generate a formal UML 2.5 Use Case Diagram in PlantUML.

Context / System Requirements:
[Insert system description, user stories, or feature requirements]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Structure:
   - Enforce 'left to right direction' for readability.
   - Define a clear system boundary using 'rectangle "System Name" { ... }'.
   - Place primary human actors on the left and secondary systems / services on the right.
   - Model all use cases inside the system boundary.
3. Relationships:
   - Mandatory Sub-routines: Model required shared flows using dashed arrows labeled '..> ... : <<include>>'.
   - Conditional Flows: Model optional branches using dashed arrows labeled '..> ... : <<extend>>'.
   - Actor Generalization: If specific user types share base privileges, model actor inheritance using '<|--'.
4. Styling:
   - Set 'skinparam shadowing false', rounded corners, and a clean slate palette.
```

---

## 2. Activity Diagram

### Engineering Purpose
Models procedural control flow and object flow through a sequence of activities. It visualizes decision branches, concurrent execution paths (forks and joins), swimlanes (partition of responsibility), and object token transformations.

### When to Select
- Documenting complex business logic, transactional sagas, and checkout workflows.
- Visualizing asynchronous parallel processing pipelines.
- Mapping cross-departmental operations using organizational swimlanes.

### AI Prompt Template
```text
Act as a Business Process and Systems Architect. Generate a formal UML 2.5 Activity Diagram in PlantUML for [Workflow Name].

Context / Process Description:
[Insert algorithm, workflow description, or transaction sequence]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Control Flow Elements:
   - Initial node (*) and final node (stop / end).
   - Action states describing discrete tasks using :Action Description;.
   - Decision and merge diamonds using 'if (condition?) then (yes) ... else (no) ... endif'.
   - Concurrency: Model parallel forks and joins using 'fork ... fork again ... end fork'.
3. Organizational Partitioning:
   - Group actions into explicit swimlanes using '|Actor or Subsystem Name|'.
4. Styling:
   - Disable drop shadows, configure distinct branch labels, and maintain clean vertical alignment.
```

---

## 3. State Machine Diagram

### Engineering Purpose
Specifies the discrete event-driven lifecycle of a state-dependent entity. It models states, state transitions, event triggers, guard conditions `[condition]`, and associated actions (`entry /`, `exit /`, `do /`).

### When to Select
- Modeling entity lifecycles (e.g., Order, Ticket, IoT Sensor, Session, Document Review).
- Implementing the State or Strategy design pattern in code.
- Verifying safety-critical state machines to eliminate deadlocks or unreachable states.

### AI Prompt Template
```text
Act as a State Machine and Verification Engineer. Generate a UML 2.5 State Machine Diagram in PlantUML modeling the lifecycle of [Entity Name].

Context / State Specifications:
[Insert entity lifecycle, event triggers, or business rules]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. State Machine Elements:
   - Initial state ([*]) and terminal states.
   - Distinct named states with internal actions where applicable (entry / action, do / activity, exit / action).
   - Transitions with formal notation: 'SourceState --> TargetState : Event [GuardCondition] / EffectAction'.
   - Composite States: Nest sub-states within parent states where hierarchical states exist.
   - Choice Pseudostates: Use '<<choice>>' diamonds for dynamic conditional state branching.
3. Invariants:
   - Ensure every state has at least one valid egress path unless it is a terminal state.
   - Maintain deterministic, non-ambiguous guard conditions.
```
