"""25. Read two 4x5 integer matrices and determine whether the largest prime number in one of the matrices is also the largest prime number in the other matrix.
matrices is also the largest prime number in the other matrix."""

try:
	print(" Enter the elements for the first matrix.")
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
 
	prime_major1 = 0

	for i in range(4): #scroll matrix1 to get the prime 
		for j in range(5): 

			num1 = matrix1[i][j] #assign matrix1 to a variable num2.
			prime = True #initialize a variable to true

			if num1 < 2: # numbers less than 2 are not primes
				prime = False
				
			else:
				#we get the primes of the first array.
				for primes in range(2, (num1 // 2)+1): #create the cycle to find out if primes is divisible by any number 
					if num1 % primes == 0: #if when modulating it is equal to 0 it is not prime
						prime = False #change to false
						break

			if primo and num1 > prime_major1: #compare to get the largest prime
					prime_major1 = num1

	major_prime2 = 0
	for i in range(4): #we shift matrix 2 to get the prime 
		for j in range(5): 

			num2 = matrix2[i][j] #assign to a variable num2, the matrix2.
			prime = True #initialize a variable to true

			if num2 < 2: # numbers less than 2 are not primes
				prime = False
				
			else:
				#we get the primes of the second matrix.
for primes in range(2, ( num2 // 2)+1): #create the cycle to know if primes is divisible by some number 
					if num2 % primes == 0: #if when modulating it is equal to 0 it is not prime
						prime = False #change to false
						break

			if primo and num2 > major_prime2: #compare to get the greater prime
					major_prime2 = num2

			
	print(" ************************************************* ")
	print(f"Largest prime first matrix {prime_major1}") #if we want to print the largest primes of each matrix
	print(f"Largest second prime matrix {major_prime2}")

	if prime_major1 == major_prime2: #if the greatest prime of the first matrix is equal to the greatest of the second matrix
		print(f" The largest primes of the matrices are equal").
	else:
		print(f" The largest primes of the arrays are not equal ") #otherwise.

except ValueError:
	print("The input must be numeric") 