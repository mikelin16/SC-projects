"""
File: weather_master.py
Name: Mike
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -460


def main():
	"""
	pre-condition: To find out the highest, lowest, average, temperature
	and how many days are there below 16 degree among the temperature(s) you entered
	post-condition: Display the highest, lowest, average temperature
	and how many days there are below 16 degree
	"""
	print('stanCode \"Weather 4.0"')
	x = int(input('Next Temperature: (Or ' + str(EXIT) + ' to quit)?'))
	count = 0
	total = 0
	cold_days = 0
	if x == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = x
		minimum = x
		count = count + 1
		total = total + x
		if x < 16:
			cold_days = cold_days + 1
		while True:
			x = int(input('Next Temperature: (Or ' + str(EXIT) + ' to quit)?'))
			count = count + 1
			total = total + x
			if x < 16:
				cold_days = cold_days + 1
			if x == EXIT:
				count = count - 1
				total = total - x
				if x < 16:
					cold_days = cold_days - 1
				break
			if x > maximum:
				maximum = x
			if x < minimum:
				minimum = x
		average = total / count
		print('Highest temperature: ' + str(maximum))
		print('Lowest temperature: ' + str(minimum))
		print('Average: ' + str(average))
		print(str(cold_days) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
