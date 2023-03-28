"""Read 10 integers, store them in a list and determine which of the stored data are multiples of 3
stored that are multiples of 3."""

try:
    numbers = [] #we create the list to store the entered numbers.
    list_multi = [] #create a list to store the multiplies of 3
    
    #create a loop to obtain the 10 numbers
    for i in range(10):

        numeros.append(int(input("Enter an integer "))) #request and add the numbers to the list.

        if numbers[i] % 3 == 0: #condition to know which are the multiplies of 3

            list_multi.append(numbers[i]) #store the multiplies in a list
    
    if len(list_multi) > 0:

        #we print the list of the multiplies of 3.
        print(f"the data that are multiplies of 3 are: {list_multi}")
    else:
        print("There are no multiplies of 3").
 
except ValueError:
    print("The entered data must be numeric") 