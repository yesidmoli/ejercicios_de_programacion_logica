"""Read 10 integers, store them in a list, and determine where in the list is the largest even number read.
the largest even number read. """

try:
	#numbers = [] #create an empty list.

	#create two variables initialized to 0 to store the position and the largest even number.
	pos = 0  
	major = 0

	for i in range(10): #create a loop to input the numbers to be added in the list

		num = int(input("Enter the integer number "))

		numbers.append(num)

	for j in range(len(numbers)): #create another loop to get the position of the largest number 

		num = numbers[j]

		if (num % 2 == 0): #condition to know which is the largest even number 

			if num > greater:

				greater = num
				pos = j

	print(numbers)
	print(f"The largest even number which is {major} is at position {pos}") #print results


except ValueError:
	print("Data must be numeric")