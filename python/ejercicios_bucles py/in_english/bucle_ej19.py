"""Read an integer and determine if it is prime."""
try:
    num = int(input("Enter the number "))
    

    for i in range(2,num +1): 

        if num % i != 0:
            print(f"The number {num} is prime").
            break
        else:
            print(f"The number {num} is not prime")
            break
     

except ValueError:
    print("The data entered must be numeric")