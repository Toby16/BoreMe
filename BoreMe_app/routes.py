from BoreMe_app import app
from flask import render_template

# view function for Home page
@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")


# view function for user login
@app.route("/login/")
def login():
    return render_template("login.html")

# view function for user account registeration
@app.route("/register/")
def register():
    return render_template("register.html")

# view function for user profile after login
@app.route("/user_profile/<username>")
def profile(username):
    return render_template("user_profile.html")

# view function for game session
@app.route("/start/game/")
def start_game():
    # Login to generate random number and start a new game session
    return "Game Start Page"

# view function to generate leaderboard data
@app.route("/leaderboard/")
def leaderboard():
    return "Leaderboard page"