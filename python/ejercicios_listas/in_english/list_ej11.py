"""Read 10 integers, store them in a list and determine how many of the numbers stored there have less than 3 digits.
have, of those stored there, less than 3 digits. """

try:
	numbers = [] #create list to store the entered numbers.
	minors = [] #create empty list to store positions
	cont = 0

	for i in range(10): #get the numbers 

		num = int(input("Enter an integer"))

		list.append(numenros) #add the numbers to the list

	for j in range(len(numbers)): #we scroll the list to find numbers with less than 3 digits

		
		if numbers[j] < 100: #condition to know who has less digits

			minors.append(numbers[j]) #those that meet the condition we add the position to the list
			cont += 1

	print(numbers)

	if len(minors) > 0: #condition to know if there are numbers less than 3 digits in the list.
		print(f"The numbers with less than 3 digits are: {minors}") #if true we print result
		print(f"the list has {cont} numbers less than 3 digits")
	else:
		print(" No numbers less than 3 digits were found") #if not true.


except ValueError:
	print("Data entered must be numeric")