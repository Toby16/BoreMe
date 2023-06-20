from BoreMe_app import app, db
from flask import render_template, flash, redirect, url_for, request
from BoreMe_app.forms import LoginForm, RegisterationForm
from flask_login import current_user, login_user, logout_user, login_required
from BoreMe_app.models import User
from werkzeug.urls import url_parse

# view funtion to welome page
@app.route("/")
@app.route("/welcome/")
def welcome():
    if current_user.is_authenticated:
        return redirect(url_for("home")) # will change this when needed
    return render_template("welcome.html")


# view function for tutorial page
@app.route("/tutorial/")
def tutorial():
    return render_template("tutorial.html")


# view function for Home page
@app.route("/home/")
@login_required
def home():
    # this view function will display a box which display the availble and general rooms to join for the game
    # with a frontend indicating a title 'Rooms', and then including the rooms for user to join to then start the game with other users
    # for now, users can't have private rooms, will add that as an update some other time
    return render_template("home.html", title='Home')


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
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("home")
        return redirect(next_page) # will change this when needed
    return render_template("login.html", title="login", form=form)


# view function for current_user logout
@app.route("/logout/")
def logout():
    logout_user() # logs a user out. This will also clean the 'remember_me' cookie if it exists
    return redirect(url_for("home"))

# view function for user account registeration
@app.route("/register/", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegisterationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash ("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Registeration", form=form)

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