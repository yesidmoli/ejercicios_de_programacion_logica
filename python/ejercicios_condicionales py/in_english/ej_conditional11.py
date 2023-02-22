"""Read two integers and determine which one is the greatest."""

try:
	# capture the two numbers
	number1, number2 = int(input("Enter the first number")), int(input("Enter the second number"))

	if number1 > number2: # check which one is the greatest
		print(f"{number1} is greater than {number2}")

	else:
		print(f"{number2} is greater than {number1}")

except ValueError:
	print("Error: The input data must be numeric")