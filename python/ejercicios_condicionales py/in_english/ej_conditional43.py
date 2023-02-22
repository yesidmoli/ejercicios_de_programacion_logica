"""Read two integers and determine if the difference between them is an exact divisor of either of the two numbers."""

try: #we capture the integers
	num1, num2 = int(input("Enter the first number")), int(input("Enter the second number"))

	difference = num1 - num2 #we create a variable to store the difference

	if difference % num1 == 0 : #we check if the difference modulated by num1 gives a remainder of 0

		print("It is an exact divisor")

	elif difference % num2 == 0: #we check if the difference modulated by num2 gives a remainder of 0
		print("It is an exact divisor")

	else:
		print("Neither of them gives an exact division") #if the above is not met we print


except ValueError:
	print("error")