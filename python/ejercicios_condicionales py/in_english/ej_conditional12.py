"""Read two integer numbers with two digits and determine if they have common digits."""

try: #we capture the two numbers
	number1 = int(input("Enter the first integer number with two digits: "))
	number2 = int(input("Enter the second integer number with two digits: "))

	if number1 and number2 >= 10 and number2 and number1 <= 99: #we verify if the numbers have two digits

		#we verify if the numbers have common digits
		if (number1 // 10 == number2 // 10) or (number1 // 10 == number2 % 10) or (number1 % 10 == number2 // 10) or (number1 % 10 == number2 % 10):

			print("The numbers have common digits")

		else:
			print("The numbers don't have common digits")

	else:
		print("At least one of the two numbers is out of range") #otherwise, we print
		
except ValueError:
	print("The entered data must be numeric")