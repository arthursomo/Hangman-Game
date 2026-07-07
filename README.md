# Hangman Game
 
A python hangman game where the player tries to guess a hidden word letter by letter.
 
## What it does
 
The program randomly picks a secret word from a predefined list and hides it using underscores (`_`). The player guesses one letter at a time:
- If the letter is in the word, it gets revealed in all the positions where it appears
- If the letter is not in the word, the player loses one attempt
- The game ends when the player either reveals the full word or runs out of attempts (6 by default)
The game also prevents the player from guessing the same letter twice and is case-insensitive (it doesn't matter if you type uppercase or lowercase).
 
## How to run
 
```bash
python hangman_game.py
```
 
## Example usage
 
```
Hangman Game!
 
Word: _ _ _ _ _ _
Attempts left: 6
Enter a letter: o
Word: _ _ _ _ o _
Attempts left: 6
Enter a letter: z
Wrong letter!
Word: _ _ _ _ o _
Attempts left: 5
Enter a letter: y
...
 
Congratulations! You guessed the word: python
```
