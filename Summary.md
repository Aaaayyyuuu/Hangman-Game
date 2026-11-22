# Summary: Hangman Game (PS No. 51)

**Name:** Ayush Prasad | **ERP:** RU-26-01094 | **Section:** 1L

## Project overview

The assignment was to build a word guessing game. The player guesses the letters of a hidden word one at a time with a limit of 6 wrong guesses. The word is chosen randomly, letters are not case-sensitive, invalid input must be rejected, and a repeated letter must not use up an attempt.

I built it in Python with four functions:
- `choose_word()` picks the secret word (always `python` in test mode).
- `show_progress()` builds the display such as `p y _ _ _ _`.
- `is_won()` returns `True` only when every letter has been guessed.
- `play()` runs the game loop, validation, scoring and final result.

## Difficulties faced and how I solved them

| Difficulty | How I solved it |
| --- | --- |
| I was new to programming and did not understand how loops and functions work together | I learned one concept at a time (variables, `if`, `while`, `for`, functions) and typed and ran small examples before writing the full game |
| A repeated letter should not cost an attempt | I check `if guess in guessed` before changing the wrong counter and use `continue` to go back to the top of the loop |
| Input like `1`, `ab` or an empty entry should be rejected | I check `len(guess) != 1` for length and `not guess.isalpha()` for non-letters |
| Capital and small letters should be treated the same | I convert every guess with `.lower()` (and `.strip()` removes extra spaces) |
| A random word makes the test cases hard to check | I added `TEST_MODE`, which fixes the word to `python` |
| Uploading to GitHub failed because the repository already had a README | I uploaded the files through the GitHub website instead |

## Test cases

The secret word was fixed to `python` (`TEST_MODE = True`).

| No. | Type | Guesses entered | Expected result | Result |
| --- | --- | --- | --- | --- |
| 1 | Normal | p, y, t, h, o, n | You won, 0/6 wrong | Pass |
| 2 | Boundary | a, b, c, d, e, f | Game Over, 6/6 wrong | Pass |
| 3 | Invalid input | 1, ab, p, p | Invalid input twice, p Correct, then already guessed with no attempt lost | Pass |
| 4 | Mixed | p, z, y, x, t, h, o, n | You won, 2/6 wrong | Pass |

### Screenshots

**Test case 1: Normal** (p, y, t, h, o, n)



**Test case 2: Boundary** (a, b, c, d, e, f)



**Test case 3: Invalid input** (1, ab, p, p)



**Test case 4: Mixed** (p, z, y, x, t, h, o, n)



## What I learned

How to break a problem into steps, use a loop that repeats until a condition is met, validate user input, split code into functions, and test a program with fixed inputs.

