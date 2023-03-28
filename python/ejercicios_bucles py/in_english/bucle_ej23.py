"""23.Read a whole number and determine if the sum of its digits is also a prime number.
prime."""

try: #capture the number 
    num = int(input("Enter the integer"))
    suma = 0 #initialize the sum to 0
    

    while num != 0: #we run through a loop to capture the digits
        digit = num % 10 
        suma += digit
        num //= 10

    print(f"The sum of the digits of the number is: {suma}") 

    if suma % 2 != 0: #condition to know if it is prime
        print("The result of the sum is a prime number")
    else:
        print("The result of the sum is not a prime number") #otherwise it is not prime.
     

except ValueError:
    print("The input data must be numeric")