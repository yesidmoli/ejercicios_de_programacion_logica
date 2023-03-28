"""Read 10 integers, store them in a list, and determine if there is at least one repeated number.
repeated number."""

try:
    # Read 10 integers.
    numbers = []
    for i in range(10):
        number = int(input("Enter an integer number: "))
        numbers.append(number)

    # Check for a repeated number
    repeated = []
    for i in range(len(numbers)):
        repeats = 0
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                repetitions += 1
        if repeats > 0 and numbers[i] not in repeats:
            # if the number is repeated and has not been added to the list of repeats, it means that it is repeated.
            repeats.append(numbers[i])
            print(f"The number {numbers[i]} is repeated {repeats+1} times in the list.")

    if len(repeats) == 0:
        # if there are no repeated numbers in the list.
        print("There are no repeated numbers in the list.")


except ValueError:
    print("Data must be numeric.")