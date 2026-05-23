import re

def extract_requirements(user_message):

    message = user_message.lower()

    website_type = "business"

    if "restaurant" in message:
        website_type = "restaurant"

    elif "portfolio" in message:
        website_type = "portfolio"

    elif "store" in message:
        website_type = "store"

    business_name = "My Business"

    match = re.search(r'for (.+)', message)

    if match:
        business_name = match.group(1).title()

    return {
        "type": website_type,
        "business_name": business_name,
        "style": "modern",
        "sections": [
            "hero",
            "about",
            "services",
            "contact"
        ]
    }