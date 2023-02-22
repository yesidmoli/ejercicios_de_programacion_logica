"""Read an integer number with three digits and determine if the first and last digit are equal."""

try:
	# capture the integer number with three digits
	num = int(input("Enter an integer number with three digits: "))

	# Verify that the number has three digits
	if num < 100 or num > 999:
		print("The number must have three digits.")

		# Get the first and last digit
		first_digit = num // 100
		last_digit = num % 10

		# Determine if the first and last digit are equal
		if first_digit == last_digit:
			print("The first and last digit are equal.")

	else:
		print("The first and last digit are different.")

except ValueError:
	print("The entered data must be numerical.")