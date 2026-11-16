#!/usr/bin/env python3
"""
Simple HTTP Server for Advanced Software Engineering Students.
Launches a local web server to browse the interactive comparison dashboard (index.html),
inspect diagrams, and view source code side-by-side.
"""

import http.server
import socketserver
import webbrowser
import sys
from pathlib import Path

PORT = 8080

def main():
    root_dir = Path(__file__).resolve().parent.parent
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(root_dir), **kwargs)

    print(f"Starting MedPulse Diagram Showcase Server at http://localhost:{PORT}")
    print(f"Root Directory: {root_dir}")
    print("Press Ctrl+C to stop the server.")

    # Try port, increment if busy
    port = PORT
    server = None
    for attempt in range(5):
        try:
            server = socketserver.TCPServer(("", port), Handler)
            break
        except OSError:
            print(f"Port {port} is in use, trying {port + 1}...")
            port += 1

    if not server:
        print("Error: Could not bind to any port.")
        sys.exit(1)

    url = f"http://localhost:{port}/index.html"
    print(f"Server ready! Open your browser to: {url}")
    
    # Open browser automatically if run directly
    try:
        webbrowser.open(url)
    except Exception:
        pass

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server. Goodbye!")
        server.server_close()

if __name__ == "__main__":
    main()
