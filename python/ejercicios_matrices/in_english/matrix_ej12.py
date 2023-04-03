"""12. Read an integer 5x5 matrix and determine in which row is the largest number ending in 6.
in 6."""
try:
	print("5*5 matrix.")

	# Read the 5*5 matrix
	matrix = []
	for i in range(5):
		row = []
		for j in range(5):
			num = int(input(f"Enter an integer for position: [{i} ,{j}] "))
			row.append(num)
		matrix.append(row)


	# Find the largest number ending in 6 in the array
	major_terminated_6 = 0
	row = 0
	for fil_k in range(len(matrix)):
		for col_l in range(len(matrix[fil_k])):

			if matrix[fil_k][col_l] % 10 == 6 and matrix[fil_k][col_l] > major_terminated_6:
				major_terminated_6 = matrix[fil_k][col_l]
				row = fil_k
	
	# Print the matrix and the row where the largest number ending in 6 is found
	print(matrix)
	if major_terminated_6 == 0:
		print("There is no largest number ending in 6").
	else:
		print(f"The largest number ending in 6 which is: ({major_terminated_6}) is found in row {row}")

except ValueError:
	print("The data entered must be numeric")  