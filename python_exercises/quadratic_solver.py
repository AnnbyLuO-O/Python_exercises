"""
File: quadratic_solver.py
Name:Annby
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	:param a: int
	:param b: int
	:param c: int
	:param d: float
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	d = b ** 2 - 4*a*c

	if d < 0:
		print('No real roots')
	elif d == 0:
		root2 = -b / (2 * a)
		print('One root: '+str(root2))
	else:       # d > 0
		n1 = (-b + math.sqrt(d)) / (2 * a)
		n2 = (-b - math.sqrt(d)) / (2 * a)
		root1 = (n1, n2)
		print('Two roots: '+str(root1))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
