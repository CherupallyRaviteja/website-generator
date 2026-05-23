from groq import Groq
from dotenv import load_dotenv

import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_website_code(plan):

    prompt = f"""
    Create a complete modern responsive website.

    WEBSITE PLAN:
    {plan}

    REQUIREMENTS:

    - Return ONLY HTML
    - Include EXACTLY:
      <script src="https://cdn.tailwindcss.com"></script>

    - Use Tailwind CSS
    - Professional modern UI
    - Functional JavaScript
    - Responsive navbar
    - Working forms/buttons
    - Smooth scrolling
    - Mobile responsive
    - Use dark themed inputs if dark UI
    - No markdown
    - No explanation

    Add all JavaScript inside <script> tags.
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    html = response.choices[0].message.content

    html = html.replace("```html", "")
    html = html.replace("```", "")

    return html