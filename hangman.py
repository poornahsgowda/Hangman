import random

# Word Categories
categories = {
    'Animals': ['elephant', 'giraffe', 'kangaroo', 'zebra'],
    'Countries': ['canada', 'brazil', 'france', 'india'],
    'Movies': ['inception', 'avatar', 'gladiator', 'titanic']
}

# Hangman ASCII Art Stages
stages = [
    """
      -----
      |   |
          |
          |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    --------
    """
]

# Function to choose word category
def choose_category():
    print("Select a category:")
    for i, category in enumerate(categories.keys()):
        print(f"{i+1}. {category}")
    choice = int(input("Enter the number of your choice: ")) - 1
    category = list(categories.keys())[choice]
    return random.choice(categories[category]), category

# Function to choose difficulty level
def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (10 incorrect guesses)")
    print("2. Medium (7 incorrect guesses)")
    print("3. Hard (5 incorrect guesses)")
    level = int(input("Enter the number of your choice: "))
    if level == 1:
        return 10
    elif level == 2:
        return 7
    else:
        return 5

# Function for providing hint
def provide_hint(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            print(f"Here's a hint: One of the letters is '{letter}'")
            return letter

# Multiplayer mode setup (optional)
def multiplayer_mode():
    players = int(input("Enter number of players: "))
    scores = [0] * players
    current_player = 0
    return players, scores, current_player

# Main game loop
def play_hangman():
    word, category = choose_category()
    allowed_guesses = choose_difficulty()
    guessed_letters = []
    incorrect_guesses = 0
    hint_used = False

    print(f"\nYou chose the category: {category}")
    print(f"The word has {len(word)} letters.")
    
    while incorrect_guesses < allowed_guesses:
        print(stages[incorrect_guesses])
        print("Guessed letters:", " ".join(guessed_letters))
        
        # Display the word with guessed letters or underscores
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word:", " ".join(display_word))

        if "_" not in display_word:
            print("Congratulations, you guessed the word!")
            break

        guess = input("Guess a letter or type 'hint' for a hint: ").lower()

        if guess == "hint" and not hint_used:
            hint = provide_hint(word, guessed_letters)
            guessed_letters.append(hint)
            hint_used = True
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                print("Correct!")
            else:
                guessed_letters.append(guess)
                incorrect_guesses += 1
                print("Incorrect!")
        else:
            print("Invalid input, please guess a single letter.")

    if incorrect_guesses == allowed_guesses:
        print(stages[-1])
        print(f"Sorry, you lost! The word was '{word}'.")

# Start the game
play_hangman()
