"""
File: name_sq.py (extension)
Name: 
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    ##### left
    """
    print('This program prints a name in a square pattern !')
    name = input(str('Name: '))
    print(name)  # up
    for i in range(1, len(name) - 1):  # right
        print(name[::-1][i] + " " * (len(name) - 2) + name[::-1][i])

    print(name[::-1])  # down


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
