"""6. Read an integer 4x4 matrix and calculate the average of the largest numbers in each row."""""
try:
	print("4*4 matrix.")

	# We read the 4x3 matrix 
	matrix = []
	
	for i in range(4):
	    row = []
	    for j in range(4):
	        num = int(input(f"Enter an integer for position: [{i} ,{j}] ")) #we request the numbers for each position.
	        row.append(num)
	    matrix.append(row)

	print(matrix)

	cont = 0
    summation = 0
	for fil_i in range(len(matrix)): #scroll the matrix (rows and columns) to get the largest number in each row
		row_major = 0
		
		for col_j in range(len(matrix[fil_i])): 
			row = matrix[fil_i][col_j].

			if row > row_major: #compare for row_major
				row_major = row
				
		print(f"The row major of row {fil_i} is: {row_major}") #print row and row major

		summation += row_major #perform summation
		cont += 1 #count how many times it is summed
		average = summation // cont #average #average
  
	print(f"The average of the largest numbers in each row is: {average}") #print average
	#print(cont)
	
	

except ValueError:
	print("The entered data must be numeric") 