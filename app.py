from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "play"

# Install flask debug toolbar
debug = DebugToolbarExtension(app)

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


@app.route("/", methods=["GET"])
def home_page():
    game_board = boggle_game.make_board()
    session["game_board"] = game_board
    return render_template("index.html", game_board=game_board)


@app.route("/submit-guess", methods=["POST"])
def submit():
    #     # take the form value and check if it is a valid word in the dictionary using the words variable in your app.py

    return render_template("submit-guess.html")
