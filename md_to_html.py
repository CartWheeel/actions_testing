import os
import re
import subprocess

TEMPLATE_PATH = 'html_template.html'
MD_DIR = 'submissions'
HTML_DIR = 'html'

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

# Get list of changed files from the last commit (push/merge)
def get_changed_files():
    # Get last two commit hashes
    commits = subprocess.check_output(['git', 'rev-list', '--max-count=2', 'HEAD']).decode().split()
    if len(commits) < 2:
        return []
    latest, previous = commits[0], commits[1]
    diff_output = subprocess.check_output(['git', 'diff', '--name-only', previous, latest]).decode().splitlines()
    # Only keep .md files in submissions/
    return [f for f in diff_output if f.startswith(f"{MD_DIR}/") and f.endswith(".md")]

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
