"""Averaging the first x multiples of 2 and determining if that average is greater than the averages of the y multiples of 5 for the x and y values read.
averages of the y multiples of 5 for x and y values read."""

try:
	x = int(input("Enter the value of x for the first multiples of 2 : "))
	y = int(input("Enter the value of y for the first multiples of 5 : "))

	average_1 = 0
	average_2 = 0
	
	for i in range(1, x+1): #we run the loop by giving the parameters 

		average_1 += i * 2
		
	average_1 //= x

	print(f"The average of the {x} multiplied by 2 is {average_1}")


	for i in range(1, y+1): #run the loop by giving the parameters 

		average_2 += i * 5
		
	average_2 //= y
	
	print(f"The average of the {y} multiplied by 5 is {average_2}")

	if average_1 > average_2:
		print(f"The average {average_1} is greater than the average {average_2}")

	if average_2 > average_1:
		print(f"The average {average_2} is greater than the average {average_1}")

	else:
		print("Averages are equal")
			

except ValueError:
	print("The data entered must be numeric")