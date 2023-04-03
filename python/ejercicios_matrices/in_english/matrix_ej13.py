"""13. Read an integer 5x3 matrix and determine in which column is the largest number that
starts with the digit 4."""

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


	# Find in which column is the largest number starting at 4 in the matrix
	max_start_4 = 0
	col = 0
	for fil_k in range(len(matrix)):
		for col_l in range(len(matrix[fil_k])):

			if matrix[fil_k][col_l] // 10 == 4 and matrix[fil_k][col_l] > max_start_4: # NOTE: If the number in the matrix cell is equal to 4,
max_start_4 = matrix[fil_k][col_l] # this expression will not consider it as a number starting with 4.
				col = col_l
	
	# print the matrix and the column where the largest number starting with 4 is found.
	print(matrix)
	if max_start_4 == 0:
		print("There is no largest number starting with 4").
	else:
		print(f"The largest number starting at 4 is: ({max_start_4}) is found in row {col}")

except ValueError:
	print("The data entered must be numeric")  