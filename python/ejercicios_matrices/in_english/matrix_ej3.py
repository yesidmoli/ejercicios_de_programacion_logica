"""3. Read an integer 3x4 matrix and determine in which exact positions the even numbers are found.
even numbers."""

try:
	print("3*4 matrix").

	matrix = []
	num_even = 0
	
	for fil_i in range(3): #read the matrix according to the parameters
		row = []
		for col_j in range(4):
			num = int(input(f"Enter an integer for position: [{fil_i} ,{col_j}] "))
			row.append(num)
		matrix.append(row)

	print(matrix) #print the matrix

	for fil_i in range(len(matrix)): #sort the array
		for col_j in range(len(matrix[fil_i])):

			if matrix[fil_i][col_j] % 2 == 0: #compare the matrix to get the even numbers and their positions.
				num_even = matrix[fil_i][col_j]: #compare the matrix to get the even numbers and their positions.

				print(f"The even number {num_pair} is in position {fil_i, col_j} ") #print the pairs with their positions.
		
except ValueError:
	print("The entered data must be numeric"). 

