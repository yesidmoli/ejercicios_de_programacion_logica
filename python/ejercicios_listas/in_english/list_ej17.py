"""Read 10 integers, store them in a list, and determine how many negative numbers are in the list.
negative numbers there are."""

try:
    numbers = [] #create the list to store the entered numbers.
    cont = 0
    #create a loop to get the 10 numbers
    for i in range(10):

        numeros.append(int(input("Enter an integer "))) #request and add the numbers to the list.

        if numbers[i] < 0:
        	cont += 1

    if cont > 0:
    	print(f"In the list there are {cont} negative number(s)")
    else:
    	print("All numbers entered are positive ")
	
except ValueError:
    print("The entered data must be numeric") 