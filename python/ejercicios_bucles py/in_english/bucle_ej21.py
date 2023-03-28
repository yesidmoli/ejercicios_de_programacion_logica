"""Read an integer and determine how much the sum of its digits is equal to."""""
try:
    num = int(input("Enter the integer ")) #capture the number.
    suma = 0
    

    while num != 0: #create the cycle to get the digits and add them together 
    	digit = num % 10
    	sum += digit
    	num //= 10

    print(f"The sum of the digits of the number is: {suma}") #print the result
     

except ValueError:
    print("The entered data must be numeric")