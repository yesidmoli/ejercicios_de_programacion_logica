"""4. Read a 4x3 integer matrix and determine in which exact positions the prime numbers are located.
prime numbers.""" 
try:
	print("Matrix 4*3")

	matrix = []
	
	
	for fil_i in range(4): #read the matrix according to the parameters
		row = []
		for col_j in range(3):
			num = int(input(f"Enter an integer for position: [{fil_i} ,{col_j}] "))
			row.append(num)
		matrix.append(row)

	print(matrix) #print the matrix
	for fil_i in range(len(matrix)): #sort the array
		for col_j in range(len(matrix[fil_i])):

			num = matrix[fil_i][col_j]
			prime = True #initialize a variable to true

			if num < 2: # numbers less than 2 are not primes
				prime = False
				
			else:

				for primes in range(2, (num // 2)+1): #create cycle to find out if prime is divisible by any number. 
					if matrix[fil_i][col_j] % primes == 0:
						prime = False
						break
					

			if prime:
				print(f"The number {num} is prime and is in position ({fil_i , col_j})") #print the result.
	if prime == 0:
		print("There are no primes") #as no prime was found.

		
except ValueError:
	print("The input must be numeric") 