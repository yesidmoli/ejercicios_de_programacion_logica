"""24. Read two 4x5 integer matrices and determine if the largest prime number in one of the matrices is also in the other matrix.
arrays is also found in the other array."""

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

	cont = 0 #counter 
	prime_major = 0

	for i in range(4):  
		for j in range(5): 

			num = matrix1[i][j] #assign to a variable num, the matrix1.
			prime = True #initialize a variable to true

			if num < 2: # numbers less than 2 are not primes
				prime = False
				
			else:
				#we get the primes of the first array.
				for primes in range(2, (num // 2)+1): #create the cycle to know if primes is divisible by some number 
					if num % primes == 0: #if when modulating it is equal to 0 it is not prime
						primo = False #change to false
						break

			if prime and num > prime_major: #compare to obtain the largest prime
					prime_major = num

	for i in range(4):  
		for j in range(5):
			if matrix2[i][j] == prime_major :
					cont += 1	

	print(" ************************************************* ")
	print(f"Prime_major {prime_major}")
	if cont != 0: 
		print(f" The largest prime number {prime_major} of the first matrix is in the second matrix ").
	else:
		print(f" The largest prime number is not found in the second array ") 

except ValueError:
	print("The entered data must be numeric") 