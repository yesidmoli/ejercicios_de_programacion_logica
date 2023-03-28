"""10. Read 10 integers, store them in a list and determine in which positions the numbers with more than 3 digits are found. 
the numbers with more than 3 digits are found."""

try:
	numbers = [] #create list to store the entered numbers.
	positions = [] #create an empty list to store the positions.
	

	for i in range(10): #get the numbers 

		num = int(input("Enter an integer "))

		numeros.append(num) #add the numbers to the list

	for j in range(len(numbers)): #we scroll the list to know the positions of the numbers with more than 3 digits

		
		if numbers[j] > 99: #condition to know who has the most digits

			positions.append(j) #those that meet the condition, we add the position to the list.





	print(numbers)

	if len(positions) > 0: #condition to find out if there are numbers with 3 digits in the list
		print(f"The numbers with more than 3 digits are in the positions: {positions}") #if it is fulfilled we print the result
	else:
		print(" No numbers greater than 3 digits were found") #if not true.


except ValueError:
	print("The entered data must be numeric")