# Hangman Game

**Name:** Ayush Prasad
**ERP / Roll No.:** RU-26-01094
**Class / Section:** B.Tech CSE, 1st Semester, Section L
**Problem Statement No.:** 51
**Course:** Programming Fundamentals and Logic Building Using Python (RU-100-01-0021)

## About the project

A console-based Hangman game written in Python 3. The computer picks a secret word at random from a word list. The player guesses one letter at a time. Correct letters appear in their positions and unguessed letters show as underscores. The player is allowed **6 wrong guesses**.

Features:
- Random word chosen from a list
- Guesses are not case-sensitive
- Invalid input (numbers, symbols, empty input, more than one character) is rejected
- A repeated letter is ignored and does not cost an attempt
- The game ends with a win when the whole word is guessed, or Game Over after 6 wrong guesses
- A `TEST_MODE` setting fixes the secret word to `python` so the test cases can be checked

## Concepts used

Variables and data types, input/output, conditionals (`if`/`else`), loops (`while`, `for`), `continue`, functions, the `random` module, strings and string methods, lists.

## How to run

1. Install Python 3 from python.org.
2. Download `Hangman.py` from this repository.
3. Open a terminal in the folder containing the file and run:

```
python Hangman.py
```

No extra libraries are needed. `random` comes with Python.

To run the test cases, change `TEST_MODE = False` to `TEST_MODE = True` near the top of the file. The secret word is then always `python`.

## Sample output

```
=== HANGMAN ===
Guess the word. You get 6 wrong guesses.

Progress: _ _ _ _ _ _
Guess a letter: p
p: Correct
Progress: p _ _ _ _ _
Guess a letter: z
z: Wrong (1/6)
```


## Files

- `Hangman.py`: the game
- `README.md`: this file
- `Summary.md`: project overview, difficulties faced and test case screenshots


