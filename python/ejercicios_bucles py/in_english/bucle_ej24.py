"""Read an integer and determine how much the sum of its even digits is equal to."""""
try:
    num = int(input("Enter an integer ")) #capture the integer number.
    suma = 0
    

    while num != 0: #create a loop, to obtain the digits
        digit = num % 10
        num //= 10

        if digit % 2 == 0: #condition the digits to know which ones are to stop
             suma += digit #if the condition is fulfilled we sum the digits
             
    print(f"The sum of the even digits is: {suma}") #print result

except ValueError:
    print("The entered data must be numeric")