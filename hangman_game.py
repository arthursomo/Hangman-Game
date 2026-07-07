import random

def hangman_game():
    words = ['python', 'programming', 'computer', 'keyboard', 'variable']
    secret_word = random.choice(words)
    revealed_letters = ['_'] * len(secret_word)
    attempts = 6
    guessed_letters = []

    print('Hangman Game!')

    while attempts > 0 and '_' in revealed_letters:
        print('\nWord: ' + ' '.join(revealed_letters))
        print(f'Attempts left: {attempts}')

        letter = input('Enter a letter: ').lower()

        if letter in guessed_letters:
            print('You already tried that letter.')
            continue

        guessed_letters.append(letter)

        if letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    revealed_letters[i] = letter
        else:
            attempts -= 1
            print('Wrong letter!')

    if '_' not in revealed_letters:
        print(f'\nCongratulations! You guessed the word: {secret_word}')
    else:
        print(f'\nYou lost! The word was: {secret_word}')

hangman_game()
