"""Read 2 whole numbers and determine which of the two has the most prime digits.
prime."""

try:
    num1 = int(input("Enter the first integer "))
    num2 = int(input("Enter the second integer "))
    counter_1 = 0
    counter_2 = 0


    while num1 != 0:
        digit_1 = num1 % 10
        num1 //= 10
        counter_1 += 1

       
    while num2 != 0:
        digit_2 = num2 % 10
        num2 //= 10
        counter_2 += 1

    if counter_1 > counter_2 :
        print("First number has more digits than the second number")
   
    if counter_2 > counter_1:
         print("The second number has more digits than the first number ")

    else:
        print("the two numbers have the same amount of digits ")

                  

except ValueError:
    print("The entered data must be numeric")