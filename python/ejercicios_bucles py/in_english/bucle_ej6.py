"""Read an integer number with 3 digits and display all integers between 1 and each of its digits"""
try:
    num = int(input("Enter the integer number with 3 digits ")) # capture the input number

    
    if num < 100 or num > 999:
        print("The number is not 3 digits")

    else:
        d1 = num // 100
        d2 = (num % 100) // 10
        d3 = num % 10

        print("Numbers of the first digit")
        for i in range(1, d1+1):
            print(i)

        print("Numbers of the second digit")
        for i in range(1, d2+1):
            print(i)
            
        print("Numbers of the third digit")
        for i in range(1, d3+1):
            print(i)
except ValueError:
    print("The input value should be a number")





