from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) # flask object
app.config.from_object(Config)

db = SQLAlchemy(app) # database object
migrate = Migrate(app, db) # migration object

login = LoginManager(app) # object to manage user logged-in state

from BoreMe_app import routes, models