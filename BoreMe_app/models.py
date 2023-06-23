from BoreMe_app import db, login
import uuid
from werkzeug.security import check_password_hash, generate_password_hash # for generating and authenticating password hashes
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(70)) # i will be storing hashes here instead of actual password
    user_id = db.Column(db.String(32), unique=True, nullable=False, default=lambda: str(uuid.uuid4().hex)) # a special identification for each users

    def __repr__(self):
        return "(User - {} - {})".format(self.username, self.user_id)
    
    # method to generate and setting user password hash
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # method for authenticating user password with existing password hash
    def check_password(self, password):
        return check_password_hash(self.password, password)


# user loader function
@login.user_loader
def load_user(id):
    return User.query.get(int(id))