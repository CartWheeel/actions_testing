# Markdown-to-HTML Profile Automation

This repo is a playground to test GitHub Actions: markdown converting to html. GitHub Actions will automatically generate a personal webpage from a submitted markdown file.

---

## How It Works

1. **Fill in your Information** using the [markdown template](md2html/templates/profile_template.md).
2. **Save and Submit your markdown file** (`yourname.md`) to the [profiles_md folder](md2html/profiles_md) by creating a pull request to `main`.
3. **Once approved merged,** the system will:
    - Generate your full HTML profile page
4. **To make changes,** simply update your current file and submit again. 

---

**Current Template:**
```markdown
## Project Title
Test Project - markdown to html 

## Student Name(s)
John Doe

## Project Overview
This project demonstrates automated markdown-to-HTML conversion with GitHub Actions.

## Technologies Used
Python, GitHub Actions

## Results / Outcomes
HTML was generated automatically and information was updated correctly.
```
---
## Known Issues
1. **Over-generalize Template**
2. **Unable to make lists or skip multiple lines**
3. **Profile cards are not being generated**
