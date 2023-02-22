"""
Read an integer number with three digits and determine in which position the highest digit is located."""

try: #we capture the integer number
	num1 = int(input("Enter an integer number with three digits: "))

	if num1 < 100 or num1 > 999: #we verify if the number has 3 digits
		print("The number must have three digits")

	else: #since the previous condition is not met, we obtain the position of the digits

		po1 = num1 // 100
		po2 = (num1 // 10) % 10 
		po3 = num1 % 10

		if po1 > (po2 and po3): #we check in which position the highest digit is located
			print("The highest digit is located in position 1")

		elif po2 > (po1 and po3):
			print("The highest digit is located in position 2")

		elif po3 > (po1 and po2):
			print("The highest digit is located in position 3")

		else:
			print("All digits are equal")

except ValueError:
	print("The entered data must be numerical")




