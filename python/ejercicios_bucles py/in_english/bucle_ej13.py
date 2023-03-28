"""Read an integer and display all multiples of 5 between 1 and the number read.
read."""

try:
	#capture the number
	num = int(input("Enter the integer number "))
	
	for i in range(1,num+1): #run the loop by giving the parameters 

		if i % 5 == 0: #condition to obtain the multiplies of 5
			
			print(i) #print result

except ValueError:
	print("The entered data must be numeric")