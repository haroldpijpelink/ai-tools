#!/usr/bin/env python3
"""Convert markdown one-pagers to PDF."""

import glob
import os
import markdown
from weasyprint import HTML

CSS = """@page { size: A4; margin: 2cm; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #1a1a1a; }
h1 { font-size: 28px; color: #1e3a5f; border-bottom: 2px solid #1e3a5f; padding-bottom: 8px; margin-top: 0; }
h2 { font-size: 20px; color: #2d5a8e; margin-top: 24px; }
strong { color: #1e3a5f; }
a { color: #2d5a8e; }
ul { padding-left: 20px; }
li { margin-bottom: 4px; }"""


def convert(md_path: str):
    name = os.path.splitext(os.path.basename(md_path))[0]
    pdf_path = f"/home/harold/projects/ai-consulting-landing/one-pagers/{name}.pdf"
    html_content = markdown.markdown(open(md_path).read(), extensions=["tables"])
    full_html = (
        f"<html><head><style>{CSS}</style></head><body>{html_content}</body></html>"
    )
    HTML(string=full_html, base_url=os.path.dirname(md_path)).write_pdf(pdf_path)
    print(f"✓ {name}.pdf")


for f in sorted(
    glob.glob("/home/harold/projects/ai-consulting-landing/one-pagers/*.md")
):
    convert(f)
