#!/usr/bin/env python3
"""Management script for productivity boost operations."""

import sys
import importlib
from pathlib import Path

# Add current directory to Python path for local imports
sys.path.insert(0, str(Path(__file__).parent))


def show_usage():
    print("Usage: manage.py <action> [options]\n")
    print("Examples:")
    print("  manage.py init [--dir PATH] [--remote URL] [--branch NAME] [--bundle]")
    print("  manage.py review-config")
    print("  manage.py review-content")
    print("  manage.py update-metadata key=value [key2=value2 ...]")
    print("  manage.py update-socials github_username=rightson x_username=myhandle")
    print("  manage.py push")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        show_usage()
        return

    action = sys.argv[1]
    args = sys.argv[2:]

    # Import operations module for non-init actions
    from gh_page import operations
    from gh_page.config import Config

    # Use configured template and directory
    target = Config.DEFAULT_TEMPLATE
    target_dir = Config.DEFAULT_TARGET_DIR

    try:
        if action == "init":
            module = importlib.import_module(f"gh_page.{target}")
            module.main(args)
        elif action == "review-config":
            operations.review_config(target_dir)
        elif action == "review-content":
            operations.review_content_pages(target_dir)
        elif action == "update-metadata":
            # Parse key=value pairs for _config.yml
            kwargs = {}
            for arg in args:
                if "=" in arg:
                    key, value = arg.split("=", 1)
                    # Convert string "true"/"false" to boolean
                    if value.lower() == "true":
                        value = True
                    elif value.lower() == "false":
                        value = False
                    kwargs[key] = value
            if kwargs:
                operations.update_site_metadata(target_dir, **kwargs)
                print(f"Updated {len(kwargs)} setting(s) in _config.yml")
            else:
                print("No key=value pairs provided. Example: first_name=John last_name=Doe")
        elif action == "update-socials":
            # Parse key=value pairs for social media
            kwargs = {}
            for arg in args:
                if "=" in arg:
                    key, value = arg.split("=", 1)
                    kwargs[key] = value
            if kwargs:
                operations.update_socials(target_dir, **kwargs)
                print(f"Updated {len(kwargs)} social setting(s)")
            else:
                print("No key=value pairs provided.")
                print("Example: github_username=rightson x_username=myhandle email=me@example.com")
                print("Available keys: github_username, x_username, linkedin_username, email, etc.")
        elif action == "push":
            operations.git_push(target_dir)
        else:
            print(f"Unknown action: {action}")
            show_usage()
            sys.exit(1)
    except ImportError:
        print(f"Error: template '{target}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()