import click
from flask import Flask, redirect, url_for
from flask_login import current_user

from config import Config
from extensions import db, login_manager, csrf


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from routes.auth import auth_bp
    from routes.dashboard import dashboard_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    @app.route("/")
    def home():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard.index"))
        return redirect(url_for("auth.login"))

    @app.cli.command("create-admin")
    @click.option("--name", prompt=True)
    @click.option("--email", prompt=True)
    @click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
    def create_admin(name, email, password):
        """Create an admin account: flask --app app create-admin"""
        email = email.strip().lower()
        if User.query.filter_by(email=email).first():
            click.echo("A user with that email already exists.")
            return
        if len(password) < 8:
            click.echo("Password must be at least 8 characters.")
            return
        admin = User(name=name.strip(), email=email, role="admin")
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        click.echo("Admin account created.")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)