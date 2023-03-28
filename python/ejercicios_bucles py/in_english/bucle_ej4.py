"""Read two numbers and display all integers between them"""
try:
    num1 = int(input("Enter the first integer: ")) #capture the two numbers
    num2 = int(input("Enter the second integer: "))


    for i in range(num1, num2+1): #iterate over the range

        print(i)
        
except ValueError:
    print("The input must be a numeric value")