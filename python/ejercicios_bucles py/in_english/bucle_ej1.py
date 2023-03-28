"""Read an integer, display all integers between 1 and the number entered"""
try:
    num = int(input("Enter an integer: ")) # capture the number

    for i in range(1, num+1, 1): # iterate over the entered number
        print(i) # print each integer

except ValueError:
    print("Error: Input is not a valid integer")
