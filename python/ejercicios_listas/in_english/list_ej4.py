"""4. Load a list of 10 positions with the first 10 elements of the Fibonacci series and display it on the screen.
and display it on the screen. """

try: #create empty list 
	numbers = [] 
	val1 = 0 #create the variables according to fibonacci order
	val2 = 1
	aux = 0



	for i in range(0,10): #create a loop to get the numbers and store them in a list

		
		numbers.append(val1) #add the numbers to the list
		aux = val1 + val2
		val1 = val2
		val2 = aux

		
	print(f"The Fibonacci series is: {numbers}") #print results


except ValueError:
	print("The entered data must be numeric")