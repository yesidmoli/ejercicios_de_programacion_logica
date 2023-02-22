""" Read two integer numbers with two digits and determine the sum of all digits"""

try:
	#we capture the two numbers
	num1 = int(input("Enter the first integer number with two digits: "))
	num2 = int(input("Enter the second integer number with two digits: "))

	if (num1 < 10 or num1 > 99) or (num2 < 10 or num2 > 99): #we verify if the numbers have two digits
		print("The numbers must have two digits")

	else: #if the previous condition is true, we get the digits of the numbers and add them
		suma = (num1 % 10 )+ (num1 // 10) + (num2 % 10) + (num2 // 10) 

		print(f"The sum of all digits is {suma}")

except ValueError:
	print("The entered data must be numeric")
