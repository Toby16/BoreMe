from BoreMe_app import app
from flask import render_template, flash, redirect
from BoreMe_app.forms import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user - {}, remember_me={}".format(
            form.username.data,
            form.remember_me.data)
        )
        return redirect("/welcome")
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