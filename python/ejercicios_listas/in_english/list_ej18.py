"""Read 10 integers, store them in a list and determine in which positions are the positive numbers.
are the positive numbers. """

try:
    #numbers = [] #create the list to store the entered numbers.
    positions = []
    pos = 0
    #create a loop to get the 10 numbers
    for i in range(10):

        numbers.append(int(input("Enter an integer "))) #request and add the numbers to the list

        if numbers[i] > 0: #condition to know the position of the positives
        	pos = i
        	positions.append(pos) #add the positions to the list

    print(f"original list {numbers}")

    if len(positions) > 0: #if what's in the list of pos is greater than 0
    	print(f"Positive integers are found in positions {positions}") #print
    else:
    	print("There are no positive numbers in the list") #otherwise.
	
except ValueError:
    print("The entered data must be numeric") 