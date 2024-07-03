from boggle import Boggle
from flask import (
    Flask,
    render_template,
    session,
    request,
    jsonify,
)
from flask_debugtoolbar import DebugToolbarExtension

# Initialization of Flask Application
app = Flask(__name__)

# Setting Configuration
# The `SECRET_KEY` is used to maintain sessions and
# protect against certain types of attacks.
app.config["SECRET_KEY"] = "play"
app.debug = True

# Enables debug mode, provides detailed erro msg.
app.debug = True

# Install flask debug toolbar
debug = DebugToolbarExtension(app)


# Create the Boggle game object
boggle_game = Boggle()


@app.route("/", methods=["GET"])
def home_page():
    """
    Render home page with a Boggle game board.

    """
    game_board = boggle_game.make_board()
    session["game_board"] = game_board
    return render_template("index.html", game_board=game_board)


@app.route("/submit-guess", methods=["POST"])
def submit_guess():
    """
    Handle submission of a word guess in the game.

    """

    # take the form value and check if it is a valid word in the dictionary using the words variable in your app.py
    guess = request.json.get("keyword")

    game_board = session["game_board"]
    response = boggle_game.check_valid_word(game_board, guess)

    # `jsonify` converts Python data into a JSON format that can be sent and understood by JavaScript.
    return jsonify({"result": response})


@app.route("/post-score", methods=["POST"])
def post_score():
    """
    Finalize player's score of the game.

    """

    # RETRIEVING SESSION DATA

    # Retrieves the score data from the request body.
    # returns `none` if the key doesn't exist.
    score = request.json.get("score")  # 1

    # Retrieves the current high score from the user session.
    # returns `0` if the key doesn't exist.
    highScore = session.get("highScore", 0)

    # Retrieves the number of games played from user session.
    # defaulting to `0` if not set.
    gamePlayed = session.get("gamePlayed", 0)

    # UPDATING SESSION DATA

    # Updates the number of games played in the session.
    session["gamePlayed"] = gamePlayed + 1

    # Updates the high score in the sessing,
    # using `max` function to compare the received `score`
    # with the current `highScore`
    session["highScore"] = max(score, highScore)

    return jsonify(
        {"gamePlayed": session["gamePlayed"], "highScore": session["highScore"]}
    )
