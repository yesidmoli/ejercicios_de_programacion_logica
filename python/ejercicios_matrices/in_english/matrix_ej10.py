"""10. Read an integer 5x3 matrix and determine in which row is the largest prime number."""""
try:
	print("5*3 matrix").

	matrix = []
	
	
	for fil_i in range(5): #read the matrix according to the parameters
		row = []
		for col_j in range(5):
			num = int(input(f"Enter an integer for position: [{fil_i} ,{col_j}] "))
			row.append(num)
		matrix.append(row)

	print(matrix) #print the matrix
	prime_major = 0
	row = 0
	for fil_i in range(len(matrix)): #sort the matrix
		for col_j in range(len(matrix[fil_i])):

			num = matrix[fil_i][col_j].
			prime = True #initialize a variable to true

			if num < 2: # numbers less than 2 are not primes
				prime = False
				
			else:
				#we get the primes
				for primes in range(2, (num // 2)+1): #create the cycle to find out if primes is divisible by any number 
					if num % primes == 0: #if when modulating it is equal to 0 it is not prime
						prime = False #change to false
						break
			if prime:
				if num > prime_major: #compare to see where the prime number is the largest number
					prime_major = num
					row = fil_i
	if fila != 0: #if the variable fila is different than assigned, there is prime number
		print(f"The largest prime number {prime_major} is in the row {row}")
	else:
		print("No prime numbers were found in the array") #otherwise.
			
except ValueError:
	print("The entered data must be numeric") 