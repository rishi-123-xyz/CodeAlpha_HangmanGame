# Task 1: Hangman Game

A simple, interactive text-based Hangman game written in Python where the player guesses a secret word one letter at a time.

---

## 📋 Features & Specifications

- **Predefined Word List**: Uses a list of 5 predefined words (`"python"`, `"guitar"`, `"orange"`, `"planet"`, `"stream"`).
- **Incorrect Guess Limit**: The player is allowed a maximum of **6 incorrect guesses** before losing.
- **Visual ASCII Gallows**: Dynamic ASCII art updates with each incorrect guess showing the progression of the hangman.
- **Progress Tracking**: Shows unguessed letters as underscores (`_`) and reveals correctly guessed letters in their proper positions.
- **Input Validation**:
  - Validates that inputs are single alphabetical characters.
  - Warns the player if a letter was already guessed without penalizing attempts.
  - Case-insensitive (accepts both uppercase and lowercase letters).
- **Replay Option**: Asks the player if they want to play another round when the game ends.

---

## 💡 Key Programming Concepts Used

| Concept | Implementation in Code |
| :--- | :--- |
| **`random` module** | Used `random.choice(words)` to randomly pick a secret word each round. |
| **`while` loop** | Used `while incorrect_guesses < max_incorrect_guesses:` to drive the turn-by-turn game loop and replay loop. |
| **`if-else` statements** | Evaluates input validity, checks whether a letter is in the word, tracks repeated guesses, and triggers win/loss conditions. |
| **Strings** | Handles word manipulation, case-insensitivity (`.strip().lower()`), and user input processing. |
| **Lists** | Stores the 5 predefined words, the list of guessed letters, and the ASCII hangman stages. |

---

## 🚀 How to Run the Game

1. Open your terminal or PowerShell in this project folder:
   ```powershell
   cd "c:\Users\kumar\OneDrive\Desktop\task 1"
   ```

2. Run the game using Python:
   ```powershell
   python hangman.py
   ```
   *(Or if using the full path: `& "C:\Users\kumar\AppData\Local\Programs\Python\Python312\python.exe" hangman.py`)*

3. Follow the on-screen prompts to enter letters and guess the secret word!
