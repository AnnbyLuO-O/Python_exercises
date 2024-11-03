"""
File: narcissistic_checker.py
Name:Annby
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT: int = -100


def main():
    """
    ⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠
    The most, most, most, most, most, most difficult question.
    """
    print('Welcome to the narcissistic number checker!')
    while True:
        user_input = input('n: ')
        if user_input == str(EXIT):
            print('Have a good one!')
            break
        else:
            n = int(user_input)  # convert the input number to an integer
            x = len(str(n))  # word length
            sum_val = 0
            for i in str(n):
                sum_val += int(i) ** x
            if sum_val == n:
                print(str(n), end='')
                print(' is a narcissistic number')
            else:
                print(str(n), end='')
                print(' is not a narcissistic number')


if __name__ == '__main__':
    main()
