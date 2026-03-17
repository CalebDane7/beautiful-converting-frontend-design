#!/usr/bin/env python3
"""21st.dev Component Library CLI — fetch, refine, and pick UI components.

Usage:
  python3 twenty_first.py fetch "navigation bar"      # Search for components
  python3 twenty_first.py refine <id> "make it dark"   # Refine a component
  python3 twenty_first.py pick                          # Open browser picker

Requires: TWENTYFIRST_API_KEY env var or ~/.config/21st-dev/api-key file.
API docs: https://magic.21st.dev
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import urllib.parse
import http.server
import webbrowser
import threading

API_BASE = "https://magic.21st.dev/api"


def get_api_key():
    """Get API key from env var or config file."""
    key = os.environ.get("TWENTYFIRST_API_KEY")
    if key:
        return key

    key_file = os.path.expanduser("~/.config/21st-dev/api-key")
    if os.path.exists(key_file):
        with open(key_file) as f:
            return f.read().strip()

    print("Error: No API key found.", file=sys.stderr)
    print("Set TWENTYFIRST_API_KEY env var or create ~/.config/21st-dev/api-key", file=sys.stderr)
    sys.exit(1)


def api_request(endpoint, data=None, method="POST"):
    """Make API request to 21st.dev."""
    url = f"{API_BASE}/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_api_key()}"
    }

    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"API Error {e.code}: {error_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def cmd_fetch(args):
    """Search for UI components by description."""
    result = api_request("fetch-ui", {
        "query": args.query,
        "limit": args.limit
    })

    components = result.get("components", result.get("results", []))
    if not components:
        print("No components found for:", args.query)
        return

    print(f"\n Found {len(components)} component(s):\n")
    for i, comp in enumerate(components, 1):
        name = comp.get("name", "Unnamed")
        comp_id = comp.get("id", "?")
        desc = comp.get("description", "No description")
        print(f"  [{i}] {name} (id: {comp_id})")
        print(f"      {desc}")
        if comp.get("preview_url"):
            print(f"      Preview: {comp['preview_url']}")
        print()

    if components:
        first_id = components[0].get("id", "?")
        print(f"  Refine: python3 {__file__} refine {first_id} \"your changes\"")


def cmd_refine(args):
    """Refine an existing component with modifications."""
    result = api_request("refine-ui", {
        "component_id": args.component_id,
        "instructions": args.instructions
    })

    code = result.get("code", result.get("html", ""))
    if code:
        print(code)
    else:
        print(json.dumps(result, indent=2))


def cmd_pick(args):
    """Open browser picker to visually select a component."""
    received = threading.Event()
    component_data = {}

    class CallbackHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            component_data.update(json.loads(body))
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b'{"status": "received"}')
            received.set()

        def do_OPTIONS(self):
            self.send_response(204)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()

        def log_message(self, format, *args):
            pass  # Suppress logging

    port = args.port
    server = http.server.HTTPServer(("127.0.0.1", port), CallbackHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    picker_url = f"https://21st.dev/picker?callback=http://127.0.0.1:{port}"
    print(f"Opening browser picker...")
    print(f"Callback server on port {port}")
    webbrowser.open(picker_url)

    print("Waiting for component selection (Ctrl+C to cancel)...")
    try:
        received.wait(timeout=300)
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(0)
    finally:
        server.shutdown()

    if component_data:
        print("\nSelected component:")
        print(json.dumps(component_data, indent=2))
    else:
        print("No component received.")


def main():
    parser = argparse.ArgumentParser(
        description="21st.dev Component Library CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # fetch
    fetch_parser = subparsers.add_parser("fetch", help="Search for components")
    fetch_parser.add_argument("query", help="Component description (e.g., 'dark navigation bar')")
    fetch_parser.add_argument("--limit", type=int, default=5, help="Max results (default: 5)")
    fetch_parser.set_defaults(func=cmd_fetch)

    # refine
    refine_parser = subparsers.add_parser("refine", help="Refine a component")
    refine_parser.add_argument("component_id", help="Component ID from fetch results")
    refine_parser.add_argument("instructions", help="Modification instructions")
    refine_parser.set_defaults(func=cmd_refine)

    # pick
    pick_parser = subparsers.add_parser("pick", help="Open browser picker")
    pick_parser.add_argument("--port", type=int, default=9876, help="Callback port (default: 9876)")
    pick_parser.set_defaults(func=cmd_pick)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()
