from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def start():
    secret = os.getenv("LAPTOP_PASSWORD")
    return "<p>Just getting the hang of Flask routing.</p>" f" Here is the password to my laptop: {secret}"

@app.route("/about")
def about():
    return "<h2>About</h2><p>This app is part of my DevSecOps encryption project.</p>"

@app.route("/status")
def status():
    return "<h2>Status</h2><p>The app is up and running 🔒</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
