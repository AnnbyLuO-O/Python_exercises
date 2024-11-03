"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This is a word guessing game. There are 7 chances; if you answer correctly within 7 attempts, you win.
    """
    word = random_word()
    spaces = ['_'] * len(word)
    guessed_letters = set()  # record list
    remaining_turns = N_TURNS

    while remaining_turns > 0:
        print('The word looks: ' + ' '.join(spaces))
        guess = input('Your guess: ').upper()

        if not guess.isalpha() or len(guess) != 1:
            print('Illegal format. Please enter a single letter.')
            continue  # error input

        if guess in guessed_letters:
            print(f'You already guessed the letter \'{guess}\'. Try again.')
            continue  # have guessed the same answer

        guessed_letters.add(guess)  # record
        correct_guess = False  # record correct or not

        for i in range(len(word)):
            ch = word[i]
            if ch == guess:
                correct_guess = True
                spaces[i] = guess  # correct

        if correct_guess:
            print('You are correct!')
        else:
            print(f'There is no \'{guess}\' in the word.')
            remaining_turns -= 1

        # check
        if all(letter in guessed_letters for letter in set(word)):
            print('You win!')
            break

        print('You have ' + str(remaining_turns) + ' wrong guesses left!')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
