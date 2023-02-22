"""
Read an integer and if it is a multiple of 4, display its half on the screen. If it is a multiple
of 5, display its square on the screen. If it is a multiple of 6, display its first digit on the screen.
 Assume that the number is not greater than 100.
"""

try: #capture the integer
	number = int(input("Enter an integer: "))


	if number <= 100: #check if the number is less than or equal to 100

		if number % 4 == 0: #check if it is a multiple of 4
			print(f"The half of {number} is: " + str(number/2))

		elif number % 5 == 0: #check if it is a multiple of 5
			print(f"The square of {number} is " + str(number ** 2 ))

		elif number % 6 == 0: #check if it is a multiple of 6

			d1 = str(number)[0]

			print(f"The first digit of {number} is {d1}")

		else:
			print("The number is not a multiple of 4, 5, and 6") #if none of the above conditions are met

	else:
		print("The number is not within range.")

except ValueError:
	print("Invalid input. Please enter a numerical value.")