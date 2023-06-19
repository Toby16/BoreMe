from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app) # database object
migrate = Migrate(app, db) # migration object

from BoreMe_app import routes, models