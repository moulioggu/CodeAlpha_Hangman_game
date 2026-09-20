# CodeAlpha_Hangman_game
Classic word-guessing Hangman game developed in Python as part of the CodeAlpha Internship.
# Hangman Game 🎮

A command-line implementation of the classic word-guessing game **Hangman**, developed as part of the **CodeAlpha Internship** program.

---

## 📌 Overview

The Hangman Game is an interactive terminal-based application where players attempt to discover a hidden word by guessing one letter at a time within a limited number of attempts. For every incorrect guess, the program updates the visual hangman state and decreases remaining lives.

---

## ✨ Features

- **Random Word Selection:** Picks words dynamically from an internal word pool.
- **ASCII Art Visuals:** Step-by-step graphical hangman progression for wrong guesses.
- **Input Validation:** Prevents penalties for duplicate guesses, numbers, or multi-character entries.
- **Dynamic Display:** Shows revealed letters, masked blanks (`_`), and a tracker of already-guessed letters.
- **Clear Win/Loss Conditions:** Displays the hidden word upon game over and announces round victories.

---

## 🛠️ Built With

- **Language:** Python 3
- **Libraries Used:** Standard Library (`random`, `os`) — *no external packages required*

---

## 📂 Project Structure

```text
├── hangman.py          # Main game loop and logic
└── README.md           # Project documentation
