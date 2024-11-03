"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Matching DNA. A to T, T to A, C to G, G to C.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna == '':
        return 'DNA strand is missing.'
    else:
        ans = ''
        for i in range(len(dna)):
            alphabet = dna[i]
            if alphabet == 'A':
                ans += 'T'
            elif alphabet == 'T':
                ans += 'A'
            elif alphabet == 'G':
                ans += 'C'
            elif alphabet == 'C':
                ans += 'G'
            else:
                ans += alphabet
        return ans





    # for alphabet in dna:
    #     if alphabet == ' ':
    #         print('DNA strand is missing.')
    #     elif alphabet == 'A':
    #         print('T', end='')
    #     elif alphabet == 'T':
    #         print('A', end='')
    #     elif alphabet == 'C':
    #         print('G', end='')
    #     elif alphabet == 'G':
    #         print('C', end='G')
    # return ans











# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
