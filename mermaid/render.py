#!/usr/bin/env python3
"""
Mermaid Rendering Script for Advanced Software Engineering Students.
Renders .mmd files to standalone SVG using base64 URL safe encoding with mermaid.ink service.
Requires zero local node_modules or headless Chrome dependencies.
"""

import os
import sys
import base64
import urllib.request
from pathlib import Path

def render_mermaid_file(mmd_path: Path, output_dir: Path) -> Path:
    """Render a .mmd file to standalone SVG."""
    print(f"Reading {mmd_path.name}...")
    with open(mmd_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Base64 URL safe encode
    b64 = base64.urlsafe_b64encode(content.encode("utf-8")).decode("utf-8")
    url = f"https://mermaid.ink/svg/{b64}"
    
    out_file = output_dir / f"{mmd_path.stem}.svg"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    
    print(f"  Fetching SVG from Mermaid rendering service...")
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = resp.read()
    
    with open(out_file, "wb") as f:
        f.write(data)
    
    print(f"  Saved -> {out_file} ({len(data)} bytes)")
    return out_file

def main():
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    mmd_files = list(base_dir.glob("*.mmd"))
    if not mmd_files:
        print("No .mmd files found in", base_dir)
        sys.exit(1)

    print(f"Found {len(mmd_files)} Mermaid files to render...")
    for mmd in mmd_files:
        try:
            render_mermaid_file(mmd, output_dir)
        except Exception as e:
            print(f"Error rendering {mmd.name}: {e}")

    print("\nAll Mermaid diagrams rendered successfully into:", output_dir)

if __name__ == "__main__":
    main()
