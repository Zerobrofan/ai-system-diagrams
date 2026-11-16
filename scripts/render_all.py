#!/usr/bin/env python3
"""
Master Build Script: Render All System Diagrams
Invokes rendering engines for:
1. PlantUML (HTTP deflate encoder -> SVG)
2. Mermaid.js (mermaid.ink API -> SVG)
3. diagram-design (export_svg.py extractor -> SVG)
"""

import os
import sys
import subprocess
from pathlib import Path

def run_script(script_path: Path, label: str):
    print(f"\n=======================================================")
    print(f"  RENDERING APPROACH: {label.upper()}")
    print(f"  Script: {script_path.relative_to(script_path.parent.parent)}")
    print(f"=======================================================")
    
    cmd = [sys.executable, str(script_path)]
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print(f"Warning: Script {script_path.name} finished with return code {res.returncode}")
    return res.returncode == 0

def main():
    root = Path(__file__).resolve().parent.parent

    scripts = [
        (root / "1-plantuml" / "render.py", "1. PlantUML (Generated with AI)"),
        (root / "2-mermaid" / "render.py", "2. Mermaid.js (Generated with AI)"),
        (root / "3-diagram-design" / "render.py", "3. diagram-design Framework"),
    ]

    success_count = 0
    for s_path, label in scripts:
        if s_path.exists():
            if run_script(s_path, label):
                success_count += 1
        else:
            print(f"Script not found: {s_path}")

    print("\n" + "="*55)
    print(f"  RENDER SUMMARY: {success_count}/{len(scripts)} approaches rendered successfully.")
    print("="*55)
    print("\nRendered SVG outputs are available in:")
    print(" - 1-plantuml/output/")
    print(" - 2-mermaid/output/")
    print(" - 3-diagram-design/output/")
    print("\nTo explore the interactive comparison showcase, open index.html or run:")
    print("  python scripts/serve.py\n")

if __name__ == "__main__":
    main()
