#!/usr/bin/env python3
"""Google Stitch CLI — generate UIs, fetch code/images, call Stitch tools.

Usage:
  python3 google_stitch.py tools                          # List available tools
  python3 google_stitch.py call <tool> key=value ...      # Call any tool
  python3 google_stitch.py build <project-id>             # Build site from project
  python3 google_stitch.py code <project-id> <screen-id>  # Get screen HTML
  python3 google_stitch.py image <project-id> <screen-id> # Get screen screenshot

Auth: STITCH_API_KEY env var / ~/.config/stitch/api-key file, OR gcloud ADC.
API docs: https://stitch.withgoogle.com/docs/mcp/setup
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

STITCH_URL = "https://stitch.googleapis.com/mcp"
TIMEOUT = 180  # Generation can be slow


def get_api_key():
    """Get Stitch API key from env var or config file. Returns None if not found."""
    key = os.environ.get("STITCH_API_KEY")
    if key:
        return key

    key_file = os.path.expanduser("~/.config/stitch/api-key")
    if os.path.exists(key_file):
        with open(key_file) as f:
            return f.read().strip()

    return None


def find_gcloud():
    """Find gcloud binary, checking common install locations."""
    import shutil
    gcloud = shutil.which("gcloud")
    if gcloud:
        return gcloud
    for path in [
        os.path.expanduser("~/google-cloud-sdk/bin/gcloud"),
        "/usr/lib/google-cloud-sdk/bin/gcloud",
        "/snap/google-cloud-sdk/current/bin/gcloud",
    ]:
        if os.path.isfile(path):
            return path
    return None


def get_gcloud_token():
    """Get access token from gcloud ADC. Returns None on failure."""
    gcloud = find_gcloud()
    if not gcloud:
        return None
    try:
        result = subprocess.run(
            [gcloud, "auth", "application-default", "print-access-token"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except FileNotFoundError:
        pass
    except subprocess.TimeoutExpired:
        pass
    return None


def get_project_id():
    """Get Google Cloud project ID from env or gcloud config."""
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if project:
        return project

    gcloud = find_gcloud()
    if not gcloud:
        return None
    try:
        result = subprocess.run(
            [gcloud, "config", "get-value", "project"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    return None


def build_headers(require_auth=True):
    """Build request headers with auth. API key preferred, gcloud ADC fallback."""
    headers = {"Content-Type": "application/json"}

    api_key = get_api_key()
    if api_key:
        headers["x-goog-api-key"] = api_key
        project = get_project_id()
        if project:
            headers["X-Goog-User-Project"] = project
        return headers

    if not require_auth:
        return headers

    token = get_gcloud_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
        project = get_project_id()
        if project:
            headers["X-Goog-User-Project"] = project
        return headers

    print("Error: No auth configured.", file=sys.stderr)
    print("Option A: Set STITCH_API_KEY env var or create ~/.config/stitch/api-key", file=sys.stderr)
    print("Option B: Run 'gcloud auth application-default login'", file=sys.stderr)
    sys.exit(1)


def jsonrpc(method, params=None, require_auth=True):
    """Send JSON-RPC 2.0 request to Stitch API."""
    headers = build_headers(require_auth=require_auth)
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": 1,
    }
    if params:
        payload["params"] = params

    body = json.dumps(payload).encode()
    req = urllib.request.Request(STITCH_URL, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"API Error {e.code}: {error_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    if "error" in data:
        err = data["error"]
        print(f"RPC Error {err.get('code', '?')}: {err.get('message', 'Unknown')}", file=sys.stderr)
        sys.exit(1)

    return data.get("result", data)


# ---- Subcommands ----

def cmd_tools(args):
    """List available Stitch tools."""
    result = jsonrpc("tools/list", require_auth=False)
    tools = result.get("tools", [])
    if not tools:
        print("No tools returned.")
        return

    print(f"\nStitch tools ({len(tools)}):\n")
    for tool in tools:
        name = tool.get("name", "?")
        desc = tool.get("description", "No description")
        print(f"  {name}")
        print(f"    {desc}")
        schema = tool.get("inputSchema", {})
        props = schema.get("properties", {})
        if props:
            required = set(schema.get("required", []))
            for pname, pinfo in props.items():
                req_mark = " (required)" if pname in required else ""
                ptype = pinfo.get("type", "?")
                pdesc = pinfo.get("description", "")
                print(f"      --{pname}: {ptype}{req_mark} {pdesc}")
        print()


def cmd_call(args):
    """Call any Stitch tool by name with key=value arguments."""
    tool_args = {}
    for kv in args.args:
        if "=" not in kv:
            print(f"Error: Argument '{kv}' must be key=value format", file=sys.stderr)
            sys.exit(1)
        k, v = kv.split("=", 1)
        # Try to parse as JSON for booleans/numbers/objects
        try:
            tool_args[k] = json.loads(v)
        except (json.JSONDecodeError, ValueError):
            tool_args[k] = v

    result = jsonrpc("tools/call", {
        "name": args.tool_name,
        "arguments": tool_args,
    })

    content = result.get("content", [])
    for item in content:
        if item.get("type") == "text":
            print(item.get("text", ""))
        elif item.get("type") == "image":
            # Save base64 image
            import base64
            data = base64.b64decode(item.get("data", ""))
            mime = item.get("mimeType", "image/png")
            ext = mime.split("/")[-1] if "/" in mime else "png"
            fname = f"/tmp/stitch-{args.tool_name}.{ext}"
            with open(fname, "wb") as f:
                f.write(data)
            print(f"Image saved: {fname}")
        else:
            print(json.dumps(item, indent=2))


def cmd_build(args):
    """Build site from a Stitch project."""
    result = jsonrpc("tools/call", {
        "name": "build_site",
        "arguments": {"projectId": args.project_id},
    })

    content = result.get("content", [])
    for item in content:
        if item.get("type") == "text":
            print(item.get("text", ""))
        else:
            print(json.dumps(item, indent=2))


def cmd_code(args):
    """Get screen HTML code."""
    result = jsonrpc("tools/call", {
        "name": "get_screen_code",
        "arguments": {
            "projectId": args.project_id,
            "screenId": args.screen_id,
        },
    })

    content = result.get("content", [])
    for item in content:
        if item.get("type") == "text":
            print(item.get("text", ""))
        else:
            print(json.dumps(item, indent=2))


def cmd_image(args):
    """Get screen screenshot."""
    import base64

    result = jsonrpc("tools/call", {
        "name": "get_screen_image",
        "arguments": {
            "projectId": args.project_id,
            "screenId": args.screen_id,
        },
    })

    content = result.get("content", [])
    for item in content:
        if item.get("type") == "image":
            data = base64.b64decode(item.get("data", ""))
            mime = item.get("mimeType", "image/png")
            ext = mime.split("/")[-1] if "/" in mime else "png"
            fname = f"/tmp/stitch-{args.screen_id}.{ext}"
            with open(fname, "wb") as f:
                f.write(data)
            print(f"Screenshot saved: {fname}")
        elif item.get("type") == "text":
            print(item.get("text", ""))
        else:
            print(json.dumps(item, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Google Stitch CLI — AI-powered UI design",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # tools
    subparsers.add_parser("tools", help="List available Stitch tools")

    # call
    call_parser = subparsers.add_parser("call", help="Call any Stitch tool")
    call_parser.add_argument("tool_name", help="Tool name (from 'tools' output)")
    call_parser.add_argument("args", nargs="*", help="key=value arguments")

    # build
    build_parser = subparsers.add_parser("build", help="Build site from project")
    build_parser.add_argument("project_id", help="Stitch project ID")

    # code
    code_parser = subparsers.add_parser("code", help="Get screen HTML code")
    code_parser.add_argument("project_id", help="Stitch project ID")
    code_parser.add_argument("screen_id", help="Screen ID")

    # image
    image_parser = subparsers.add_parser("image", help="Get screen screenshot")
    image_parser.add_argument("project_id", help="Stitch project ID")
    image_parser.add_argument("screen_id", help="Screen ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        "tools": cmd_tools,
        "call": cmd_call,
        "build": cmd_build,
        "code": cmd_code,
        "image": cmd_image,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
