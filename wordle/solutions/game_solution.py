"""
Wordle Game Logic - SOLUTION FILE

This is the answer key. Don't share with students!
"""


def is_valid_guess(guess, valid_words):
    """
    Check if a guess is valid.
    """
    return len(guess) == 5 and guess in valid_words


def check_guess(guess, secret_word):
    """
    Compare the guess to the secret word and return feedback.
    """
    result = []

    for i in range(5):
        if guess[i] == secret_word[i]:
            result.append("correct")
        elif guess[i] in secret_word:
            result.append("misplaced")
        else:
            result.append("wrong")

    return result


def is_winner(guess, secret_word):
    """
    Check if the player has won.
    """
    return guess == secret_word
