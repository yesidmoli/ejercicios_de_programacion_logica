"""Read an integer number less than 50 and positive and determine if it is a prime number."""

try: #we capture the integer number
	number = int(input("Enter an integer number less than 50 and positive "))

	if number <= 0 or number >= 50: #we verify if it is a positive number and less than 50
		print("The number must be less than 50 and positive")

	else: #if the previous condition is not met, we validate if the number is prime
		if number % 2 != 0:
			print(f"{number} is a prime number")
		else:
			print(f"{number} is not a prime number")

except ValueError:
	print("The entered data must be numeric")