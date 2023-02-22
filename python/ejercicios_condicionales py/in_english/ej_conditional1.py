"""Read an integer and determine if it is a number ending in 4."""
try:
	number = int(input("Enter an integer number: ")) #capture the integer number and store it in a variable

	if number % 10 == 4: #if the remainder of the division by 10 is equal to 4, print that the number ends in 4
   		print("The number ends in 4")
    
	else:
		print("The number does not end in 4") #if the previous condition is not met, print that the number does not end in 4
    
except ValueError:
	print("The entered data must be numeric") #if the user enters a non-numeric value, print an error message