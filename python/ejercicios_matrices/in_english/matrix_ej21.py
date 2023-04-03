"""21. Read two 4x5 integer arrays and determine how much data they have in common."""""
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
			num = int(input(f "Enter an integer for position: [{i} ,{j}] ")) 
			row.append(num)
		matrix2.append(row) 

	cont = 0 #start a counter at 0 to know if there is common data

	for i in range(len(matrix1)): # we traverse the matrices
		for j in range(len(matrix1[i])): 

			if matrix1[i][j] == matrix2[i][j]: #compare each data of the two matrices.
				cont +=1 #counter to count how much data they have in common	

	if cont != 0: #if counter is different from 0, there is data in common
		print(f" The two arrays have ({cont}) data in common ")
	else:
		print("The two arrays have no common data") #otherwise.

except ValueError:
	print("The data entered must be numeric") 