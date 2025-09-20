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


def git_push(target_dir, branch="main"):
    """Push repository to remote origin."""
    target_path = Path(target_dir)

    try:
        subprocess.run(["git", "push", "-u", "origin", branch],
                      cwd=target_path, check=True)
        print(f"Successfully pushed to origin/{branch}")
    except subprocess.CalledProcessError:
        print("Failed to push. Make sure remote is configured correctly.")


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