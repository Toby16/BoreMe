#!/usr/bin/env python

from BoreMe_app import app, db, socketio
from BoreMe_app.models import User


if __name__ == "__main__":
    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User}
    socketio.run(app, debug=True)


