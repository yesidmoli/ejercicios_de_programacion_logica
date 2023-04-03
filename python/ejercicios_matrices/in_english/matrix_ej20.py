"""20. Read two 4x5 integer matrices, then read an integer and determine if each of the elements of one of the matrices is equal to each of the elements of the other matrix.
elements of one of the arrays is equal to each of the elements of the other array multiplied by the integer read.
multiplied by the integer read. """

try:
	print(" Enter the elements for the first array.")
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
			num = int(input(f"Enter an integer for position: [{i} ,{j}] ")) 
			row.append(num)
		matrix2.append(row) 

	print(" ************************************************* ")
	#request the integer
	number = int(input(" Enter an integer number: "))

	cont = 0 #initialize a counter and two variables to store the multiplication
	multi_matrix_1 = 0
	multi_matrix_2 = 0
	multiply1 = [] #create two lists to store the multiplication of each matrix
	multiply2 = []

	for i in range(len(matrix1)): #compare the matrices, multiplying the integer number read
		for j in range(len(matrix1[i])): 

			multi_matrix_1 = matrix1[i][j] * number.
			multiply1.append(multi_matrix_1)

			multi_matrix_2 = matrix2[i][j] * number
			multiply2.append(multi_matrix_2)

			if multi_matrix_1 != multi_matrix_2: #if the multiplication of each of the matrices is different, they are not equal
				cont +=1 #counter to find out if they are different
				
	print(" ************************************************* ")
	print("Multiplication of each matrix")
	print(f" M1 {multiply1}")
	print(f" M2 {multiply2}")

	print(" ************************************************* ")
	if cont == 0: #if cont == 0, it means that the matrices are equal.
		print(f" The elements of the matrices multiplied by ({number}) are exactly equal.")
	else:
		print(" The elements of the arrays are not exactly equal.") #otherwise.

except ValueError:
	print("The entered data must be numeric.")