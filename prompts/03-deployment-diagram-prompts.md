# AI Prompt Templates: Deployment Diagrams

Use these structured prompts when asking AI models to generate physical and infrastructure deployment diagrams.

---

## 1. PlantUML Prompt

```text
Act as a Cloud Infrastructure Architect. Create a multi-tier physical Deployment Diagram for [System Name] in PlantUML.

Requirements:
1. Output ONLY valid PlantUML enclosed within @startuml and @enduml.
2. Architecture Tiers to Model:
   - Client Tier: Browser, Mobile device, and IoT/Hardware nodes.
   - Edge Tier: Cloudflare / CDN / WAF node.
   - Compute / Kubernetes Cluster: Ingress controller node and at least 3 distinct microservice pod nodes.
   - Secure Data Tier: PostgreSQL Primary, Read Replica, Redis In-Memory Cache, and Object Storage (S3/MinIO).
   - External SaaS Tier: Payment gateway and third-party APIs.
3. Network Links & Protocols:
   - Label all communication links with network protocols and port numbers (e.g., 'HTTPS : 443', 'gRPC : 50051', 'JDBC / TLS : 5432', 'RESP : 6379').
4. Styling:
   - Differentiate node stereotypes: <<iOS / Android>>, <<Windows>>, <<Traefik>>, <<PCI-DSS>>.
   - Use clean modern skinparams with zero drop shadows.
```

---

## 2. Mermaid.js Prompt

```text
Act as a DevOps & Infrastructure Engineer. Generate a Mermaid.js Deployment topology for [System Name].

Requirements:
1. Output ONLY valid Mermaid syntax starting with 'flowchart TB'.
2. Structure:
   - Tier 1: subgraph "Client Devices Tier"
   - Tier 2: subgraph "Edge & DMZ (Cloudflare)"
   - Tier 3: subgraph "Kubernetes Production Cluster" with nested subgraph for Microservices.
   - Tier 4: subgraph "Private Data Subnet" using cylinder database shapes: NodeID[("Database Name")]
   - Tier 5: subgraph "External Cloud APIs"
3. Connections:
   - Label every arrow with transport protocol and port (e.g., -->|HTTPS / 443|, -->|gRPC : 50051|, -->|JDBC / TLS|).
   - Dotted arrows for asynchronous replication or read queries: -.->|Streaming WAL Replication|
4. Semantic Colors:
   - Define classDef styles for client (blue), edge (slate), k8s (emerald/green), data (amber), and external (purple).
```

---

## 3. diagram-design Prompt (Editorial HTML + SVG)

```text
Act as an editorial information designer adhering strictly to the 'type-deployment.md' diagram-design specification. Generate a standalone HTML file with inline SVG showing the production deployment architecture for [System Name].

Requirements:
1. Multi-Zone Geometry:
   - Place infrastructure across distinct dashed zone containers with mono uppercase tags: CLIENT TIER, EDGE / CLOUDFLARE, PROD K8S CLUSTER, DATA TIER / VPC, and EXTERNAL HEALTH APIS.
2. Node Cards:
   - Node cards must have 1px borders, rounded corners (rx=6), node title, tech stack description, and port badges.
   - High-availability nodes must include a small green status dot indicator.
3. Network Paths:
   - Draw connector paths BEHIND node boxes using orthogonal rounded elbows (rx=8).
   - Color code transport types: blue (#2e5aa8) for public HTTPS/mTLS, coral (#bf4520) for internal gRPC service mesh and DB replication, and slate (#4f5d75) for standard TCP.
   - Every connector must feature an opaque masked protocol badge (e.g. 'HTTPS:443', 'gRPC:50051', 'JDBC:5432').
4. Legend:
   - Include an infrastructure legend in the bottom corner.
```
