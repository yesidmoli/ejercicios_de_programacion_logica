"Display on screen all even numbers between 20 and 200."

try:

	for i in range(20,200+1): #we iterate through the cycle giving the parameters requested 

		if i % 2 == 0: #check if the number is even

			print (i) #print the result
except ValueError:
	print("The entered data must be numeric")