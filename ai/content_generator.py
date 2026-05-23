def generate_content(data):

    return {
        "hero_title": f"Welcome To {data['business_name']}",
        "hero_subtitle": "Professional services for modern businesses.",

        "about_title": "About Us",

        "about_text":
        f"{data['business_name']} is committed to delivering quality experiences and customer satisfaction.",

        "services": [
            "Premium Quality",
            "Fast Service",
            "Affordable Pricing"
        ]
    }