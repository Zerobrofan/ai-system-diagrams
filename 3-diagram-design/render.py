#!/usr/bin/env python3
"""
diagram-design Export Script for Advanced Software Engineering Students.
Extracts clean, standalone SVGs from the editorial diagram-design HTML files
using the diagram-design export script.
"""

import sys
import subprocess
from pathlib import Path

def export_diagram(html_path: Path, output_dir: Path):
    export_script = Path(__file__).resolve().parent.parent / "diagram-design-framework" / "scripts" / "export_svg.py"
    if not export_script.exists():
        print(f"Error: export_svg.py not found at {export_script}")
        return False

    out_svg = output_dir / f"{html_path.stem}.svg"
    print(f"Exporting {html_path.name} -> {out_svg.name}...")

    cmd = [sys.executable, str(export_script), str(html_path), str(out_svg)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  Saved -> {out_svg} ({out_svg.stat().st_size} bytes)")
        return True
    else:
        print(f"  Error exporting {html_path.name}: {res.stderr}")
        return False

def main():
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    html_files = [
        base_dir / "use-case.html",
        base_dir / "class-diagram.html",
        base_dir / "deployment-diagram.html"
    ]

    print("Exporting diagram-design HTML diagrams to standalone SVGs...")
    for h in html_files:
        if h.exists():
            export_diagram(h, output_dir)
        else:
            print(f"Warning: file {h} does not exist.")

    print("\nAll diagram-design SVGs exported into:", output_dir)

if __name__ == "__main__":
    main()
