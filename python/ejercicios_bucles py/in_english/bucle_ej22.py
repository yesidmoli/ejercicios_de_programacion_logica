"""Read an integer and determine how many times it has the digit 1."""

try:
	num = int(input("Enter the integer "))
	counter = 0


	while num != 0:
		digit = num % 10
		num //= 10

		if digit == 1:
			counter += 1

	print(f"the number has {counter} times 1")
		

except ValueError:
	print("The entered data must be numeric")