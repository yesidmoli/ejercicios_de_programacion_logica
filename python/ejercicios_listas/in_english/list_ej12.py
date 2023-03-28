"""Read 10 integers, store them in a list, and determine how much the average integer of the data in the list equals.
integer average of the data in the list is equal to. """

try:
    numbers = [] #create the list to store the entered numbers.
    
    #create a loop to get the 10 numbers
    for i in range(10):

        numbers.append(int(input("Enter an integer "))) #add the entered numbers to the list.

    #create two variables to get the average
    average = 0
    sum = 0
    #we run through the list to get the average
    for j in range(len(numbers)):

        sum += numbers[j]
        average = sum // len(numbers)

    print(f"The original list {numbers}") 
    print(f"The average of the integers in the list is: {average} ") #we print the average of the integers



except ValueError:
    print("The input data must be numeric")