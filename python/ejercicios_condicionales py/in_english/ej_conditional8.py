"""Read a two-digit integer and determine if its two digits are prime."""

try: #capture the integer
	number = int(input("Enter a two-digit integer "))

	if number >= 10 and number <= 99: #check if it is two digits

		# get the digits
		d1 = number // 10
		d2 = number % 10

		if d1 % 2 != 0 and d2 % 2 != 0: #check the digits to see if they are prime numbers
			print("is prime")

		else:
			print("at least one of the two digits is not prime")

	else:
		print("invalid number") #If the above conditions are not met

except ValueError:
	print("the entered value must be numeric")