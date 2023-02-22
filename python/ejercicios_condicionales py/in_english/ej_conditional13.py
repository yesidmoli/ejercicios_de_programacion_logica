"""Read two integer numbers with two digits and determine if the sum of the two numbers results in an even number."""

try: #we capture the numbers
	num1 = int(input("Enter the first integer number: "))
	num2 = int(input("Enter the second integer number: "))

	if (num1 and num2) >= 10 and (num2 and num1) <= 99: #we verify if the numbers have two digits 

		if ((num1 + num2) % 2 == 0): #we verify if the sum of the numbers is even 

			print(f"The sum of the two numbers results in an even number which is: {num1 + num2}")

		else:
			#otherwise 
			print(f"The sum of the two numbers results in an odd number which is: {num1 + num2}")

	else:
		print("At least one of the two numbers is out of range")

except ValueError:
	print("The data entered must be numeric")