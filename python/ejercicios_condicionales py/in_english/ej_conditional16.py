"""Read an integer number with three digits and determine if at least two of its three digits are equal."""

try:
	#get the integer number
	num1 = int(input("Enter an integer number with three digits: "))

	if num1 < 100 or num1 > 999: #check if it is a three digit number
		print("The number must have three digits")

	else: #if the above is not true, get the digits of the number

		d1 = num1 // 100
		d2 = (num1 // 10) % 10 
		d3 = num1 % 10

		if d1 == d2 or d1 == d3 or d2 == d1 or d3 == d1 or d2 == 3:  #check which digits are equal
			print("At least two of its three digits are equal")

		else:
			print("None of the 3 digits are equal")

except ValueError:
	print("The entered data must be numeric")