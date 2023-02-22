"""Read an integer number of three digits and determine if any digit is a multiple of the others."""

try: #we capture the integer number
	num1 = int(input("Enter an integer number of three digits: "))

	if num1 < 100 or num1 > 999: #we verify if the number has 3 digits
		print("Numbers must have three digits")

	else: #we obtain the digits
		d1 = num1 // 100
		d2 = (num1 // 10) % 10 
		d3 = num1 % 10

		if d1 % d2 == 0: #we verify which digit is a multiple of the other
			print(f"The digit {d1} is a multiple of digit {d2}")

		elif d1 % d3 == 0:
			print(f"The digit {d1} is a multiple of digit {d3}")

		elif d2 % d1 == 0:
			print(f"The digit {d2} is a multiple of digit {d1}")

		elif d2 % d3 == 0:
			print(f"The digit {d2} is a multiple of digit {d3}")

		elif d3 % d1 == 0:
			print(f"The digit {d3} is a multiple of digit {d1}")

		elif d3 % d2 == 0:
			print(f"The digit {d3} is a multiple of digit {d2}")

		else:
			print("No digit is a multiple of the others")

except ValueError:
	print("The entered data must be numeric")