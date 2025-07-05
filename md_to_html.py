import os
import re
from git import Repo

# Set paths
TEMPLATE_PATH = 'html_template.html'
MD_DIR = 'submissions'
HTML_DIR = 'html'

# Fields to extract from markdown
fields = {
    'Project_Title': r'## Project Title\s*\n(.*)',
    'Student_Names': r'## Student Name\(s\)\s*\n(.*)',
    'Project_Overview': r'## Project Overview\s*\n(.*)',
    'Technologies_Used': r'## Technologies Used\s*\n(.*)',
    'Results_Outcomes': r'## Results / Outcomes\s*\n(.*)',
}

def extract_field(md, pattern):
    match = re.search(pattern, md)
    if match:
        return match.group(1).strip()
    return ""

def get_changed_files():
    repo = Repo(os.getcwd())
    # Get files changed in the last commit
    changed = set()
    for commit in repo.iter_commits('HEAD', max_count=1):
        for file in commit.stats.files:
            if file.startswith(f"{MD_DIR}/") and file.endswith(".md"):
                changed.add(file)
    return changed

with open(TEMPLATE_PATH, encoding='utf-8') as f:
    template = f.read()

os.makedirs(HTML_DIR, exist_ok=True)

changed_files = get_changed_files()

for file_path in changed_files:
    filename = os.path.basename(file_path)
    with open(file_path, encoding='utf-8') as f:
        md = f.read()
    html = template
    for key, pattern in fields.items():
        html = html.replace('{' + key + '}', extract_field(md, pattern))
    output_file = os.path.splitext(filename)[0] + '.html'
    with open(os.path.join(HTML_DIR, output_file), 'w', encoding='utf-8') as out:
        out.write(html)
