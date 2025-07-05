import os
import re

# Paths
TEMPLATE_PATH = 'html_template.html'
MD_DIR = 'submissions'
HTML_DIR = 'html'

# Fields and regex patterns
fields = {
    'Project_Title': r'## Project Title\s*\n(.*)',
    'Student_Names': r'## Student Name\(s\)\s*\n(.*)',
    'Project_Overview': r'## Project Overview\s*\n(.*)',
    'Technologies_Used': r'## Technologies Used\s*\n(.*)',
    'Results_Outcomes': r'## Results / Outcomes\s*\n(.*)',
}

# Helper to extract content for each field
def extract_field(md, pattern):
    match = re.search(pattern, md)
    if match:
        return match.group(1).strip()
    return ""

# Load HTML template
with open(TEMPLATE_PATH, encoding='utf-8') as f:
    template = f.read()

os.makedirs(HTML_DIR, exist_ok=True)

# Process each markdown file in submissions/
for filename in os.listdir(MD_DIR):
    if filename.endswith('.md'):
        with open(os.path.join(MD_DIR, filename), encoding='utf-8') as f:
            md = f.read()
        html = template
        for key, pattern in fields.items():
            html = html.replace('{' + key + '}', extract_field(md, pattern))
        output_file = os.path.splitext(filename)[0] + '.html'
        with open(os.path.join(HTML_DIR, output_file), 'w', encoding='utf-8') as out:
            out.write(html)
