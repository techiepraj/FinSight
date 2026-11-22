from flask import Flask
from config import Config
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    import models  # noqa: F401  (this registers the tables)

    @app.route("/")
    def home():
        return "FinSight is running!"

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)