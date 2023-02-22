"""Read an integer and determine if it is negative."""
try:
	number = int(input("Enter an integer number")) #we capture the integer number

	if number < 0: #we verify if the number entered is positive or negative
		print("It is a negative number")
	else:								
		print("It is a positive number")


except ValueError:
	print("The data entered must be numeric") #if the user entered a data that is not numeric, we show a message