import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # grab secret key to protect against CSRF attacks in flask login and sign-up forms
    SECRET_KEY = os.getenv("SECRET_KEY") or "you-will-never-guess"

    # configuration for sqlite database - for testing
    # will switch to MySQL Database for production
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///{}".format(os.path.join(basedir, "app.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False