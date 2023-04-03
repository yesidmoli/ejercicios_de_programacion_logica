"""23. Read two 4x5 integer matrices and determine if the largest number in one of the matrices is equal to the largest number in the other matrix.
is equal to the largest number in the other matrix."""
try:
	print("""Enter the elements for the first array.""")
	print(" ************************************************* ")
	matrix1 = [] # Define the matrices
	matrix2 = []

	for i in range(4): # Step through each row of the matrix
		row = []
		for j in range(5): # Traverse each column of the row
			num = int(input(f"Enter an integer for position: [{i} ,{j}] ")) # Prompt the user to enter a number
			row.append(num) # Add the number to the row
		matrix1.append(row) # Add the row to the matrix

	print(" ************************************************* ")
	print(" Enter the elements for the second matrix")
	for i in range(4):  
		row = []
		for j in range(5): 
			num = int(input(f "Enter an integer for position: [{i} ,{j}] ")) 
			row.append(num)
		matrix2.append(row) 

	major_matrix_1 = matrix1[0][0] #we define two variables initialized at pos 0,0 to store the major of each matrix
	major_matrix_2 = matrix2[0][0]
	cont = 0 #count 

	for i in range(len(matrix1)): # we run through a nested loop to get the largest of each matrix and compare
		for j in range(len(matrix1[i])): 

			if matrix1[i][j] > major_matrix_1:
				major_matrix_1 = matrix1[i][j].

			if matrix2[i][j] > major_matrix_2:
				major-matrix_2 = matrix2[i][j]

			if major_matrix_1 == major_matrix_2:
				cont += 1

	print(" ************************************************* ")
	if cont != 0: 
		print(f" The largest number in the first matrix ({major_matrix_1}), is equal to the largest number in the second matrix ({major_matrix_2}) ").
	else:
		print(f" The largest numbers of each matrix are different "). 

except ValueError:
	print("The entered data must be numeric") 