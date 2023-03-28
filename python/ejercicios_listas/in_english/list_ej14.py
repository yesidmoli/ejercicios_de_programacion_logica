"""Read 10 integers, store them in a list and determine how many times the integer average of the data within the list is repeated.
the integer average of the data within the list is repeated. """

try:
    numbers = [] #create the list to store the entered numbers.
    cont = 0
    #create a loop to get the 10 numbers
    for i in range(10):

        numeros.append(int(input("Enter an integer "))) #request and add the numbers to the list.

    #create two variables to get the average
    average = 0
    sum = 0
    
    #we run through the list to get the average
    for j in range(len(numbers)):

        sum += numbers[j]
        average = sum // len(numbers)

    print(f"Original list {numbers}") 

    if average == numbers[j]: #condition to know if the average is in the list
        print(f"The average of the list that is: {average} is in the list") #if if if we print

        for k in range(len(numbers)): #run the list again to compare how many times the average is repeated

            if numbers[k] == average:
                cont += 1

        print(f"The average in the list is repeated {cont} times") #print the times it is repeated.
	
    else:
        print(f"The average that is: {average} is not in the list") #otherwise.   

except ValueError:
    print("The entered data must be numeric")