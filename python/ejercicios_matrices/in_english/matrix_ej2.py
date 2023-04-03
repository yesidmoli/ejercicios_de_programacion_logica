"""Read an integer 4x4 matrix and determine how many times the largest number is repeated in it."""
try:
	print("4*4 array").

	matrix = []
	major = 0
	pos_major = 0
	cont = 0

	for fil_i in range(4): #read the matrix according to the parameters
		row = []
		for col_j in range(4):
			num = int(input(f"Enter an integer for position: [{fil_i} ,{col_j}] "))
			row.append(num)
		matrix.append(row)

	for fil_k in range(len(matrix)): #search in matrix for the largest number
		for col_l in range(len(matrix[fil_k])):
			

			if matrix[fil_k][col_l] > major: #condition to get the greater of
				major = matrix[fil_k][col_l]
				pos_major = fil_k, col_l

			if matrix[fil_k][col_l] == major: #compare to find out how many times the major is repeated
				cont += 1
	print(f"The largest number that is {major} is repeated ({cont} times) ") #we print result.
	
except ValueError:
	print("The entered data must be numeric") 

