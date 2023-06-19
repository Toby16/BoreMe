from BoreMe_app import app
from flask import render_template, flash, redirect, url_for
from BoreMe_app.forms import LoginForm
from flask_login import current_user, login_user
from BoreMe_app.models import User

# view funtion to welome page
@app.route("/")
@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")


# view function for tutorial page
@app.route("/tutorial/")
def tutorial():
    return render_template("tutorial.html")

# view function for Home page
@app.route("/home/")
def home():
    return render_template("home.html")


# view function for user login
@app.route("/login/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home")) # will change this when needed
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("home")) # will change this when needed
    return render_template("login.html", title="login", form=form)

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