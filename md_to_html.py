import os
import re

TEMPLATE_PATH = 'html_template.html'
OUTPUT_DIR = 'html'
MD_DIR = 'submissions'

fields = {
    'Project_Title': r'## Project Title\n(.*)',
    'Student_Names': r'## Student Name\(s\).*?\n(.*)',
    'Adviser': r'## Adviser/Supervisor.*?\n(.*)',
    'Course': r'## Course or Department.*?\n(.*)',
    'Duration': r'## Project Duration.*?\n(.*)',
    'Project_Overview': r'## Project Overview.*?\n(.*)',
    'Problem_Statement': r'## Problem Statement / Motivation.*?\n(.*)',
    'Goals': r'## Goals/Objectives.*?\n(.*)',
    'Features': r'## Key Features / Functionality.*?\n(.*)',
    'Technologies': r'## Technologies Used.*?\n(.*)',
    'Challenges': r'## Major Challenges & Solutions.*?\n(.*)',
    'Results': r'## Results / Outcomes.*?\n(.*)',
    'Screenshots': r'## Screenshots / Demo Links.*?\n(.*)',
    'Future_Work': r'## Future Work / Improvements.*?\n(.*)',
    'Lessons': r'## Lessons Learned / Reflections.*?\n(.*)',
    'Acknowledgments': r'## Acknowledgments.*?\n(.*)',
    'How_To_Run': r'## How to Run / Use the Project.*?\n(.*)',
    'Links': r'## Relevant Links.*?\n(.*)',
}

def extract_field(md, pattern):
    match = re.search(pattern, md, re.DOTALL)
    if not match:
        return ""
    val = match.group(1).strip()
    # Support bulleted lists: keep only until next heading
    val = re.split(r'\n## ', val)[0].strip()
    return val

with open(TEMPLATE_PATH) as f:
    template = f.read()

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(MD_DIR):
    if filename.endswith('.md'):
        with open(os.path.join(MD_DIR, filename)) as f:
            md = f.read()
        html = template
        for key, pattern in fields.items():
            html = html.replace('{' + key + '}', extract_field(md, pattern))
        out_name = os.path.splitext(filename)[0] + '.html'
        with open(os.path.join(OUTPUT_DIR, out_name), 'w') as out:
            out.write(html)
