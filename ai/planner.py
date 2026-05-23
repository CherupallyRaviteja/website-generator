from groq import Groq
from dotenv import load_dotenv

import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_website_plan(user_prompt):

    prompt = f"""
    Analyze this website request.

    USER REQUEST:
    {user_prompt}

    Return ONLY valid JSON.

    JSON format:

    {{
      "website_type": "",
      "business_name": "",
      "theme": "",
      "sections": [],
      "features": [],
      "functionality": []
    }}
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    content = response.choices[0].message.content

    content = content.replace("```json", "")
    content = content.replace("```", "")

    return json.loads(content)