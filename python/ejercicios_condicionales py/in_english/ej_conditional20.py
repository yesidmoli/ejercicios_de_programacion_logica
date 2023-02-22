"""Read three integer numbers and display them in ascending order"""

try:
	# Read three integer numbers
	num1 = int(input("Enter the first number: "))
	num2 = int(input("Enter the second number: "))
	num3 = int(input("Enter the third number: "))

	# Sort the numbers in ascending order using conditionals
	if num1 <= num2 and num1 <= num3:

		first = num1
		if num2 <= num3:
			second = num2
			third = num3

		else:
			second = num3
			third = num2

	elif num2 <= num1 and num2 <= num3:
		first = num2

		if num1 <= num3:
			second = num1
			third = num3

		else:
			second = num3
			third = num1

	else:
		first = num3

		if num1 <= num2:
			second = num1
			third = num2

		else:
			second = num2
			third = num1

	# Display the numbers in ascending order
	print("The numbers in ascending order are:", first, second, third)
except ValueError:
	print("The entered value must be numeric")