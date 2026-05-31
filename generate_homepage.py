import os


def generate_homepage():

    folders = []

    IGNORE_FOLDERS = {
    ".vercel",
    "__pycache__"
    }

    for item in os.listdir("generated"):

        if item in IGNORE_FOLDERS:
            continue

        path = os.path.join("generated", item)

        if os.path.isdir(path):
            folders.append(item)

    cards = ""

    for folder in sorted(folders):

        cards += f"""
        <div class="bg-zinc-900 border border-zinc-800 rounded-3xl p-6 hover:border-cyan-400 transition">

            <h3 class="text-2xl font-bold">
                {folder.replace("-", " ").title()}
            </h3>

            <p class="text-gray-400 mt-2">
                AI Generated Website
            </p>

            <a
                href="/{folder}"
                target="_blank"
                class="mt-6 inline-block bg-cyan-500 hover:bg-cyan-400 text-black px-5 py-3 rounded-xl font-semibold transition">

                Open Website

            </a>

        </div>
        """

    with open(
        "templates/homepage.html",
        "r",
        encoding="utf-8"
    ) as f:

        html = f.read()

    html = html.replace(
        "<!-- GENERATED_CARDS -->",
        cards
    )

    with open(
        "generated/index.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print("Homepage generated successfully")