""". Read a 3-digit integer number and determine if it has the digit 1."""
try:
	#capture the number.
	num = int(input("Enter the 3-digit integer ")))

	if num < 100 or num > 999:
		print("The number must be 3 digits").

	else:
		"""while num != 0:

			digit = num % 10

			if digit == 1:
				print("The number entered has the number 1")

				break
			else:
				print("The number does not have the number 1")


			num = num // 10"""


		while num != 0:

			if num // 10 == 1 or num % 10 == 1:
				print("The number has the 1 ") 
				break

			num //= 10

except ValueError:
	print("The entered data must be numeric")