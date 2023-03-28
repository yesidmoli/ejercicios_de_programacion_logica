"""Read two numbers and display all numbers ending in 4 between them."""
try:
    num1 = int(input("Enter the first integer: ")) #capture the two numbers
    num2 = int(input("Enter the second integer: "))

    
    for i in range(num1, num2+1): #loop through to obtain the numbers between the two ranges
        if i % 10 == 4: #check if the numbers end in 4
            print(i) #if the condition is met, print the numbers ending in 4
except ValueError:
    print("The entered data must be numerical.")





