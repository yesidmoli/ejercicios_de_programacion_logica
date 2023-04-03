"""17. Read an integer 5x4 matrix and determine how many multiples of 5 are stored in it.
it."""
try:
	print("5*4 matrix.")

	# Read the 5*4 array
	matrix = [] # Define the array
	for i in range(5): # Step through each row of the matrix
		row = []
		for j in range(4): # Traverse each column of the row
			num = int(input(f"Enter an integer for position: [{i} ,{j}] ")) # Prompt the user to enter a number
			row.append(num) # Add the number to the row
		matrix.append(row) # Add the row to the matrix

	# find how many numbers in the array are multiplies of 5
	cont = 0
	multiples_5 = []
	for fil_k in range(len(matrix)):
		for col_l in range(len(matrix[fil_k])):

			if matrix[fil_k][col_l] % 5 == 0: #compare to know which numbers are multiplies of 5.
				cont += 1
				multiples_5.append(matrix[fil_k][col_l])

	
	# We print the matrix and the amount of numbers that are multiplies of 5.
	print(matrix)

	if cont != 0:
		print(f"In the matrix there are ({cont}) numbers that are multiples of 5 ")
		print(f"Which are: {multiples_5}")
	else:
		print("The array does not have stored numbers that are multiples of 5")

except ValueError:
	print("The entered data must be numeric") 