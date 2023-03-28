"""Read 10 integers, store them in a list, and determine which numbers are multiples of 5 and in which positions they are in.
multiples of 5 and in which positions they are."""


try:
    numbers = [] #create the list to store the entered numbers.
    positions = []
    

    #create a cycle to get the 10 numbers
    for i in range(10):
        numeros.append(int(input("Enter an integer "))) #add the numbers to the list.

    for i in range(len(numbers)): #scroll through the list 
        if numbers[i] % 5 == 0: #condition to know which numbers are multiples of 5
            positions.append(i) #those that meet the condition we add them to another list

    if len(positions) > 0: #condition to know if there are numbers in the list.

        print(f"original list {numbers}")
        print(f"Multiples of 5 are in the positions {positions}") #print positions
    else:
        print("There are no multiplies of 5") #otherwise. 
   
except ValueError:
    print("The entered data must be numeric") 