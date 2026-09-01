# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and conditionals. You will practice string manipulation, iteration, and game logic by creating an interactive game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description

Create a complete Hangman game that runs in the terminal. The game should randomly select a word from a list and allow the player to guess letters one at a time. Players win by guessing all letters before their attempts run out, and lose when they exhaust their attempts without completing the word.

#### Requirements

Completed program should:

- Randomly select a word from a predefined list of words
- Display the current game state showing guessed letters and blanks (e.g., `_ _ _ _`)
- Accept letter guesses from the player via user input
- Track and display the number of incorrect guesses remaining
- Validate input to reject non-letter characters or duplicate guesses
- End the game with a win message when the player guesses all letters
- End the game with a loss message when the player runs out of attempts
- Show the hidden word when the player loses
