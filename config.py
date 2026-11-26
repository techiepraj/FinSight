import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///finsight.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session cookie security
    SESSION_COOKIE_HTTPONLY = True     # JavaScript cannot read the cookie
    SESSION_COOKIE_SAMESITE = "Lax"    # helps block cross-site requests
    # SESSION_COOKIE_SECURE = True     # turn on when the site is served over HTTPS