""" Read three integer numbers (with two digits) and determine which one is the greatest. Use
only two variables."""

try: #we capture the integer numbers
	n1 = int(input("Enter the first two-digit number: "))
	n2 = int(input("Enter the second two-digit number: "))
	n3 = int(input("Enter the third two-digit number: "))


	if (n1 < 10 or n1 > 99) or (n2 < 10 or n2 > 99) or (n3 < 10 or n3 > 99): #we verify if the numbers have two digits
		print("The numbers must be two-digit numbers.")

	else: #if the previous condition is not met, we condition and search for the greatest number

		greatest = n1

		if n2 > greatest:
			greatest = n2

		if n3 > greatest:
			greatest = n3

			print(f"The greatest number is {greatest}.")

except ValueError:
	print("The entered data must be numeric.")