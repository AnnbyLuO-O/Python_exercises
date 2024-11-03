"""
File: weather_master.py
Name: Annby
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT: int = -1


def main():
	"""
	:param data: int
	:param count: int
	# cold_day : means temperature < 16 a day
	"""
	print('standCode\'Weather Master 4.0!')
	data = int(input('Next Temperature:' + ' (or ' + str(EXIT) + ' to quit)? '))
	if data == EXIT:  # leave
		print('No temperatures were entered !')
	else:  # find highest data ＆ lowest data
		highest = data
		lowest = data
		count = 0
		cold_day = 0
		total = 0
		while True:
			if data == EXIT:
				break
			if data > highest:
				highest = data
			if data < lowest:
				lowest = data
			if data < 16:  # cold_day
				cold_day += 1
			count += 1  # total
			total += data  # sum
			data = int(input('Next Temperature:' + ' (or ' + str(EXIT) + ' to quit)? '))
		print('Highest temperature= ' + str(highest))
		print('Lowest temperature= ' + str(lowest))
		print('Average = ' + str(total / count))
		print(str(cold_day), end='')
		print(' cold day(s)')

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
