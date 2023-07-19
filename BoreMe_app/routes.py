from BoreMe_app import app, db, socketio
from flask_socketio import emit
from flask import render_template, flash, redirect, url_for, request, jsonify, session
from BoreMe_app.forms import LoginForm, RegisterationForm, PlayerVsPcForm
from flask_login import current_user, login_user, logout_user, login_required
from BoreMe_app.models import User
from werkzeug.urls import url_parse
import random # for game logic

"""
Things left to complete
1. when the player or pc score gets to 10, the game ends
the player gets redirected to the home page to pick a mode and start a new game
A flashed message will be displayed in the game-mode page indicating whether the player or the pc won

2. to fix the game status (  `game_status = "Click to generate new number"` when pc gets a point)
"""

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


@app.route("/start/game/vs_pc", methods=["GET", "POST"])
@login_required
def start_game_pc():
    form = PlayerVsPcForm()

    if request.method == "POST":
        # Generate the random number and store it in the session
        session["prev_target_number"] = None ##
        target_number = generate_random_number()
        session["target_number"] = target_number ##
        session['target_number'] = target_number
        # print("target number:", target_number)  # for testing - will remove later
        return jsonify(target_number=target_number, player_status="waiting")

    game_status = "Click here to start"
    session["game_status"] = game_status #

    player_score = 0
    pc_score = 0
    session["player_score"] = player_score
    session["pc_score"] = pc_score

    session["pc_high"] = 100
    session["pc_low"] = 1

    player_status = "waiting"
    pc_status = "waiting"

    ## -----------------------------
    """
    To redirect page back to route function
    with message of who wins in the 'player_vs_pc' mode
    """
    """
    player_score = session.get("player_score")
    pc_score = session.get("pc_score")

    if player_score == 10:
        flash("{} won!".format(current_user.username))
        return redirect(url_for("home"))
    elif pc_score == 10:
        flash("PC won!")
        return redirect(url_for("home"))
    """
    ## ---------------------------------

    return render_template("player_vs_pc.html",
                           title="Player vs PC",
                           game_status=game_status,
                           player_score=player_score,
                           pc_score=pc_score,
                           form=form,
                           player_status=player_status,
                           pc_status=pc_status
                           )


@app.route("/start/game/vs_pc/player", methods=["POST"])
def user_submit():
    target_number = session.get('target_number')  # Retrieve the stored target number from the session
    json_data = request.get_json()
    prev_guess = session.get('user_input')
    user_input = None
    difference = None
    game_status = "Random number generated"
    try:
        user_input = int(json_data['user_input'])
        difference = target_number - user_input
    except:
        player_status = "Invalid input"
    # user_input = int(form.user_input.data)
    # print("user_input:", user_input)  # for testing - will remove later
    player_score = session.get("player_score") + 1

    if type(difference) is not int:
        player_status = "Invalid input"
    elif difference == 0:
        player_status = "Correct"
        if prev_guess == user_input:
            session["player_score"] += 0  # same as `player_score = session.get("player_score")`
        else:
            session["player_score"] = player_score
        game_status = "Click to generate new number"
        session["game_status"] = game_status
        game_status = session.get("game_status")
        # session["target_number"] = generate_random_number()
    elif difference in range(1, 11):
        player_status = "little low"
    elif difference in range(-10, 0):
        player_status = "little high"
    elif difference in range(11, 21):
        player_status = "low"
    elif difference in range(-20, -10):
        player_status = "high"
    elif difference in range(21, 31):
        player_status = "very low"
    elif difference in range(-30, -20):
        player_status = "very high"
    else:
        player_status = "too far"

    session["user_input"] = user_input

    ## ------------------------------------------
    player_score = session.get("player_score")

    """
    if player_score == 10:
        flash("{} won!".format(current_user.username))
        return redirect(url_for("home"))
    """
    ## ----------------------------------------------
    
    return jsonify(player_status=player_status,
                   player_score=session.get("player_score"),
                   pc_score=session.get("pc_score"),
                   game_status=game_status), 200
                   


# generate random number for pc
def generate_pc_guess(x=1, y=100):
    return random.randint(x, y)


