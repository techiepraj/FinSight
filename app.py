import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()  # reads the .env file into environment variables

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


@app.route("/")
def home():
    return "FinSight is running!"


if __name__ == "__main__":
    app.run(debug=True)