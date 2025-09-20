#!/usr/bin/env python3
"""Management script for productivity boost operations."""

import sys
import importlib
from pathlib import Path

# Add current directory to Python path for local imports
sys.path.insert(0, str(Path(__file__).parent))


def show_usage():
    print("Usage: manage.py <service> <action> <target> [options]\n")
    print("Examples:")
    print("  manage.py gh-page init alfolio")
    print("  manage.py gh-page review-config alfolio")
    print("  manage.py gh-page review-content alfolio")
    print("  manage.py gh-page update-metadata alfolio")
    print("  manage.py gh-page push alfolio")


def main():
    if len(sys.argv) < 4 or sys.argv[1] in ("-h", "--help", "help"):
        show_usage()
        return

    service, action, target = sys.argv[1:4]
    args = sys.argv[4:]

    if service == "gh-page" and action == "init":
        try:
            module = importlib.import_module(f"gh_page.{target}")
            module.main(args)
        except ImportError:
            print(f"Error: template '{target}' not found")
            sys.exit(1)
    else:
        print(f"Unknown command: {service} {action} {target}")
        show_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()