@app.route("/start/game/vs_pc/pc", methods=["POST"])
def pc_submit():
    """
    pc_submit: function to generate random number for pc according to predefined rules
    Report:
        this function works properly but it has a little problem..
        it isn't efficient enough as it takes the pc a little more time to get the target_number

        This makes the player vs pc mode a little easier for the player/user to play
    """
    target_number = session.get('target_number')  # Retrieve the stored target number from the session
    prev_guess = session.get('pc_input')  # Retrieve the previous guess from the session
    # pc_high = session.get("pc_high")# 100
    # pc_low = session.get("pc_low")  # 1
    pc_high = session.get("pc_high")
    pc_low = session.get("pc_low")
    game_status = "Random number generated"



    # Logic to generate the PC's guess
    if (prev_guess is None) or (session["prev_target_number"] != session["target_number"]):
        """
        This conditional statement is created to improve and fix the pc's guessing ability.
        When a random number gets generated, it gets stored in a session 'session["target_number"]'.
        'session["target_number"]' gets compared with 'session["prev_target_number"]',
          which is the previous target number before a new random number gets generated.

        if session["prev_target_number"] is not same with session["target_number"],
         then it means the pc's guession algorithm starts afresh to guess the newly generated target number
         else, it should continue with it's current guessing and not start over again.

        Also, the pc_low and pc_high gets reset back to it's default value in the session
        """
        session["prev_target_number"] = session["target_number"]
        session["pc_low"] = 1
        session["pc_high"] = 100
        pc_low = session["pc_low"]
        pc_high = session["pc_high"]
        pc_input = generate_pc_guess()
        session["pc_input"] = pc_input
    else:
        if prev_guess == target_number:
            pc_input = prev_guess
        elif prev_guess > target_number:
            session["pc_high"] = prev_guess
            pc_high = session.get("pc_high")
            # pc_input = generate_pc_guess(pc_low, pc_high - 1)
            if pc_low < (pc_high - 1):
                pc_input = generate_pc_guess(pc_low, pc_high - 1)
            elif pc_low == pc_high - 1:
                pc_input = pc_low  # or 'pc_high - 1'
            else:
                # Handle the case where pc_low is greater than pc_high - 1 (should not happen)
                pc_input = generate_pc_guess(pc_high - 1, pc_low)
        else:
            session["pc_low"] = prev_guess
            pc_low = session.get("pc_low")
            # pc_input = generate_pc_guess(pc_low + 1, pc_high)
            if pc_low + 1 < pc_high:
                pc_input = generate_pc_guess(pc_low + 1, pc_high)
            elif pc_low + 1 == pc_high:
                pc_input = pc_low + 1  # or 'pc_high'
            else:
                # Handle the case where pc_high is less than pc_low + 1 (should not happen)
                pc_input = generate_pc_guess(pc_low, pc_high)


    pc_score = session.get("pc_score") + 1
    # Calculate the difference between PC's guess and the target number
    difference = target_number - pc_input

    # Determine the PC's status based on the difference
    if type(difference) is not int:
        pc_status = "Invalid input"
    elif difference == 0:
        pc_status = "Correct"
        session["pc_low"] = 1 #
        session["pc_high"] = 100 #
        if prev_guess == target_number:
            session["pc_score"] += 0
        else:
            session["pc_score"] = pc_score
        game_status = "Click to generate new number"
        session["game_status"] = game_status
        game_status = session.get("game_status")
    elif difference in range(1, 11):
        pc_status = "little low"
    elif difference in range(-10, 0):
        pc_status = "little high"
    elif difference in range(11, 21):
        pc_status = "low"
    elif difference in range(-20, -10):
        pc_status = "high"
    elif difference in range(21, 31):
        pc_status = "very low"
    elif difference in range(-30, -20):
        pc_status = "very high"
    else:
        pc_status = "too far"

    # Update the session with the current guess
    session["pc_input"] = pc_input

    pc_score = session.get("pc_score")
    ## ---------------------------------------------
    """
    if pc_score == 10:
        flash("PC won!")
        return redirect(url_for("home"))
    """
    ## -------------------------------------

    return jsonify(pc_input=pc_input,
                   pc_status=pc_status,
                   pc_score=pc_score,
                   game_status=game_status), 200



## settings for 'Group vs Group mode' - Coming Soon!
@app.route("/start/game/player_vs_player/")
def group_vs_group():
    title = "player_vs_player"
    return render_template("player_vs_player.html", title=title)




## settings for 'player_vs_player' mode
@app.route("/start/game/chat_room/", methods=["GET", "POST"])
def player_vs_player():
    user_name = current_user.username
    return render_template("chat.html", user_name=user_name, title="General Chat")

@socketio.on("connect")
def chat_connect():
    print("Client Connected!")

@socketio.on("disconnect")
def chat_disconnect():
    print("Client Disconnected")

@socketio.on("message")
def chat_message(data):
    name = current_user.username  #current user's username
    msg = "{}: {}".format(name, data)
    print(msg)
    emit("message", msg, broadcast=True, include_self=False)