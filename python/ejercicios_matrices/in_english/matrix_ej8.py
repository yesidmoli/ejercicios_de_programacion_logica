"""8. Read a 4x4 integer matrix and determine how many integers ending in 0 are stored in it.
stored in it."""

try:
	print("4*4 matrix").

	matrix = []

	for fil_i in range(4): #read and fill the array according to the parameters
		row = []
		for col_j in range(4):
			num = int(input(f"Enter an integer for position: [{fil_i} ,{col_j}] ")) #request the numbers
			row.append(num)
		matrix.append(row)

	print(matrix)

	finished_0 = 0
	cont = 0

	for fil_k in range(len(matrix)): #search in the matrix the numbers ending in 0
		for col_l in range(len(matrix[fil_k])):

			if matrix[fil_k][col_l] % 10 == 0: #modulate to get the numbers with a last digit of 0
				cont +=1 #if there are numbers ending in 0 we count

	if cont > 0: #condition to find out how many numbers ending in 0 are there
		print(f"In the array there are {cont} numbers that end in 0") 
	else:
		print("There are no numbers ending in 0") #otherwise.
			
except ValueError:
	print("The entered data must be numeric") 