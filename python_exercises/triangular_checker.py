"""
File: triangular_checker.py
Name:Annby
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
import math
EXIT: int = -100


def main():
    """
    :param n: int
    """
    print('Welcome to the triangular number checker !')
    n = int(input('n: '))

    while True:
        d = (8 * n + 1)  # Discriminant: (math.sqrt(d))/2 - 1/2
        if n == EXIT:
            print('Have a good one!')
            break
        if ((math.sqrt(d))/2 - 1/2) == int(((math.sqrt(d))/2 - 1/2)):
            print(str(n), end='')
            print(' is a triangular number.')
            n = int(input('n: '))
        else:
            print(str(n), end='')
            print(' is not a triangular number.')
            n = int(input('n: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
