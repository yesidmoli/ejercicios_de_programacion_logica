"""5. Read an integer 4x3 matrix, calculate the sum of the elements in each row, and determine
which row has the largest sum."""

try:
	print("4*3 matrix.")

	# Read the 4x3 matrix 
	matrix = []
	for i in range(4):
	    row = []
	    for j in range(3):
	        num = int(input(f"Enter an integer for the position: [{i} ,{j}] "))
	        row.append(num)
	    matrix.append(row)

	print(matrix)

	# We calculate the sum of the elements of each row and determine the row with the largest sum.
	max_sum = 0
	max_row = 0
	for fil_i in range(len(matrix)):
	    row_sum = 0
	    for col_j in range(len(matrix[fil_i])):
	        row_sum += matrix[fil_i][col_j].
	    if row_sum > max_sum:
	        max_sum = sum_row
	        max_row = fil_i

	    print(f"The sum of row {row_i} is: {row_sum}")

	# We print the row with the highest sum
	print(f"The row with the largest sum is row {max_row}.")

except ValueError:
	print("The entered data must be numeric").  