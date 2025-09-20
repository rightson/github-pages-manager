"""GitHub Pages specific operations."""

import subprocess
import yaml
from pathlib import Path


def review_config(target_dir):
    """Review and optionally edit _config.yml."""
    target_path = Path(target_dir)
    config_file = target_path / "_config.yml"

    if not config_file.exists():
        print("No _config.yml found")
        return

    print(f"Config file: {config_file}")
    with open(config_file) as f:
        config = yaml.safe_load(f)

    print("Key settings:")
    for key in ['title', 'email', 'description', 'url', 'baseurl']:
        if key in config:
            print(f"  {key}: {config[key]}")


def review_content_pages(target_dir):
    """List and review content pages."""
    target_path = Path(target_dir)

    content_dirs = ['_pages', '_posts', '_projects']
    for dir_name in content_dirs:
        content_dir = target_path / dir_name
        if content_dir.exists():
            files = list(content_dir.glob('*.md'))
            if files:
                print(f"\n{dir_name}:")
                for file in files:
                    print(f"  {file.name}")


def update_site_metadata(target_dir, **kwargs):
    """Update site metadata in _config.yml."""
    target_path = Path(target_dir)
    config_file = target_path / "_config.yml"

    if not config_file.exists():
        print("No _config.yml found")
        return

    with open(config_file) as f:
        config = yaml.safe_load(f)

    config.update(kwargs)

    with open(config_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

    print(f"Updated {len(kwargs)} settings in _config.yml")


def update_socials(target_dir, **kwargs):
    """Update social media settings in _data/socials.yml."""
    target_path = Path(target_dir)
    socials_file = target_path / "_data" / "socials.yml"

    if not socials_file.exists():
        print(f"No socials.yml found at {socials_file}")
        return

    with open(socials_file) as f:
        socials = yaml.safe_load(f) or {}

    # Update social media settings
    for key, value in kwargs.items():
        if value.lower() in ('none', 'null', ''):
            # Remove the key if set to none/null/empty
            socials.pop(key, None)
        else:
            socials[key] = value

    with open(socials_file, 'w') as f:
        yaml.dump(socials, f, default_flow_style=False, allow_unicode=True)

    print(f"Updated socials.yml with {len(kwargs)} setting(s)")

    # Show what was updated
    for key, value in kwargs.items():
        if value.lower() in ('none', 'null', ''):
            print(f"  Removed: {key}")
        else:
            print(f"  Set {key}: {value}")


def git_push(target_dir, branch="main"):
    """Push repository to remote origin."""
    target_path = Path(target_dir)

    if not target_path.exists():
        print(f"Target directory '{target_dir}' does not exist")
        return

    try:
        # Add all changes first
        subprocess.run(["git", "add", "."], cwd=target_path, check=True)

        # Check if there are changes to commit
        result = subprocess.run(["git", "status", "--porcelain"],
                              cwd=target_path, capture_output=True, text=True)

        if result.stdout.strip():
            # There are changes, commit them
            subprocess.run(["git", "commit", "-m", "Update site content"],
                          cwd=target_path, check=True)
            print("Committed changes")
        else:
            print("No changes to commit")

        # Push to remote
        subprocess.run(["git", "push", "-u", "origin", branch],
                      cwd=target_path, check=True)
        print(f"Successfully pushed to origin/{branch}")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")
        print("Make sure:")
        print("  1. Remote origin is configured")
        print("  2. You have push permissions")
        print("  3. Branch exists on remote")


def setup_git_repo(target_path, branch="main", remote=None, commit_msg="Initial commit"):
    """Initialize git repository with standard setup."""
    target_path = Path(target_path)

    subprocess.run(["git", "init", "-b", branch], cwd=target_path, check=True, capture_output=True)
    subprocess.run(["git", "add", "."], cwd=target_path, check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=target_path, check=True)

    if remote:
        subprocess.run(["git", "remote", "add", "origin", remote], cwd=target_path, check=True)


def install_dependencies(target_path, bundle=False):
    """Install dependencies with optional feedback."""
    target_path = Path(target_path)

    if bundle:
        try:
            subprocess.run(["bundle", "install"], cwd=target_path, check=True)
            print("Bundle install completed.")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Warning: bundle install failed")
    else:
        print(f"(Optional) Run 'bundle install' inside '{target_path}' before building locally.")