"""Read 10 integers, store them in a list, and determine which number is the smallest.
smallest."""

try:
    #numbers = [] #create the list to store the entered numbers.
    

    #create a cycle to get the 10 numbers
    for i in range(10):

        numeros.append(int(input("Enter an integer "))) #request and add the numbers to the list.

    minor = numbers[0] #initialize minor with the 0 position in the list

    for i in range(len(numbers)): #we scroll the list to determine the smallest number

        if numbers[i] < minor: #condition to know which is minor
            smallest = numbers[i]

    print(f"original list {numbers}") 
    print(f"The smallest number in the list is: {smallest}") #we print the smallest number.
    
except ValueError:
    print("The input must be numeric") 