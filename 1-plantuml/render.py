#!/usr/bin/env python3
"""
PlantUML Rendering Script for Advanced Software Engineering Students.
Renders .puml files to SVG using standard PlantUML Deflate-Base64 encoding.
Requires zero local Java/Graphviz installations.
"""

import os
import sys
import zlib
import base64
import string
import urllib.request
from pathlib import Path

# PlantUML custom alphabet mapping
PLANTUML_ALPHABET = string.digits + string.ascii_uppercase + string.ascii_lowercase + "-_"
BASE64_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
B64_TO_PLANTUML = bytes.maketrans(BASE64_ALPHABET.encode("utf-8"), PLANTUML_ALPHABET.encode("utf-8"))

def plantuml_encode(text: str) -> str:
    """
    Compresses text using Deflate (zlib without header/checksum)
    and encodes it into PlantUML's 64-character alphabet.
    Note: Do NOT add '~1' prefix, which indicates Huffman compression.
    """
    utf8_bytes = text.encode("utf-8")
    zlibbed = zlib.compress(utf8_bytes)
    # Strip 2-byte zlib header and 4-byte checksum trailer
    raw_deflate = zlibbed[2:-4]
    return base64.b64encode(raw_deflate).translate(B64_TO_PLANTUML).decode("utf-8")

def render_file(puml_path: Path, output_dir: Path, fmt: str = "svg") -> Path:
    """Render a single .puml file to SVG or PNG."""
    print(f"Reading {puml_path.name}...")
    with open(puml_path, "r", encoding="utf-8") as f:
        content = f.read()

    encoded = plantuml_encode(content)
    # Note: URL format is /plantuml/{fmt}/{encoded} (NO ~1 prefix)
    url = f"http://www.plantuml.com/plantuml/{fmt}/{encoded}"
    
    out_file = output_dir / f"{puml_path.stem}.{fmt}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    
    print(f"  Fetching {fmt.upper()} from PlantUML service...")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
    except Exception as e:
        print(f"  PlantUML server error, attempting Kroki fallback: {e}")
        kroki_b64 = base64.urlsafe_b64encode(zlib.compress(content.encode("utf-8"))).decode("utf-8")
        fallback_url = f"https://kroki.io/plantuml/{fmt}/{kroki_b64}"
        fallback_req = urllib.request.Request(fallback_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(fallback_req, timeout=15) as resp:
            data = resp.read()

    # Safety check: ensure response is not an error SVG
    text_sample = data[:400].decode("utf-8", errors="ignore")
    if "bad URL" in text_sample or "HUFFMAN" in text_sample:
        raise ValueError(f"PlantUML returned encoding error message: {text_sample}")

    with open(out_file, "wb") as f:
        f.write(data)
    
    print(f"  Saved -> {out_file.name} ({len(data)} bytes, valid diagram)")
    return out_file

def main():
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    puml_files = sorted(list(base_dir.glob("*.puml")))
    if not puml_files:
        print("No .puml files found in", base_dir)
        sys.exit(1)

    print(f"Found {len(puml_files)} PlantUML files to render...")
    for puml in puml_files:
        try:
            render_file(puml, output_dir, fmt="svg")
        except Exception as e:
            print(f"Error rendering {puml.name} to SVG: {e}")

    print("\nAll PlantUML diagrams rendered successfully into:", output_dir)

if __name__ == "__main__":
    main()
