import os
import time
import zipfile
import requests
import uuid

from dotenv import load_dotenv

load_dotenv()

NETLIFY_TOKEN = os.getenv("NETLIFY_AUTH_TOKEN")


def zip_folder(folder_path, zip_path):

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for root, dirs, files in os.walk(folder_path):

            for file in files:

                file_path = os.path.join(root, file)

                arcname = os.path.relpath(
                    file_path,
                    folder_path
                )

                zipf.write(file_path, arcname)


def deploy_to_netlify(folder_path):

    zip_name = f"{uuid.uuid4()}.zip"

    zip_folder(folder_path, zip_name)

    headers = {
        "Authorization": f"Bearer {NETLIFY_TOKEN}"
    }

    # CREATE SITE

    site_response = requests.post(
        "https://api.netlify.com/api/v1/sites",
        headers=headers
    )

    site_data = site_response.json()

    site_id = site_data["id"]

    print("SITE CREATED:", site_id)

    # DEPLOY ZIP

    with open(zip_name, "rb") as f:

        deploy_response = requests.post(
            f"https://api.netlify.com/api/v1/sites/{site_id}/deploys",
            headers=headers,
            files={
                "file": f
            }
        )

    print("DEPLOY STATUS:", deploy_response.status_code)

    print("DEPLOY RESPONSE:")
    print(deploy_response.text)

    deploy_data = deploy_response.json()

    os.remove(zip_name)

    return site_data["ssl_url"]