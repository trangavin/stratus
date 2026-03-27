"""
Wordle Flask Application

This file runs the web server. You don't need to edit this file.
Your game logic goes in game.py!
"""

import random

from flask import Flask, jsonify, render_template, request, session
from game import check_guess, is_valid_guess, is_winner
from words import SOLUTIONS, VALID_GUESSES

# Convert solutions to list for random.choice()
SOLUTIONS_LIST = list(SOLUTIONS)

app = Flask(__name__)
app.secret_key = "wordle-secret-key-change-in-production"


@app.route("/")
def index():
    """Show the game page."""
    return render_template("index.html")


@app.route("/new-game", methods=["POST"])
def new_game():
    """Start a new game with a random word."""
    session["secret_word"] = random.choice(SOLUTIONS_LIST)
    session["attempts"] = 0
    session["max_attempts"] = 6
    session["game_over"] = False
    return jsonify({"success": True})


@app.route("/guess", methods=["POST"])
def make_guess():
    """Process a guess and return feedback."""
    # Check if game is already over
    if session.get("game_over", False):
        return jsonify({"error": "Game is over. Start a new game!"}), 400

    # Get the guess from the request
    data = request.get_json()
    guess = data.get("guess", "").lower().strip()

    # Get the secret word
    secret_word = session.get("secret_word")
    if not secret_word:
        return jsonify({"error": "No game in progress. Start a new game!"}), 400

    # Validate the guess using the student's function
    if not is_valid_guess(guess, VALID_GUESSES):
        return jsonify({"valid": False, "error": "Not a valid word"})

    # Check the guess using the student's function
    feedback = check_guess(guess, secret_word)

    # Increment attempts
    session["attempts"] = session.get("attempts", 0) + 1

    # Check for win using the student's function
    won = is_winner(guess, secret_word)

    # Check for loss
    lost = session["attempts"] >= session["max_attempts"] and not won

    # Mark game as over if won or lost
    if won or lost:
        session["game_over"] = True

    return jsonify(
        {
            "valid": True,
            "feedback": feedback,
            "won": won,
            "lost": lost,
            "attempts": session["attempts"],
            "secret_word": secret_word if lost else None,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
