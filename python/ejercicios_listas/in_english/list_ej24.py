"""Read 10 integers, store them in a list, and determine in which position is the number with the most digits.
the number with the most digits is in."""

try:
    # Read 10 integers and store them in a list.
    numbers = []
    for i in range(10):
        number = int(input("Enter an integer number: "))
        numbers.append(number)

    # Determine the number with the most digits and its position in the list
    max_digits = -1
    pos_max_digits = -1

    for i in range(len(numbers)):
        # Convert the number to a string and count its digits.
        num_str = str(numbers[i])
        digits = len(num_str)
        if digits > max_digits:
            # If we find a number with more digits than the previous one, we update it.
            max_digits = digits
            pos_max_digits = i

    # Print the result
    print(f"The number with the most digits ({max_digits} digits) is at position {pos_max_digits} in the list.")

except ValueError:
    print("The entered data must be numeric").