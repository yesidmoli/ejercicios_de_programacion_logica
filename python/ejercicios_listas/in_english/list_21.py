"""21. Read 10 whole numbers, store them in a list, and determine in which position is the number whose sum of digits is the greatest. 
the number whose sum of digits is the largest."""


try:
    #numbers = [] #create the list to store the entered numbers.
    

    #create a loop to get the 10 numbers
    for i in range(10):
        numbers.append(int(input("Enter an integer "))) #add the numbers to the list.
    print(f"original list {numbers}") 

    list_sum = [] #initialize variables 
    pos = 0
    greater = 0

    for j in range(len(numbers)): #scroll through the list 
        sum = 0
        num = numbers[j]
        while num > 0: #create a while to get the digits of each number
            sum += num % 10
            num //= 10
        list_sum.append(sum) #the sum we add to the list 
        
        if sum > greater: #compare to find out which sum is greater 
            greater = sum
            pos = j

    
    print(f"The sum of the digits of the numbers entered are: {list_sum}")
    print(f"The largest number of the sum of its digits ({major}) is in position {pos}") #print result
    
except ValueError:
    print("The entered data must be numeric")  
