"""Configuration management for GitHub Pages operations."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(Path(__file__).parent.parent / '.env')


class Config:
    """Configuration settings loaded from environment."""

    GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', 'rightson')
    GITHUB_PAGES_REPO = os.getenv('GITHUB_PAGES_REPO', 'rightson.github.io')
    GITHUB_PAGES_URL = os.getenv('GITHUB_PAGES_URL', 'https://rightson.github.io')
    GIT_REMOTE = os.getenv('GIT_REMOTE', 'git@github.com:rightson/rightson.github.io.git')

    AUTHOR_NAME = os.getenv('AUTHOR_NAME', 'Rightson')
    AUTHOR_EMAIL = os.getenv('AUTHOR_EMAIL', '')

    DEFAULT_BRANCH = os.getenv('DEFAULT_BRANCH', 'main')
    DEFAULT_TARGET_DIR = os.getenv('DEFAULT_TARGET_DIR', 'rightson.github.io')

    @classmethod
    def get_repository_url(cls):
        """Get the full repository URL."""
        return f"{cls.GITHUB_USERNAME}/{cls.GITHUB_PAGES_REPO}"