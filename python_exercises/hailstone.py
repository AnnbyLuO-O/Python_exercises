"""
File: hailstone.py
Name: Annby
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    :param n: int
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:  # even
            print(str(n)+' is even, so I take half: ', end='')
            n = n // 2

        else:  # odd
            print(str(n) + ' is odd, so I make 3*n+1: ', end='')
            n = 3 * n + 1
        print(str(n))
    print('It took '+str(count)+' step to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
