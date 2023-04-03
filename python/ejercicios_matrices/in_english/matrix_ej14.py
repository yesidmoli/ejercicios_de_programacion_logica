"""14. Read an integer 5x5 matrix and determine how many numbers stored in it have
more than 3 digits."""
try:
	print("5*5 matrix.")

	# Read the 5*3 matrix
	matrix = []
	for i in range(5):
		row = []
		for j in range(5):
			num = int(input(f"Enter an integer for the position: [{i} ,{j}] "))
			row.append(num)
		matrix.append(row)


	# we look for how many numbers in the matrix have more than 3 digits
	cont = 0
	for fil_k in range(len(matrix)):
		for col_l in range(len(matrix[fil_k])):

			if matrix[fil_k][col_l] > 999:
				cont += 1
	
	# We print the matrix and the number of stored numbers that have more than 3 digits
	print(matrix)

	if cont != 0:
		print(f"In the array there are ({cont}) numbers that have more than 3 digits ").
	else:
		print("The array has no numbers with more than 3 digits stored")

except ValueError:
	print("The entered data must be numeric")  