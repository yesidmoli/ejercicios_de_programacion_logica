"""Read 10 integers, store them in a list, and determine if the average integer is stored in the list.
of this data is stored in the list. """


try:
    numbers = [] #create the list to store the entered numbers.
    
    #create a loop to get the 10 numbers
    for i in range(10):

        list.append(int(input("Enter an integer "))) #request and add the numbers to the list.

    #create two variables to get the average
    average = 0
    sum = 0
    #we run through the list to get the average
    for j in range(len(numbers)):

        sum += numbers[j]
        average = sum // len(numbers)

    print(f"Original list {numbers}") 

    if average == numbers[j]: #condition to know if the average is in the list
    	print(f"The average that is: {average} is in the list") #yes, if we print.
    else:
    	print(f"The average that is: {average} is not in the list") #otherwise.
    	
   
except ValueError:
    print("The entered data must be numeric").