"""18. Read an integer 5x5 matrix and determine in which exact position the largest multiple of 8 is located.
multiple of 8.""""

try:
	print("5*5 matrix.")

	# Read the 5*4 matrix
	matrix = [] # Define the array
	for i in range(5): # Step through each row of the matrix
		row = []
		for j in range(5): # Traverse each column of the row
			num = int(input(f "Enter an integer for position: [{i} ,{j}] ")) # Prompt the user to enter a number
			row.append(num) # Add the number to the row
		matrix.append(row) # Add the row to the matrix

	# find how many numbers in the matrix are multiplies of 5
	max_multiple_8 = 0
	pos_multiple = 0
	multi_8 = []
	for fil_k in range(len(matrix)):
		for col_l in range(len(matrix[fil_k])):
			#compare to find out which numbers are multiplies of 8 and which is the largest.
			if matrix[fil_k][col_l] % 8 == 0 and matrix[fil_k][col_l] > max_multiple_8: 
				max_multiple_8 = matrix[fil_k][col_l].
				pos_multiple = fil_k, col_l
				multi_8.append(matrix[fil_k][col_l]) #those that are multiplies of 8 we add to a list


	# we print the matrix and the largest number multiplo of 8
	print(matrix)

	if max_multiple_8 != 0:
		print(f"Multiples of 8: {multi_8}")
		print(f"The largest number multiples of 8 ({max_multiple_8}) is in position {pos_multiple}")
	else:
		print("There are no multiples of 8 ")

except ValueError:
	print("The entered data must be numeric")