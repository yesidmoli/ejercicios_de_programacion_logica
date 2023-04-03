"""15. Read an integer 5x4 matrix and determine how many numbers stored in it end in 34.
end in 34. """

try:
	print("5*4 matrix.")

	# Read the 5*4 matrix
	matrix = [] # Define the array
	for i in range(5): # Step through each row of the matrix
		row = []
		for j in range(4): # Traverse each column of the row
			num = int(input(f"Enter an integer for position: [{i} ,{j}] ")) # Prompt the user to enter a number
			row.append(num) # Add the number to the row
		matrix.append(row) # add the row to the matrix

	# find how many numbers in the array end in 34
	cont = 0
	for fil_k in range(len(matrix)):
		for col_l in range(len(matrix[fil_k])):

			if matrix[fil_k][col_l] % 100 == 34:
				cont += 1
	
	# Print the array and the number of stored numbers ending in 34
	print(matrix)

	if cont != 0:
		print(f"In the array there are ({cont}) numbers ending in 34 ").
	else:
		print("The array does not have stored numbers ending in 34")

except ValueError:
	print("The entered data must be numeric") 