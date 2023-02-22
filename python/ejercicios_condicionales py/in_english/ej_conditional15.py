""" Read an integer number of three digits and determine the sum of its digits."""

try:
	# Capture the integer number
	num1 = int(input("Enter an integer number of three digits: "))


	if num1 < 100 or num1 > 999: # Verify if the number has 3 digits
		print("The number must have three digits.")

	else: # If the above condition is not met, obtain the digits and add them up
		suma = (num1 // 100) + ((num1 // 10) % 10) + (num1 % 10)

		print(f"The sum of all the digits is {suma}.")

except ValueError:
	print("The entered data must be numeric.")