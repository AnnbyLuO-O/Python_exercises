"""
File: number_checker.py
Name: Annby
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT: int = -100


def main():
    """
    :param n: int
    """
    print('Welcome to the number checker!')
    n = int(input('n: '))
    ans = 0
    for i in range(1, n):
        if n % i == 0:
            ans += i
    while True:
        if n == EXIT:
            print('Have a good one!')
            break
        if ans > n:
            print(str(n), end='')
            print(' is an abundant number')
        if ans < n:
            print(str(n), end='')
            print(' is a deficient number')
        if ans == n:
            print(str(n), end='')
            print(' is a Perfect number')
        n = int(input('n: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
