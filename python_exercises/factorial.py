"""
File: factorial.py
Name: Annby
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT: int = -100


def main():
	"""
	:param n: int
	"""
	print('Welcome to stanCode factorial master!')
	n = int(input('Give me a number, and I will list the answer of factorial: '))
	# answer = 1
	while True:
		if n == EXIT:
			print('------See Ya!------')
			break
		else:
			answer = 1
			while n > 1:
				answer *= n
				n -= 1
			print('Answer: '+str(answer))
		n = int(input('Give me a number, and I will list the answer of factorial: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()
