"""Read an integer and determine how much the integer average of its digits is equal to."""""

try:
    num = int(input("Enter an integer ")) #capture the integer number.
    suma = 0
    average = 0
    counter = 0

    

    while num != 0: #create a loop, to get: 
        digit = num % 10 #the digits
        counter += 1 #number of digits
        num //= 10
        suma += digit #sum
    
    average = suma // counter #we take out the average
        
    print(f"the average of the digits is: {average}") #print result

except ValueError:
    print("The entered data must be numeric")