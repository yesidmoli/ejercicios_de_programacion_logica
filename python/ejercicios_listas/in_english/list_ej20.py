try:
    numbers = [] # we create an empty list to store the numbers entered.

    # create a loop to get 10 numbers 
    for i in range(10):
        # we ask the user for an integer and add it to the list.
        numbers.append(int(input("Enter an integer ")))

    minor = numbers[0]
    pos = 0

    # we go through the list of numbers
    for i in range(len(numbers)):
        cont_multi = 0 # we initialize a counter. 
        # create another loop to check if i is divisible by any number less than itself
        for j in range(2, (numbers[i] // 2) + 1):

            if numbers[i] % j == 0: # if i is divisible, we increment the counter.
                cont_multi += 1

        if cont_multi == 0: # if no divisors other than 1 and itself were found, then i is prime
            if numbers[i] < minor:
                
                minor = numbers[i] # if it is the first prime number or is smaller than the smallest found so far.
                pos = i # store it as the new smallest prime number and save its position

    # print the original list 
    print(f "original list {numbers}") 

    if smallest == numbers[0]: #if no smallest prime numbers found and smallest remains the same
        print("No prime numbers were found in the list.")
    else:
        print(f"the least prime number is: {minor}") #if found we print the minor and position.
        print(f"the smallest prime number is in position: {pos}")
except ValueError:
     print("The entered data must be numeric")