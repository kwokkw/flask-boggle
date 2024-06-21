from boggle import Boggle
from flask import (
    Flask,
    render_template,
    session,
    request,
    redirect,
    flash,
    jsonify,
    json,
)
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "play"
app.debug = True

# Install flask debug toolbar
debug = DebugToolbarExtension(app)

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


@app.route("/", methods=["GET"])
def home_page():
    game_board = boggle_game.make_board()
    session["game_board"] = game_board
    return render_template("index.html", game_board=game_board)


# TODO
@app.route("/submit-guess", methods=["POST"])
def submit_guess():
    # take the form value and check if it is a valid word in the dictionary using the words variable in your app.py
    guess = request.json["guess"]
    game_board = session["game_board"]
    response = boggle_game.check_valid_word(game_board, guess)

    # UNABLE TO SEE PRINT STATEMENT IN GIT BASH - do not understand the behavior
    print("***********************")
    print(guess)
    print("***********************")

    # `jsonify` converts Python data into a JSON format that can be sent and understood by JavaScript.
    return jsonify({"result": response})
