"""1. Read an integer 4x4 matrix and determine in which row and which column the largest number is found.
largest number."""

try:
	print("4*4 matrix.")
	row = int(input("Enter the number of rows in the matrix: ")) #get the parameters
	column = int(input("Enter the number of columns in the matrix: "))

	if (row > 0 and row <= 4) and (column > 0 and column <= 4):

		matrix = []
		major = 0
		pos_major = 0

		for fil_i in range(row): #read the matrix according to the parameters
			row = []
			for col_j in range(column):
				num = int(input(f"Enter an integer for position: [{fil_i} ,{col_j}] "))
				row.append(num)
			matrix.append(row)

		for fil_k in range(len(matrix)): #search in the matrix for the largest number
			for col_l in range(len(matrix[fil_k])):

				if matrix[fil_k][col_l] > greater:
					major = matrix[fil_k][col_l]
					pos_major = fil_k, col_l

		print(f"The largest number in the array which is: {major} is in position [{pos_major}]") #print the largest number and position.

	else:
		print("the range of rows or columns is not correct").


except ValueError:
	print("The entered data must be numeric")

