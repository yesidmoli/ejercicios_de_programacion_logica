"""Display the integer average of the first n multiples of 3 for an n number read.
n read."""
try:
	n = int(input("Enter the value of n: "))
	average = 0
	
	for i in range(1, n+1): #we run the loop by giving the parameters 

		average += i * 3 
		
	average //= n

	print(f"The average of the first {n} multiplies of 3 is: {average} ")

			

except ValueError:
	print("The data entered must be numeric")