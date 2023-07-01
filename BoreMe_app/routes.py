from BoreMe_app import app, db
from flask import render_template, flash, redirect, url_for, request
from BoreMe_app.forms import LoginForm, RegisterationForm, PlayerVsPcForm
from flask_login import current_user, login_user, logout_user, login_required
from BoreMe_app.models import User
from werkzeug.urls import url_parse
import random # for game logic

# view funtion to welome page
@app.route("/")
@app.route("/welcome/")
def welcome():
    if current_user.is_authenticated:
        return redirect(url_for("home")) # will change this when needed
    flash ("For your mobile devices, ensure you switch to desktop mode!")
    return render_template("welcome.html")


# view function for tutorial page
@app.route("/tutorial/")
def tutorial():
    return render_template("tutorial.html")


# view function for Home page
@app.route("/home/")
@login_required
def home():
    # this view function will display a box which display the 'availble and general rooms' to join for the game
    # with a frontend indicating a title 'Rooms', and then including the rooms for user to join to then start the game with other users
    # for now, users can't have private rooms, will add that as an update some other time
    return render_template("home.html", title='Home/Game-Mode')


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
@app.route("/user_profile/<username>/<user_id>/")
@login_required
def profile(username, user_id):
    # the route displays both user's username and user_id
    # for example 'http://127.0.0.1:5000/user_profile/test_user/34b8962a585d449abb7f3813b3ed36d3/'
    user = User.query.filter_by(username=username).first_or_404()
    return render_template("user_profile.html", user=user, title=str(user.username))

# view function for game session
@app.route("/start/game/")
def start_game():
    # Login to generate random number and start a new game session
    return "Game Start Page"

# view function to generate leaderboard data
@app.route("/leaderboard/")
def leaderboard():
    return "Leaderboard page"


## ----------------------------

# game logic
def generate_random_number():
    return random.randint(1, 100)


# Compare the guess with the target number
def compare_guess(guess, target_number):
    if guess == target_number:
        return "Correct"
    elif guess < target_number:
        return "Too low"
    else:
        return "Too high"




from flask import jsonify, session

@app.route("/start/game/vs_pc", methods=["GET", "POST"])
@login_required
def start_game_pc():
    form = PlayerVsPcForm()
    # session["target_number"] = None
    # print("form.submit.data:", form.submit.data)

    if request.method == "POST": # and target_number is None and (form.submit.data is False):
        # Generate the random number and store it in the session
        target_number = generate_random_number()
        session['target_number'] = target_number
        print("target number -:", target_number)  # for testing - will remove later
        return jsonify(target_number=target_number, player_status="waiting")
    """
    elif request.method == "POST" and target_number is not None and (form.submit.data is False):
        print("target number:", target_number) # for testing - will remove later
        print("request.form:", request.form) # for testing - will remove later
        print("form.submit.data:", form.submit.data) # for testing - will remove later
        form.submit.data = True
        return jsonify(target_number=target_number, player_status="waiting")
    """

    game_status = "Click here to start"
    player_score = 0
    session["player_score"] = player_score
    pc_score = 0
    session["pc_score"] = pc_score
    # form.submit.data = True

    player_status = "waiting"
    # if form.validate_on_submit():
    

    return render_template("player_vs_pc.html",
                           title="Player vs PC",
                           game_status=game_status,
                           player_score=player_score,
                           pc_score=pc_score,
                           form=form,
                           player_status=player_status
                           )


@app.route("/start/game/vs_player_play", methods=["POST"])
def user_submit():
    # if request.method == "POST" and target_number is not None and form.submit.data is True:
    target_number = session.get('target_number')  # Retrieve the stored target number from the session
    json_data = request.get_json()
    user_input = int(json_data['user_input'])
    # user_input = int(form.user_input.data)
    print("user_input:", user_input)  # for testing - will remove later
    player_score = session.get("player_score") + 1
    difference = abs(target_number - user_input)

    if difference == 0:
        player_status = "Correct"
        session["player_score"] = player_score
        # session["target_number"] = generate_random_number()
    elif difference > 10:
        player_status = "Too far"
    else:
        player_status = "Near"
    return jsonify(player_status=player_status,
                   player_score=session.get("player_score"),
                   pc_score=session.get("pc_score")), 200


@app.route("/start/game/vs_pc_play", methods=["POST"])
def pc_submit():
    """
    # if request.method == "POST" and target_number is not None and form.submit.data is True:
    target_number = session.get('target_number')  # Retrieve the stored target number from the session
    json_data = request.get_json()
    user_input = int(json_data['user_input'])
    # user_input = int(form.user_input.data)
    print("user_input:", user_input)  # for testing - will remove later
    player_score = session.get("player_score") + 1
    difference = abs(target_number - user_input)

    if difference == 0:
        player_status = "Correct"
        session["player_score"] = player_score
        # session["target_number"] = generate_random_number()
    elif difference > 10:
        player_status = "Too far"
    else:
        player_status = "Near"
    return jsonify(player_status=player_status,
                   player_score=session.get("player_score"),
                   pc_score=session.get("pc_score")), 200
    """