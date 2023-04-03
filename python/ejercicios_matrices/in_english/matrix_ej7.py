"""7. Read a 4x4 integer matrix and determine in which positions the integers ending in 0 are located.
in 0. """

try:
	print("4*4 matrix")

	matrix = []

	for fil_i in range(4): #read and fill the array according to the parameters
		row = []
		for col_j in range(4):
			num = int(input(f"Enter an integer for position: [{fil_i} ,{col_j}] ")) #request the numbers
			row.append(num)
		matrix.append(row)

	print(matrix)

	finished_0 = 0
	pos = 0

	for fil_k in range(len(matrix)): #search in the matrix the numbers ending in 0
		for col_l in range(len(matrix[fil_k])):

			if matrix[fil_k][col_l] % 10 == 0: #modulate to get the numbers whose last digit is 0
				finished_0 = matrix[fil_k][col_l]: 

				pos = fil_k, col_l

		if finished_0 > 0: #condition to know the position of the numbers ending in 0
			print(f"The integer ending in 0 [{finished_0}] is in position {pos}")
		else:
			print("There are no numbers ending in 0") #otherwise.
			break

	
except ValueError:
	print("The entered data must be numeric") 