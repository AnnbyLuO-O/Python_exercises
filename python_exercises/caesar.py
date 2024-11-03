"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Caesar Puzzle
    """
    i = int(input('Secret number: '))  # Displacement letter amount
    cipher = input('What\'s the ciphered string? ')  # input
    d = decipher_word(cipher, i)  # cipher is the encrypted string, i is the displacement
    print('The deciphered string is: ', d)


def reverse(alphabet, x):  # 反轉原本的26個字母(上面的i拉下來變成x)
    """
    Reverse the alphabet x positions
    """
    new_alphabet = alphabet[(26-x):] + alphabet[:(26-x)]
    return new_alphabet


def decipher_word(cipher, x):  # 解密出來的字母
    """
    decipher the word.
    """
    new_alphabet = reverse(ALPHABET, x)
    ans = ''
    for i in range(len(cipher)):
        ch = cipher[i]
        if ch.isalpha():
            de = ALPHABET[new_alphabet.find(ch.upper())]
            ans += de.upper()
        else:
            ans += ch
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
