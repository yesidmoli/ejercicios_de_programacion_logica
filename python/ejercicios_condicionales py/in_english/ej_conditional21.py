"""Read three integer numbers of two digits each and determine in which of them the largest digit is located."""

try:
	# capture the 3 numbers
	num1 = int(input("Enter the first integer number of two digits: "))
	num2 = int(input("Enter the second integer number of two digits: "))
	num3 = int(input("Enter the third integer number of two digits: "))

	# Verify that the numbers are two digits
	if num1 < 10 or num1 > 99 or num2 < 10 or num2 > 99 or num3 < 10 or num3 > 99:
		print("Error: The numbers must be integers of two digits (between 10 and 99).")

	else:
    	# Search for the largest digit in each number, with the max function
		largest1 = max(str(num1))
		largest2 = max(str(num2))
		largest3 = max(str(num3))
    
    	# Compare the largest to determine in which one the largest digit is located

		if largest1 > largest2 and largest1 > largest3:
			print("The largest digit is located in the first number.")

		elif largest2 > largest1 and largest2 > largest3:
			print("The largest digit is located in the second number.")

		else:
			print("The largest digit is located in the third number.")


except ValueError:
	print("The entered data must be numeric.")

