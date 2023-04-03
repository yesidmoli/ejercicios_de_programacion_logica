"""19. Read two 4x5 integer arrays and determine whether their contents are exactly equal."""""
try:
	

	print(" Enter the elements for the first matrix").
	matrix1 = [] # Define the arrays
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
			num = int(input(f"Enter an integer for position: [{i} ,{j}] ")) 
			row.append(num)
		matrix2.append(row) 

	#compare the matrices
	cont = 0
	for i in range(len(matrix1)):  
		for j in range(len(matrix1[i])): 
			if matrix1[i][j] != matrix2[i][j]:
				cont +=1
				

	if cont == 0: #if counter is still 0 then the matrices are equal
		print(" The matrices are exactly the same.")
	else:
		print(" The matrices are not exactly equal.") #otherwise.

except ValueError:
	print("The entered data must be numeric.")  