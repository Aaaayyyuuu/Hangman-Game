import random

# ---------- Settings ----------
WORDS = ["python", "program", "computer", "keyboard", "variable",
         "function", "science", "network", "database", "algorithm"]
MAX_WRONG = 6          # number of wrong guesses allowed
TEST_MODE = False      # set to True to always use the secret word 'python'


# ---------- Functions ----------
def choose_word():
    """Pick the secret word (fixed to 'python' in test mode)."""
    if TEST_MODE:
        return "python"
    return random.choice(WORDS)


def show_progress(secret, guessed):
    """Return the word with unguessed letters shown as underscores."""
    display = ""
    for letter in secret:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "
    return display.strip()


def is_won(secret, guessed):
    """Return True if every letter of the secret word has been guessed."""
    for letter in secret:
        if letter not in guessed:
            return False
    return True


def play():
    """Run one full game of Hangman."""
    secret = choose_word()
    guessed = []       # all valid letters the player has tried
    wrong = 0          # count of wrong guesses

    print("=== HANGMAN ===")
    print(f"Guess the word. You get {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG and not is_won(secret, guessed):
        print("Progress:", show_progress(secret, guessed))
        guess = input("Guess a letter: ").strip().lower()   # not case-sensitive

        # 1) Validate: must be exactly one alphabet letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter.")
            continue

        # 2) Repeated letter: no attempt is lost
        if guess in guessed:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        # 3) Valid new guess
        guessed.append(guess)
        if guess in secret:
            print(f"{guess}: Correct")
        else:
            wrong = wrong + 1
            print(f"{guess}: Wrong ({wrong}/{MAX_WRONG})")

    # ---------- Result ----------
    print("Progress:", show_progress(secret, guessed))
    if is_won(secret, guessed):
        print(f"You won! The word was {secret}.")
    else:
        print(f"Game Over! The word was {secret}.")
    print(f"Wrong guesses: {wrong}/{MAX_WRONG}")


# ---------- Program starts here ----------
play()