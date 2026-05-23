import subprocess
import os

from dotenv import load_dotenv

load_dotenv()

VERCEL_TOKEN = os.getenv("VERCEL_TOKEN")

def deploy_to_vercel(folder_path):

    result = subprocess.run(

        [
            r"C:\Users\user\AppData\Roaming\npm\vercel.cmd",
            "--prod",
            "--yes",
            "--public",
            "--token",
            VERCEL_TOKEN
        ],

        cwd=folder_path,

        capture_output=True,
        text=True
    )

    print(result.stdout)

    print(result.stderr)

    for line in result.stdout.splitlines():
        line = line.strip()
        if "Aliased" in line:
            return line.split()[-1]

    return "Deployment Failed"