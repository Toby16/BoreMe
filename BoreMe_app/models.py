from BoreMe_app import db
import uuid

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(70)) # i will be storing hashes here instead of actual password
    user_id = db.Column(db.String(32), unique=True, nullable=False, default=lambda: str(uuid.uuid4().hex)) # a special identification for each users

    def __repr__(self):
        return "(User - {} - {})".format(self.username, self.user_id)