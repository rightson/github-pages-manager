# Productivity Boost

Bootstrap your GitHub Pages site in minutes! This tool helps you set up professional academic portfolios and other Jekyll-based sites with zero configuration hassle.

## 🚀 Quick Start - Get Your Site Running

### Step 1: Clone This Repository
```bash
git clone https://github.com/rightson/productivity-boost.git
cd productivity-boost
```

### Step 2: Configure Your Settings
```bash
# Copy the template
cp .env.example .env

# Edit with your information
nano .env  # or use your favorite editor
```

**Required settings in `.env`:**
```bash
GITHUB_USERNAME=yourusername          # Your GitHub username
GITHUB_PAGES_REPO=yourusername.github.io  # Your repo name
GITHUB_PAGES_URL=https://yourusername.github.io
GIT_REMOTE=git@github.com:yourusername/yourusername.github.io.git
AUTHOR_NAME=Your Full Name
```

### Step 3: Install Dependencies
```bash
pip install python-dotenv PyYAML
```

### Step 4: Create Your GitHub Repository
1. Go to GitHub and create a new repository named `yourusername.github.io`
2. Don't initialize with README (we'll create everything)

### Step 5: Bootstrap Your Site
```bash
# Creates a complete Al-folio academic portfolio
./manage.py gh-page init alfolio --bundle

# Follow the output instructions to push to GitHub
cd yourusername.github.io
git push -u origin main
```

### Step 6: Success! 🎉
Your site will be live at `https://yourusername.github.io` within minutes!

## 📋 What You Get

### Al-folio Academic Portfolio
- **Beautiful Design**: Clean, professional academic portfolio
- **Publications**: BibTeX integration for your papers
- **Projects**: Showcase your research and code
- **Blog**: Built-in Jekyll blog functionality
- **Responsive**: Mobile-friendly design
- **Customizable**: Easy to modify colors, fonts, and layout

## 🛠️ Managing Your Site

Once your site is created, you can manage it easily:

```bash
# Review your site configuration
./manage.py gh-page review-config yourusername.github.io

# Check what content pages you have
./manage.py gh-page review-content yourusername.github.io

# Update site settings (title, description, etc.)
./manage.py gh-page update-metadata yourusername.github.io title="My Amazing Site"

# Push changes to GitHub
./manage.py gh-page push yourusername.github.io
```

## 🔧 Troubleshooting

**Common Issues:**

1. **"Template not found" error**: Make sure you've installed dependencies with `pip install python-dotenv PyYAML`

2. **Git push fails**:
   - Check your SSH key is set up with GitHub
   - Verify the repository exists on GitHub
   - Make sure `.env` has the correct `GIT_REMOTE` URL

3. **Site not loading**:
   - GitHub Pages can take 5-10 minutes to deploy
   - Check repository settings → Pages → Source is set to "Deploy from branch: main"

4. **Bundle install fails**:
   - Install Ruby: `brew install ruby` (macOS) or follow [Ruby installation guide](https://www.ruby-lang.org/en/documentation/installation/)
   - Retry with: `./manage.py gh-page init alfolio --bundle`

## 🎯 Next Steps After Setup

1. **Customize your site**: Edit `_config.yml` in your site directory
2. **Add your photo**: Replace `assets/img/prof_pic.jpg`
3. **Update your bio**: Edit `_pages/about.md`
4. **Add publications**: Place BibTeX files in `_bibliography/`
5. **Create blog posts**: Add Markdown files to `_posts/`

## 🚀 Advanced Usage

### Multiple Sites
```bash
# Create different sites for different purposes
./manage.py gh-page init alfolio --dir my-research-site
./manage.py gh-page init alfolio --dir my-teaching-site
```

### Custom Configuration
```bash
# Use different branch or remote
./manage.py gh-page init alfolio --branch gh-pages --remote https://github.com/user/repo.git
```

## 🔮 Coming Soon

- More templates (Hugo, plain Jekyll, etc.)
- Interactive setup wizard
- Automated dependency checking
- Content migration tools

---

**Need help?** Open an issue or check `CLAUDE.md` for technical details.