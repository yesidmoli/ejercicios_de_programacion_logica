"""Display the first 20 multiples of 3."""

try:
	
	print(f "The first 20 multiples of 3 are: ").

	for i in range(1, 20+1): #run the loop by giving the parameters 
			
			print(i*3) #print the result

except ValueError:
	print("The entered data must be numeric")