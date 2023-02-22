"""Read an integer of two digits and determine if both digits are even."""

try:
	# Ask the user to input a two-digit integer and define a variable for it
	number = int(input("Enter a two-digit integer: "))

	# Get the digits of the number
	d1 = number // 10
	d2 = number % 10

	# Create a condition to check if both digits are even
	if d1 % 2 == 0 and d2 % 2 == 0:
		print("Both digits are even.")
		
	else:
		print("At least one of the digits is not even.")

except ValueError:
print("Error")