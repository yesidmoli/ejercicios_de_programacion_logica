"""Read an integer number and determine which is the largest of its digits."""
try:
	num = int(input("Enter the integer."))
	largest = 0


	for i in range(1, num):
		digit = num % 10
		num //= 10

		if digit > greater:
			greater = digit
	
	print("the greatest digit is", greater)
			

except ValueError:
	print("The entered data must be numeric")