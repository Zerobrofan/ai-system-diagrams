# Approach 3: Editorial System Diagrams with `diagram-design`

[`cathrynlavery/diagram-design`](https://github.com/cathrynlavery/diagram-design) is an open-source framework and AI agent skill engineered specifically for AI coding assistants (Claude Code, GitHub Copilot, Codex, Cursor, Gemini). 

Its explicit mission is to combat **"Mermaid slop"** — the generic, unstyled, auto-laid-out boxes and tangled lines typical of default AI diagram generators — by producing **publication-ready, editorial-grade HTML + SVG diagrams**.

---

## 1. Diagrams in this Directory

| Diagram | Source File | Rendered Output | Key Editorial Characteristics |
|---|---|---|---|
| **Use Case Diagram** | [`use-case.html`](use-case.html) | [`output/use-case.svg`](output/use-case.svg) | Dedicated system boundary, primary/secondary actor classification, masked «include» / «extend» labels, zero line intersections |
| **Class Diagram** | [`class-diagram.html`](class-diagram.html) | [`output/class-diagram.svg`](output/class-diagram.svg) | Adheres strictly to `type-uml-class.md`: 3-compartment classes, precise marker vocabulary (hollow/filled diamonds, inheritance triangles), multiplicities, focal class accent tint |
| **Deployment Diagram** | [`deployment-diagram.html`](deployment-diagram.html) | [`output/deployment-diagram.svg`](output/deployment-diagram.svg) | Multi-zone infrastructure: Client Tier, Cloudflare WAF Edge, Kubernetes Microservices, Private VPC Data Tier, and External SaaS, with rounded elbow connectors and protocol badges |

---

## 2. Design Principles & Anti-Slop Rules

`diagram-design` enforces rigorous typography, palette, and geometric rules:

1. **Hairline Precision**: 
   - Strict `1px` (or `0.8px` / `1.2px`) stroke weights. 
   - Absolutely **no drop shadows**, heavy gradients, or cartoonish borders.
2. **Editorial Typography**:
   - Headers: `Instrument Serif` (editorial gravitas).
   - Metadata & Labels: `Geist Mono` (precise tracking & technical clarity).
   - Body & Class Members: `Geist` (clean grotesque sans).
3. **Muted Color Discipline**:
   - `paper`: `#f5f5f5` (warm background).
   - `ink`: `#2d3142` (deep charcoal text & borders).
   - `muted`: `#4f5d75` (secondary lines & annotations).
   - `accent`: `#bf4520` (warm coral, reserved strictly for 1–2 focal elements per diagram).
   - `link`: `#2e5aa8` (network / transport protocols).
4. **Orthogonal Routing with Masks**:
   - Connectors never slice through node text. Connectors pass behind boxes, and all text labels sit on opaque background masks.
   - All 90-degree turns use rounded elbows (`rx=8` or `Q` bezier points).

---

## 3. How to View & Export

### Viewing:
Double-click any `.html` file (`use-case.html`, `class-diagram.html`, `deployment-diagram.html`) to open directly in any browser. They are 100% self-contained with no server required.

### Exporting to Vector SVG:
Run our Python script:

```bash
python diagram-design/render.py
```

This invokes the framework's `export_svg.py` extractor and outputs standalone `.svg` files into `output/`.

---

## 4. How to Prompt AI Agents for `diagram-design`

To prompt an AI model to generate `diagram-design` output:

### System Prompt Directive:
> *"You are an editorial information designer. Do not generate Mermaid or PlantUML. Generate a standalone, self-contained HTML file containing an inline SVG diagram. Enforce 1px hairline strokes, the 'Geist' and 'Instrument Serif' typography, a paper (#f5f5f5) and ink (#2d3142) palette with coral (#bf4520) accent. Mask connector labels with opaque rectangles, use rounded orthogonal elbows, and define markers in `<defs>`."*

### Key Prompt Constraints:
- `"Never pad class boxes to uniform heights; height must fit the content exactly."`
- `"Draw connector lines before boxes in DOM order so lines pass underneath node cards."`
- `"Include a relationship vocabulary legend in the corner."`

---

## 5. Strengths & Trade-Offs

### Strengths:
- **Publication Grade**: Looks like an illustration from a high-end technical whitepaper, textbook, or Stripe/Apple engineering blog.
- **Complete Visual Control**: Every coordinate, label, port, and line is pixel-positioned.
- **Zero Tooling Requirement**: Opens in any browser, embeds into any web page, renders crisp at 4K resolution.

### Limitations:
- **Authoring Verbosity**: Generates 100–250 lines of HTML/SVG rather than 20 lines of DSL text.
- **Manual Spatial Layout**: The AI must compute SVG coordinate layouts (`x`, `y`, `width`, `height`) rather than relying on an auto-layout engine.
