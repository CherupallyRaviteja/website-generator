import os
import uuid
import os
import re

def slugify(text):

    text = text.lower()

    text = re.sub(r'[^a-z0-9]+', '-', text)

    return text.strip("-")


def save_website(html, project_name):

    slug = slugify(project_name)

    output_dir = os.path.join(
        "generated",
        slug
    )

    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(
        output_dir,
        "index.html"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return slug