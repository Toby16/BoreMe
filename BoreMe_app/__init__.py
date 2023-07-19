from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__) # flask object
app.config.from_object(Config)

db = SQLAlchemy(app) # database object
migrate = Migrate(app, db) # migration object

login = LoginManager(app) # object to manage user logged-in state
login.login_view = "login" # requiring users to login
socketio = SocketIO(app)

from BoreMe_app import routes, models