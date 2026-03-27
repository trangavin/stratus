"""
Wordle Game Logic

This is the file you will edit! Implement the functions below to make the game work.
"""


def is_valid_guess(guess, valid_words):
    """
    Check if a guess is valid.

    A valid guess:
    - Has exactly 5 letters
    - Is in valid_words

    Args:
        guess: The player's guess (a string)
        valid_words: A collection of valid 5-letter words

    Returns:
        True if the guess is valid, False otherwise

    Hint:
        Use `in` to check if something is in a collection:
        "apple" in valid_words  -> True or False
    """
    # TODO: Fix this function!
    # Right now it accepts ANY 5-letter guess, even fake words like "zzzzz"
    return len(guess) == 5


def check_guess(guess, secret_word):
    """
    Compare the guess to the secret word and return feedback.

    For each letter in the guess, determine if it is:
    - "correct" = right letter in the right position (green)
    - "misplaced" = right letter but wrong position (yellow)
    - "wrong" = letter not in the word (gray)

    Args:
        guess: The player's 5-letter guess
        secret_word: The secret 5-letter word to guess

    Returns:
        A list of 5 strings, one for each letter: "correct", "misplaced", or "wrong"

    Examples:
        check_guess("crane", "crane") -> ["correct", "correct", "correct", "correct", "correct"]
        check_guess("brain", "crane") -> ["wrong", "correct", "correct", "wrong", "correct"]
        check_guess("apple", "peace") -> ["misplaced", "misplaced", "wrong", "wrong", "correct"]
    """
    # TODO: Fix this function!
    # Right now it marks everything as "wrong" (gray)
    return ["wrong", "wrong", "wrong", "wrong", "wrong"]


def is_winner(guess, secret_word):
    """
    Check if the player has won.

    The player wins if their guess exactly matches the secret word.

    Args:
        guess: The player's guess
        secret_word: The secret word

    Returns:
        True if the guess matches the secret word, False otherwise

    Examples:
        is_winner("crane", "crane") -> True
        is_winner("brain", "crane") -> False
    """
    # TODO: Fix this function!
    # Right now you can never win
    return False
