from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """Hello, World! This is a Flask App Tier-3 Devops Project !
    This project demonstrates containerization, CI/CD, and cloud deployment, showcasing strong Tier 3 DevOps skills while using free resources.
    Github: https://github.com/muhammadharoon26/flask-app-tier3-devops-project.git
    Made By: muhammadharoon26.vercel.app"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
