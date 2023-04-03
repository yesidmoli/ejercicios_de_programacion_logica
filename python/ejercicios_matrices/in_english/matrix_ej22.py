"""22. Read two 4x5 integer matrices and determine if the largest number stored in the first one is in the second.
is in the second one.""" 
try:
	print("""Enter the elements for the first array.""")
	print(" ************************************************* ")
	matrix1 = [] # Define the matrices
	matrix2 = []

	for i in range(4): # Step through each row of the matrix
		row = []
		for j in range(5): # Traverse each column of the row
			num = int(input(f "Enter an integer for position: [{i} ,{j}] ")) # Prompt the user to enter a number
			row.append(num) # Add the number to the row
		matrix1.append(row) # Add the row to the matrix

	print(" ************************************************* ")
	print(" Enter the elements for the second matrix")
	for i in range(4):  
		row = []
		for j in range(5): 
			num = int(input(f"Enter an integer for position: [{i} ,{j}] ")) 
			row.append(num)
		matrix2.append(row) 

	major_matrix_1 = matrix1[0][0]

	for i in range(len(matrix1)): # we traverse the first matrix to get the largest number
		for j in range(len(matrix1[i])): 

			if matrix1[i][j] > largest_matrix_1:
				major_matrix_1 = matrix1[i][j].

	cont = 0 #start a counter at 0 

	for i in range(len(matrix2)): # we traverse matrix 2
		for j in range(len(matrix2[i])): 

			if matrix2[i][j] == major_matrix1 : #compare to see if this is the largest 
				cont +=1 #count
	print(" ************************************************* ")
	print(f" M1 {matrix1}")
	print(f" M2 {matrix2}")
	print(" ************************************************* ")
	print(f" The largest number in the first matrix is: {major_matrix_1} ")

	if cont != 0: #if cont is different from 0, the largest number M1 is in M2
		print(f" The largest number of the first matrix ({major_matrix_1}), is also in the second matrix ")
	else:
		print(f" The largest number of the first matrix ({major_matrix_1}) is not in the second matrix ") #otherwise.

except ValueError:
	print("The input must be numeric")