"""
Word lists for Wordle game.

Two lists are loaded:
- SOLUTIONS: ~2,300 common words that can be the secret word
- VALID_GUESSES: ~15,000 words accepted as guesses (includes all solutions)

Both are stored as sets for O(1) lookup.
"""

from pathlib import Path

WORDS_DIR = Path(__file__).parent / "words"


def load_words(filename):
    """Load words from a text file into a set."""
    filepath = WORDS_DIR / filename
    with open(filepath) as f:
        return {word.strip().lower() for word in f if word.strip()}


# Load word lists at module import (once, at startup)
SOLUTIONS = load_words("solutions.txt")
VALID_GUESSES = load_words("valid_guesses.txt")

# Ensure all solutions are also valid guesses
VALID_GUESSES = VALID_GUESSES | SOLUTIONS
