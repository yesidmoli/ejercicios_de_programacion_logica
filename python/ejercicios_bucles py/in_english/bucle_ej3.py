"""Read an integer and show all exact divisors of the number between 1 and the number read."""

try:
    num = int(input("Enter an integer: ")) #capture the number


    for i in range(1,num+1): #iterate through the input number
        
        if num % i == 0: #condition to obtain the exact divisors
            
            print(i)
            
except ValueError:
    print("The entered data must be numeric.")