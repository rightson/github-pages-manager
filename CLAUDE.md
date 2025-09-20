# Claude Code Information

## GitHub Pages Management System

### manage.py
Python-based management script for GitHub Pages operations with simplified command structure.

**Structure:**
- `manage.py` - Main launcher script
- `gh_page/` - GitHub Pages operations package
- `gh_page/alfolio.py` - Al-folio template implementation
- `gh_page/operations.py` - Common GitHub Pages operations
- `gh_page/config.py` - Configuration management

**Configuration:**
Settings are loaded from `.env` file (copy from `.env.example`):
- `GITHUB_USERNAME` - GitHub username
- `GITHUB_PAGES_REPO` - Repository name
- `GITHUB_PAGES_URL` - Site URL
- `GIT_REMOTE` - Git remote URL
- `AUTHOR_NAME` - Author name for content
- `DEFAULT_BRANCH` - Default git branch
- `DEFAULT_TARGET_DIR` - Default target directory
- `DEFAULT_TEMPLATE` - Default template (e.g., alfolio)

**Dependencies:**
- python3 (required)
- python-dotenv (for .env support)
- PyYAML (for config operations)
- git (required)
- bundle (optional, for Jekyll)

**Usage:**
```bash
# Initialize template (uses DEFAULT_TEMPLATE from .env)
./manage.py init [options]

# Review and manage site
./manage.py review-config
./manage.py review-content

# Update site configuration (_config.yml)
./manage.py update-metadata first_name=John last_name=Doe email=john@example.com

# Update social media links (_data/socials.yml)
./manage.py update-socials github_username=rightson x_username=myhandle linkedin_username=john-doe email=john@example.com

# Commit and push changes
./manage.py push

Options for init:
  --dir PATH       Destination directory
  --remote URL     Git remote URL
  --branch NAME    Default branch name
  --bundle         Run bundle install after setup

Social media keys supported:
  github_username, x_username, linkedin_username, email, instagram_id,
  facebook_id, scholar_userid, orcid_id, medium_username, and more.
  Use 'none' or 'null' to remove a social link.
```

**Extensibility:**
- Add new templates in `gh_page/` package
- Configure different templates via `DEFAULT_TEMPLATE` in `.env`
- Reusable operations in `gh_page/operations.py`