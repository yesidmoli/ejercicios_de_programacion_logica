"""11. Read an integer 5x3 array and determine in which column is the smallest even number."""
try:
	print("5*3 matrix.")

	# Read the 5*3 matrix
	matrix = []
	for i in range(5):
		row = []
		for j in range(3):
			num = int(input(f"Enter an integer for the position: [{i} ,{j}] "))
			row.append(num)
		matrix.append(row)


	# Find the smallest even number in the array
	minor_pair = float('inf') # Initialize with positive infinity as no even number has been found yet
	col_pair = 0
	for fil_k in range(len(matrix)):
		for col_l in range(len(matrix[fil_k])):

			if matrix[fil_k][col_l] % 2 == 0 and matrix[fil_k][col_l] < minor_pair:
				minor_pair = matrix[fil_k][col_l]
				col_pair = col_l
		
	# Print the matrix and the column where the smallest even number is found
	print(matrix)
	if minor_pair == float('inf'):
		print("No even number was found in the array").
	else:
		print(f"The smallest even number ({minor_pair}) is found in column {col_pair}")

except ValueError:
	print("The input must be numeric")  