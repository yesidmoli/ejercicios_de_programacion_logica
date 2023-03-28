"""Write on the screen the result of adding the first 20 multiples of 3."""
try:
	suma = 0
	print(f "The first 20 multiples of 3 are: ")

	"""for i in range(1, 20+1): #we run the loop by giving the parameters 

		sum += i * 3


			
	print(sum) #we print result"""

	for i in range(1, 60+1): #run the cycle by giving parameters 

		if i % 3 == 0:

			suma += i 

			print(i)


			
	print(f" The sum of the multiplies is: {suma}") #print the result

except ValueError:
	print("The entered data must be numeric")