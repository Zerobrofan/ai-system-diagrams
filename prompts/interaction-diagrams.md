# UML 2.5 Interaction Diagrams: Specifications and Prompt Templates

Interaction diagrams are an abstract subcategory of behaviour diagrams. They emphasize the dynamic exchange of messages, signals, and control transfers between collaborating object lifelines over time.

---

## Taxonomy of Interaction Diagrams

```
Interaction Diagram (Abstract Classification)
├── Sequence Diagram
├── Communication Diagram
├── Interaction Overview Diagram
└── Timing Diagram
```

---

## 1. Sequence Diagram

### Engineering Purpose
Models the chronological sequence of message invocations exchanged between object lifelines. Emphasizes time ordering, synchronous blocking calls, asynchronous dispatches, return responses, activation bars, and interaction frames (`alt`, `opt`, `loop`, `par`).

### When to Select
- Documenting API invocation chains across microservices.
- Visualizing complex protocol handshakes (OAuth2, mTLS, WebSocket negotiation).
- Debugging race conditions and transactional execution flows.

### AI Prompt Template
```text
Act as a Distributed Systems Architect. Generate a formal UML 2.5 Sequence Diagram in PlantUML for [Scenario Name].

Context / Interaction Flow:
[Insert API interaction, service orchestration, or method invocation sequence]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Lifeline Elements:
   - Define participants explicitly with appropriate stereotypes: 'actor User', 'participant "API Gateway" as GW', 'database "PostgreSQL" as DB'.
   - Use activation bars (activate / deactivate) to reflect processing execution lifetimes.
3. Message Semantics:
   - Synchronous blocking call: ->
   - Return message: -->
   - Asynchronous fire-and-forget message: ->>
4. Interaction Frames:
   - Alternative execution branches: alt condition ... else ... end
   - Optional conditional flows: opt condition ... end
   - Repeated processing: loop condition ... end
   - Concurrent parallel flows: par ... else ... end
5. Styling:
   - Auto-number messages using 'autonumber'.
   - Disable drop shadows and apply modern slate styling.
```

---

## 2. Communication Diagram (Collaboration)

### Engineering Purpose
Emphasizes the structural relationships and object topologies across which messages are transmitted, rather than the pure vertical timeline. Messages are attached directly to structural link lines and sequenced using hierarchical dot numbering (e.g., `1.1: request()`, `1.2: validate()`).

### When to Select
- Evaluating structural coupling between collaborating components.
- Illustrating the network or memory topology through which messages flow.
- Analyzing refactoring candidates where an object is overly coupled to too many communicators.

### AI Prompt Template
```text
Act as an Object-Oriented Architect. Generate a UML 2.5 Communication Diagram in PlantUML illustrating the collaboration topology for [Scenario Name].

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Structure:
   - Define collaborating objects or components as nodes.
   - Draw structural link lines connecting communicating pairs.
   - Add sequenced, numbered messages along link paths (e.g., "1: authenticate()", "1.1: lookupCredentials()", "2: issueToken()").
3. Ensure the message numbers clearly reflect the sequence and nesting of calls.
```

---

## 3. Interaction Overview Diagram

### Engineering Purpose
A hybrid architectural diagram combining activity diagram flow logic with nested interaction diagrams. It represents the high-level orchestration of multiple interaction fragments (such as complete sequence diagrams), organizing them with decision diamonds, merge nodes, forks, and joins.

### When to Select
- High-level business process visualization containing multiple subordinate sequence flows.
- Visualizing multi-stage enterprise checkout or onboarding pipelines.
- Providing an executive overview of distributed system interactions.

### AI Prompt Template
```text
Act as an Enterprise Integration Architect. Generate a UML 2.5 Interaction Overview Diagram in PlantUML modeling [Complex Process Name].

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Structure:
   - Use activity-like control nodes: initial node (*), decision diamonds, merge nodes, and final states.
   - Represent interaction occurrences (subordinate sequence flows) as framed interaction rectangles containing internal lifeline summaries.
   - Connect interaction occurrences with conditional guard transitions.
3. Emphasize the macro-level transition between different conversational phases of the system.
```

---

## 4. Timing Diagram

### Engineering Purpose
Focuses specifically on linear time constraints and the continuous state evolution of one or more classifiers along a calibrated horizontal time axis. It is the premier diagram for embedded systems, hardware drivers, and real-time network protocol analysis.

### When to Select
- Real-time and safety-critical systems with strict deadline requirements (e.g., medical devices, automotive telemetry).
- Specifying hardware interface bus timing (SPI, I2C, CAN bus).
- Verifying timeout, retry, and circuit-breaker thresholds in distributed systems.

### AI Prompt Template
```text
Act as a Real-Time Systems and Protocols Engineer. Generate a formal UML 2.5 Timing Diagram in PlantUML for [Protocol / Hardware Component].

Context / Timing Constraints:
[Insert protocol timing rules, clock pulses, state durations, or timeout thresholds]

Requirements:
1. Output valid PlantUML enclosed within @startuml and @enduml.
2. Structure:
   - Define horizontal time-based lifelines: 'robust "Component Name" as Comp'.
   - Define discrete states along the vertical scale of the lifeline (e.g., IDLE, LISTENING, TRANSMITTING, TIMEOUT).
   - Plot state transitions at exact time points (@0, @50, @120).
   - Annotate linear duration constraints and maximum latency windows using time markers (e.g., '{50 ms < time < 100 ms}').
3. Verify that all timeout states and clock transitions are mathematically consistent.
```
