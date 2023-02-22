"""Read an integer number with two digits and determine if it is prime and also if it is negative."""

try: #we capture the integer number
	number = int(input("Enter a two-digit number"))

	if number < 0: #we check if the number is negative
		print("The number is negative")

	else: #if it is not negative, we verify by means of the condition if it is a two-digit number

		if number >= 10 and number <= 99:

			if number % 2 != 0: #we modulate to know if it is a prime number or not
				print("It is prime")

			else:
				print("It is not prime")

		else:
			print("The number is not valid") #if the previous conditions are not met

except ValueError:
	print("ValueError")