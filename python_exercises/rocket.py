"""
File: rocket.py
Name: Annby
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 5


def main():
    """
    that's build a rocket! To Infinity and Beyond!
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(1, SIZE+1):  # start from 1 or will get a blank line above the head of the rocket.
        for j in range(SIZE-i+1):
            print(' ', end='')
        for j in range(i):
            print('/', end='')
        for j in range(i):
            print('\\', end='')
        print('')


def belt():
    print('+', end='')
    for i in range(SIZE):
        print('==', end='')
    print('+', end='')
    print('')


def upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(i+1):
            print('/\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        print('|', end='')
        print('')


def lower():
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\\/', end='')
        for j in range(i):
            print('.', end='')
        print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
