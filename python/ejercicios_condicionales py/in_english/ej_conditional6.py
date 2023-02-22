"""Read an integer number with two digits less than 20 and determine if it is a prime number."""

try:
	#capture the number
	number = int(input("Enter an integer number with two digits: "))

	#check if the number is two digits and less than 20
	if number >= 10 and number < 20:
		
		if number % 2 != 0: #if the condition is met, we mod by 2 to determine if it is prime or not
			print(f"{number} is a prime number")

		else:
			print(f"{number} is not a prime number")
	else:
		print("The number is not valid") #if the above conditions are not met, this message will be printed

except ValueError:
	print("The entered value must be numeric")