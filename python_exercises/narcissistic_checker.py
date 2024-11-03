"""
File: extension4_narcissistic_checker.py
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

    # note
    # n = int(input('n: '))
    # while True:
    #     if n == EXIT:
    #         print('Have a good one!')
    #         break
    #     else:
    #         x = len(str(n))  # how many digit
    #         k = 0
    #         for i in str(n):
    #             k += int(n) ** x
    #             if sum == int(i):
    #                 print(str(n), end='')
    #                 print(' is a narcissistic number')
    #             else:
    #                 print(str(n), end='')
    #                 print(' is not a narcissistic number')
    #                 n = int(input('n: '))

        # else:
        #     for i in range(100, n+1):
        #         power = len(str(n))  # the power of n
        #         total = 0  # to sum
        #         digit = 0  # last digits of the number
        #         while True:
        #             a = n % 10
        #             total += digit ** n
        #             if total == n:
        #                 print(str(n), end='')
        #                 print(' is a narcissistic number')
        #             else:
        #                 print(str(n), end='')
        #                 print(' is not a narcissistic number')
        #                 n = int(input('n: '))

        # sum = 0
        # i = n
        # while i > 0:
        #     n1 = i % 10
        #     sum += n1 ** n
        #     i //= 10
        # if n == sum:
        #     print(str(n), end='')
        #     print(' is a narcissistic number')
        #     n = int(input('n: '))
        # else:
        #     print(str(n), end='')
        #     print(' is not a narcissistic number')
        #     n = int(input('n: '))

        # if 1000 > n > 100:
        #     for i in range(100, 1000):
        #         n1 = int(n // 100)
        #         n2 = int(n // 10)
        #         n3 = int(n % 10)
        #         s1 = n1 ** 3 + n2 ** 3 + n3 ** 3
        #         s2 = n1 * 100 + n2 * 10 + n3
        #         if s1 == s2:
        #             print(str(n), end='')
        #             print(' is a narcissistic number')
        #             n = int(input('n: '))
        # elif 10000 > n > 1000:
        #     for i in range(1000, 10000):
        #         n4 = int(n // 1000)
        #         n5 = int(n // 100)
        #         n6 = int(n // 10)
        #         n7 = int(n % 10)
        #         s3 = n4 ** 4 + n5 ** 4 + n6 ** 4 + n7 ** 4
        #         s4 = n4 * 1000 + n5 * 100 + n6 * 10 + n7
        #         if s3 == s4:
        #             print(str(n), end='')
        #             print(' is a narcissistic number')
        #             n = int(input('n: '))
        # elif 100000 > n > 10000:
        #     for i in range(10000, 100000):
        #         n8 = int(n // 10000)
        #         n9 = int(n // 1000)
        #         n10 = int(n // 100)
        #         n11 = int(n // 10)
        #         n12 = int(n % 10)
        #         s5 = n8 ** 5 + n9 ** 5 + n10 ** 5 + n11 ** 5 + n12 ** 5
        #         s6 = n8 * 10000 + n9 * 1000 + n10 * 100 + n11 * 10 + n12
        #         if s5 == s6:
        #             print(str(n), end='')
        #             print(' is a narcissistic number')
        #             n = int(input('n: '))
        # else:
        #     print(str(n), end='')
        #     print(' is not a narcissistic number')
        #     n = int(input('n: '))


if __name__ == '__main__':
    main()
