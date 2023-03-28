"""6. Read two integers and store in a list the first 10 prime numbers between the smallest and largest
between the smallest and the largest. Then display them on the screen."""


try:
	primes = [] #create the empty list.
	cont = 0

	num1 = int(input("Enter the first number to search for the prime numbers ")) # Read two integers
	num2 = int(input("Enter the second number up to which the prime number will be calculated"))

	if num1 < num2: # Find the smallest and largest number
		smallest = num1
		greater = num2
	else:
		minor = num2
		greater = num1


	# Find the prime numbers between minor and major
	for i in range(minor, major +1):

		if i > 1:

			for j in range(2, i):

				if ( i % j) == 0:
					

			else:

				primos.append(i)
				if len(primos) == 10:
					break


	print(primos) #Show the primes found
	

except ValueError:
	print("The data must be numeric")