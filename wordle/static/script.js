/**
 * Wordle Game Frontend
 * Handles keyboard input, display updates, and communication with the backend.
 */

// Game state
let currentRow = 0;
let currentCol = 0;
let gameOver = false;

// DOM elements
const board = document.getElementById('board');
const message = document.getElementById('message');
const keyboard = document.getElementById('keyboard');
const newGameBtn = document.getElementById('new-game');

// Initialize game on page load
document.addEventListener('DOMContentLoaded', startNewGame);

// New game button
newGameBtn.addEventListener('click', startNewGame);

// Physical keyboard input
document.addEventListener('keydown', handleKeyPress);

// Virtual keyboard input
keyboard.addEventListener('click', (e) => {
    if (e.target.classList.contains('key')) {
        const key = e.target.dataset.key;
        handleInput(key);
    }
});

/**
 * Start a new game
 */
async function startNewGame() {
    try {
        const response = await fetch('/new-game', { method: 'POST' });
        const data = await response.json();

        if (data.success) {
            resetBoard();
            showMessage('');
        }
    } catch (error) {
        showMessage('Error starting game', 'error');
    }
}

/**
 * Reset the board for a new game
 */
function resetBoard() {
    currentRow = 0;
    currentCol = 0;
    gameOver = false;

    // Clear all tiles
    const tiles = document.querySelectorAll('.tile');
    tiles.forEach(tile => {
        tile.textContent = '';
        tile.className = 'tile';
    });

    // Reset keyboard colors
    const keys = document.querySelectorAll('.key');
    keys.forEach(key => {
        key.classList.remove('correct', 'misplaced', 'wrong');
    });
}

/**
 * Handle physical keyboard input
 */
function handleKeyPress(e) {
    if (gameOver) return;

    const key = e.key.toUpperCase();

    if (key === 'ENTER') {
        handleInput('ENTER');
    } else if (key === 'BACKSPACE') {
        handleInput('BACKSPACE');
    } else if (/^[A-Z]$/.test(key)) {
        handleInput(key);
    }
}

/**
 * Handle input from keyboard (physical or virtual)
 */
function handleInput(key) {
    if (gameOver) return;

    if (key === 'ENTER') {
        submitGuess();
    } else if (key === 'BACKSPACE') {
        deleteLetter();
    } else if (/^[A-Z]$/.test(key) && currentCol < 5) {
        addLetter(key);
    }
}

/**
 * Add a letter to the current position
 */
function addLetter(letter) {
    const row = board.children[currentRow];
    const tile = row.children[currentCol];

    tile.textContent = letter;
    tile.classList.add('filled');
    currentCol++;
}

/**
 * Delete the last letter
 */
function deleteLetter() {
    if (currentCol > 0) {
        currentCol--;
        const row = board.children[currentRow];
        const tile = row.children[currentCol];

        tile.textContent = '';
        tile.classList.remove('filled');
    }
}

/**
 * Submit the current guess
 */
async function submitGuess() {
    if (currentCol !== 5) {
        showMessage('Not enough letters', 'error');
        shakeRow();
        return;
    }

    const row = board.children[currentRow];
    let guess = '';
    for (let i = 0; i < 5; i++) {
        guess += row.children[i].textContent;
    }

    try {
        const response = await fetch('/guess', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ guess: guess })
        });

        const data = await response.json();

        if (data.error) {
            showMessage(data.error, 'error');
            shakeRow();
            return;
        }

        if (!data.valid) {
            showMessage('Not in word list', 'error');
            shakeRow();
            return;
        }

        // Reveal the feedback with animation
        revealFeedback(data.feedback);

        // Check for win/loss
        if (data.won) {
            setTimeout(() => {
                showMessage('You won!', 'success');
                gameOver = true;
            }, 1600);
        } else if (data.lost) {
            setTimeout(() => {
                showMessage(`Game over! The word was: ${data.secret_word.toUpperCase()}`, 'info');
                gameOver = true;
            }, 1600);
        } else {
            // Move to next row
            currentRow++;
            currentCol = 0;
        }

    } catch (error) {
        showMessage('Error submitting guess', 'error');
    }
}

/**
 * Reveal feedback with flip animation
 */
function revealFeedback(feedback) {
    const row = board.children[currentRow];

    feedback.forEach((result, index) => {
        setTimeout(() => {
            const tile = row.children[index];
            tile.classList.add(result);

            // Update keyboard
            const letter = tile.textContent;
            updateKeyboard(letter, result);
        }, index * 300);
    });
}

/**
 * Update keyboard key colors
 */
function updateKeyboard(letter, result) {
    const key = document.querySelector(`.key[data-key="${letter}"]`);
    if (!key) return;

    // Only upgrade colors: wrong -> misplaced -> correct
    if (result === 'correct') {
        key.classList.remove('misplaced', 'wrong');
        key.classList.add('correct');
    } else if (result === 'misplaced' && !key.classList.contains('correct')) {
        key.classList.remove('wrong');
        key.classList.add('misplaced');
    } else if (result === 'wrong' && !key.classList.contains('correct') && !key.classList.contains('misplaced')) {
        key.classList.add('wrong');
    }
}

/**
 * Shake the current row (for invalid input)
 */
function shakeRow() {
    const row = board.children[currentRow];
    row.classList.add('shake');
    setTimeout(() => row.classList.remove('shake'), 300);
}

/**
 * Show a message to the user
 */
function showMessage(text, type = '') {
    message.textContent = text;
    message.className = 'message';
    if (type) {
        message.classList.add(type);
    }
}
