"""Read 10 integers, store them in a list and determine how many of the stored data are multiples of 3
stored are multiples of 3."""

try:
    numbers = [] #create the list to store the entered numbers.
    cont = 0
    
    #create a cycle to get the 10 numbers
    for i in range(10):

        numeros.append(int(input("Enter an integer "))) #request and add the numbers to the list.

        if numbers[i] % 3 == 0: #condition to know which numbers are multiplies of 3
        	cont += 1 #we count how many there are

    print(f"In the list there are {cont} data that are multiplies of 3")
 
except ValueError:
    print("The entered data must be numeric") 