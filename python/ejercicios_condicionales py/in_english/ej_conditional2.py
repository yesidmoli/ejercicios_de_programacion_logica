"""Read an integer and determine if it has 3 digits."""

try:
	number = int(input("Enter an integer: ")) #capture the integer

	if number > 99 and number < 999: #check if the number has 3 digits, if so, print
		print("It is a 3-digit number")

	else:
		print("It is not a 3-digit number") #otherwise, print not a 3-digit number
		
except ValueError:
	print("+++error+++")




