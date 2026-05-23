from importlib.resources import path

from flask import Flask, request
from dotenv import load_dotenv
from ai.planner import generate_website_plan
from ai.website_generator import generate_website_code
from deployment.deployer import deploy_to_netlify
from deployment.vercel_deployer import deploy_to_vercel
from generator.builder import save_website
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"


@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get("Body", "")
    print("MESSAGE:", incoming_msg)
    plan = generate_website_plan(incoming_msg)
    html = generate_website_code(plan)
    project_name = plan["business_name"]
    path = save_website(
        html,
        project_name
    )
    deploy_to_vercel("generated")
    live_url = f"https://generated-nu.vercel.app/{path}"
    print("LIVE URL:", live_url)
    response = MessagingResponse()
    response.message(
        f"Your website is ready!\n\n{live_url}"
    )
    return str(response)


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)