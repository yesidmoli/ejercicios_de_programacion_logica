"""Read a two-digit integer and determine if one digit is a multiple of the other."""

try: #capture the integer
	number = int(input("Enter a two-digit number"))

	if number >= 10 and number <= 99: #check if it is a two-digit number

		# get the digits
		d1 = number // 10
		d2 = number % 10

		if d1 % d2 == 0: #validate if d1 is a multiple of d2
			print("The first digit is a multiple of the second")

		elif d2 % d1 == 0:#validate if d2 is a multiple of d1
			print("The second digit is a multiple of the first")

		else:
			print(" Neither digit is a multiple of the other") #otherwise we print

	else:
		print("invalid number")

except ValueError:
	print("the number entered must be numeric")