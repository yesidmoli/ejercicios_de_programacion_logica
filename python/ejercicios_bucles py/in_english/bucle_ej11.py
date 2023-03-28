"""Read a two-digit integer and display on the screen all the integers between one digit and the other.
between one digit and the other."""

try:
	#capture the numbers.
	num1 = int(input("Enter the first integer "))
	num2 = int(input("Enter the second integer "))
	
	print("The integers between {} and {} are: ".format(num1,num2))
	for i in range(num1,num2+1): #we run the loop giving the parameters we are asked for 

		

		print(i) #print result

except ValueError:
	print("The entered data must be numeric")