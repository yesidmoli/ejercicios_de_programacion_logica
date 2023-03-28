""" Read two integers and display all the multiples of 5 between the smaller and the larger.
less than and greater than."""

try:
    num1 = int(input("Enter the first number "))
    num2 = int(input("Enter the second number "))
    
    if num1 < num2:

        for i in range(num1, num2+1): #recorrect the loop by giving the parameters. 
            print(i*5)

    elif num2 < num1:
        for i in range(num2, num1+1): #run the loop by giving the parameters 
            print(i*5)

    else:
        print("The two values are equal").
     

except ValueError:
    print("The entered data must be numeric")