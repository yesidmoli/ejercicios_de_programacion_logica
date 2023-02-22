"""Read an integer number with two digits and determine if the two digits are equal."""

try: #we capture the integer number
	number = int(input("Enter an integer number with two digits"))

	if number >= 10 and number <= 99:  #we verify if it is a two-digit number

		#get the digits of the number

		d1 = number // 10
		d2 = number % 10

		if d1 == d2: #we verify if the digits are equal
			print("The two digits are equal")
			
		else:
			print("The two digits are not equal") #otherwise

	else:
		print("Invalid number")

except ValueError:
	print("The entered data must be numerical")