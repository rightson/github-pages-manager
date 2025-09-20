#!/usr/bin/env python3
"""Al-folio template initialization for GitHub Pages."""

import argparse
import subprocess
import tempfile
import shutil
import re
from pathlib import Path
from .config import Config


def setup_alfolio(target_dir=None, remote=None, branch=None, bundle=False):
    """Setup Al-folio template."""
    repo_url = "https://github.com/alshedivat/al-folio.git"

    # Use config defaults if not specified
    target_dir = target_dir or Config.DEFAULT_TARGET_DIR
    remote = remote or Config.GIT_REMOTE
    branch = branch or Config.DEFAULT_BRANCH

    target_path = Path(target_dir)

    # Check if target exists
    if target_path.exists():
        if target_path.is_dir() and not any(target_path.iterdir()):
            target_path.rmdir()
        else:
            raise FileExistsError(f"Destination '{target_dir}' already exists and is not empty")

    # Clone template
    with tempfile.TemporaryDirectory() as temp_dir:
        clone_dir = Path(temp_dir) / "al-folio"
        subprocess.run(["git", "clone", "--depth=1", repo_url, str(clone_dir)],
                      check=True, capture_output=True)

        # Move to target
        shutil.move(str(clone_dir), str(target_path))

    # Remove original git history
    shutil.rmtree(target_path / ".git")

    # Initialize new repo
    subprocess.run(["git", "init", "-b", branch], cwd=target_path, check=True, capture_output=True)

    # Configure for GitHub Pages
    config_file = target_path / "_config.yml"
    if config_file.exists():
        text = config_file.read_text()
        text = re.sub(r'^url:\s*.+$', f'url: {Config.GITHUB_PAGES_URL}', text, flags=re.MULTILINE)
        text = re.sub(r'^baseurl:\s*.+$', 'baseurl: ""', text, flags=re.MULTILINE)
        text = re.sub(r'^repository:\s*.+$', f'repository: {Config.get_repository_url()}', text, flags=re.MULTILINE)
        config_file.write_text(text)

    # Update about page
    about_file = target_path / "_pages" / "about.md"
    if about_file.exists():
        text = about_file.read_text()
        if 'Your Name' in text:
            about_file.write_text(text.replace('Your Name', Config.AUTHOR_NAME, 1))

    # Commit initial setup
    subprocess.run(["git", "add", "."], cwd=target_path, check=True)
    subprocess.run(["git", "commit", "-m", "Initialize site with Al-folio"],
                  cwd=target_path, check=True)
    subprocess.run(["git", "remote", "add", "origin", remote], cwd=target_path, check=True)

    print(f"Repository ready at '{target_dir}'.")
    print("Next steps:")
    print(f"  1. cd '{target_dir}'")
    print("  2. Review _config.yml and content pages")
    print("  3. Update site metadata and personal details")
    print(f"  4. git push -u origin {branch}")

    if bundle:
        try:
            subprocess.run(["bundle", "install"], cwd=target_path, check=True)
            print("Bundle install completed.")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Warning: bundle install failed")
    else:
        print(f"(Optional) Run 'bundle install' inside '{target_dir}' before building locally.")


def main(args):
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Initialize Al-folio template")
    parser.add_argument("--dir", default=Config.DEFAULT_TARGET_DIR, help="Target directory")
    parser.add_argument("--remote", help="Git remote URL")
    parser.add_argument("--branch", default=Config.DEFAULT_BRANCH, help="Branch name")
    parser.add_argument("--bundle", action="store_true", help="Run bundle install")

    parsed_args = parser.parse_args(args)

    try:
        setup_alfolio(parsed_args.dir, parsed_args.remote, parsed_args.branch, parsed_args.bundle)
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))