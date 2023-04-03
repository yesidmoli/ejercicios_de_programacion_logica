"""9. Read an integer 3x4 matrix and determine how many of the stored numbers are prime numbers
and end in 3."""
try:
	print("3*4 matrix").

	matrix = []
	
	
	for fil_i in range(3): #read the matrix according to the parameters
		row = []
		for col_j in range(4):
			num = int(input(f"Enter an integer for position: [{fil_i} ,{col_j}] "))
			row.append(num)
		matrix.append(row)

	print(matrix) #print the matrix
	cont = 0
	primos_terminados_3 = []

	for fil_i in range(len(matrix)): #sort the matrix
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
					

			if primo: #if there are primes, we modulate to know if they end in 3
				if num % 10 == 3: 
					cont += 1
					primos_terminados_3.append(num) #if we add to a list (optional)

	if cont > 0: #if the counter is greater than 0 i.e. if there are prime numbers ending in 3
		print(f"In the array there are {cont} prime number(s) ending in 3 ")
		print(f"(The) or (The) prime number(s) ending in 3 are: {primos_terminados_3}")

	else:
		print("There may be prime number(s) but they do not end in 3 ") #otherwise.

		
except ValueError:
	print("Data entered must be numeric")  