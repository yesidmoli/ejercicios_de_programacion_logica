"""Read an integer number and determine the sum of all integers between 1 and the number read."""

try:


    num = int(input("Enter an integer number ")) #capture the number
    suma = 0 #define a variable to store the sum, initialized to 0

    for i in range(1,num+1): #iterate over the range of numbers from 1 to num

        suma += i #sum the numbers

    print(f"The sum of all integers is: {suma}") #print the result
except ValueError:
    print("The entered data must be numeric")