"""
Task 1: Hangman Game
--------------------
A simple text-based Hangman game where the player guesses a word one letter at a time.
Features:
- Predefined list of 5 words
- Maximum 6 incorrect guesses
- Clear console-based UI with text/ASCII hangman stages
- Tracks guessed letters, validates input, and provides feedback
"""

import random

# Visual hangman stages for 0 to 6 incorrect guesses
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def display_word_progress(secret_word, guessed_letters):
    """
    Returns a string showing correctly guessed letters and underscores for hidden letters.
    Example: 'p _ t h _ n'
    """
    display_letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_letters.append(letter)
        else:
            display_letters.append("_")
    return " ".join(display_letters)


def play_hangman():
    """
    Runs a single session of the Hangman game.
    """
    # 1. Predefined list of 5 words
    words = ["python", "guitar", "orange", "planet", "stream"]

    # Select a random word from the list
    secret_word = random.choice(words)

    # Game configuration and state variables
    max_incorrect_guesses = 6
    incorrect_guesses = 0
    guessed_letters = []

    print("\n" + "=" * 40)
    print("      WELCOME TO HANGMAN GAME!      ")
    print("=" * 40)
    print("Rules:")
    print("- Guess the secret word one letter at a time.")
    print(f"- You are allowed a maximum of {max_incorrect_guesses} incorrect guesses.")
    print("=" * 40)

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display current hangman visual
        print(HANGMAN_STAGES[incorrect_guesses])

        # Display current word status
        current_display = display_word_progress(secret_word, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        
        # Display already guessed letters
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        else:
            print("Guessed letters: None")

        # Prompt player for input
        user_input = input("\nEnter a letter: ").strip().lower()

        # Input validation
        if len(user_input) != 1 or not user_input.isalpha():
            print(">> Invalid input! Please enter a single alphabetical letter.\n")
            continue

        if user_input in guessed_letters:
            print(f">> You already guessed '{user_input}'. Try a different letter.\n")
            continue

        # Add guess to the list of guessed letters
        guessed_letters.append(user_input)

        # Check if guess is in the secret word
        if user_input in secret_word:
            print(f">> Good job! '{user_input}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f">> Sorry! '{user_input}' is NOT in the word.\n")

        # Check win condition immediately after processing guess
        all_revealed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_revealed = False
                break

        if all_revealed:
            print(HANGMAN_STAGES[incorrect_guesses])
            print(f"Word: {display_word_progress(secret_word, guessed_letters)}")
            print("\n" + "*" * 40)
            print(f" Congratulations! You guessed the word: '{secret_word}'")
            print("*" * 40)
            return

    # If loop ends, the player reached 6 incorrect guesses
    print(HANGMAN_STAGES[incorrect_guesses])
    print("=" * 40)
    print("             GAME OVER!             ")
    print("=" * 40)
    print(f"You ran out of guesses. The secret word was: '{secret_word}'\n")


def main():
    while True:
        play_hangman()
        replay = input("Would you like to play again? (y/n): ").strip().lower()
        if replay != 'y' and replay != 'yes':
            print("\nThank you for playing Hangman! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
