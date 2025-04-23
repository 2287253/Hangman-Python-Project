import random
import os

# ASCII art for hangman stages
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

# Word categories and their words
WORDS = {
    "Animals": ["elephant", "giraffe", "kangaroo", "penguin", "dolphin"],
    "Fruits": ["banana", "strawberry", "watermelon", "pineapple", "blueberry"],
    "Countries": ["canada", "brazil", "japan", "australia", "germany"],
    "Sports": ["basketball", "football", "tennis", "swimming", "volleyball"]
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_word(category):
    return random.choice(WORDS[category])

def display_game_state(word, guessed_letters, attempts_left):
    clear_screen()
    print(HANGMAN_STAGES[6 - attempts_left])
    print("\nWord:", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
    print("\nGuessed letters:", " ".join(sorted(guessed_letters)))
    print(f"Attempts left: {attempts_left}")

def play_hangman():
    print("Welcome to Hangman!")
    print("\nCategories available:")
    for i, category in enumerate(WORDS.keys(), 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("\nSelect a category (1-4): ")) - 1
            if 0 <= choice < len(WORDS):
                category = list(WORDS.keys())[choice]
                break
            print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")

    word = get_random_word(category)
    guessed_letters = set()
    attempts_left = 6
    game_over = False

    while not game_over:
        display_game_state(word, guessed_letters, attempts_left)
        
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts_left -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            display_game_state(word, guessed_letters, attempts_left)
            print("\nCongratulations! You won!")
            print(f"The word was: {word}")
            game_over = True
        
        if attempts_left == 0:
            display_game_state(word, guessed_letters, attempts_left)
            print("\nGame Over! You lost!")
            print(f"The word was: {word}")
            game_over = True

def main():
    while True:
        play_hangman()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
