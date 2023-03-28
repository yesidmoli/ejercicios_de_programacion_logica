"""8. Read 10 integers, store them in a list, and determine in which positions the numbers ending in 4 are found.
are the numbers ending in 4. """

try: #create empty list 
	numbers = [] 
	ended_list_4 = []
	

	for i in range(10): #create a loop to get the numbers and store them in a list

		num = int(input("Enter a number: "))

		numeros.append(num)

		"""if num % 10 == 4:

			finished_list_4.append(i)"""""


	

	for j in range(len(numbers)): #create a loop to go through the list and determine which numbers end in 4


		if numbers[j] % 10 == 4: #condition by modulating what is in j to get the last position of the number stored in the list.

			lista_terminados_4.append(j) #if the condition is fulfilled we add to the list the numbers ending in 4



	print(f"original list {numbers}")
	print(f"the positions of 4 are found {terminal_list_4} ") #print the positions


except ValueError:
	print("Data entered must be numeric")