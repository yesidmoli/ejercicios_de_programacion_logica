"""Read an integer number with two digits and determine the sum of its digits."""

try:
	number = int(input("Enter an integer number with two digits"))
	
	if number >= 10 and number <= 99: #creating a condition to determine if the entered number is a two-digit number

	#getting the digits
	d1 = number // 10
	d2 = number % 10

	#summing the obtained digits
	suma = d1 + d2 

	#printing the result of the sum 
	print(f"The sum of the digits is: {suma}")

	else:# if the condition is not met, print an error message
		print("The number is not a two-digit number")

except ValueError:
	print("Error")