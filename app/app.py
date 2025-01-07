from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World! This is a Flask App Tier-3 Devops Project !"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
