try:
    # Get input from the user and convert it to an integer
    decimal_number = int(input("Enter an integer: "))

    hexadecimal_representation = hex(decimal_number)
    binary_representation = bin(decimal_number)

    print(f"The number in hexadecimal is: {hexadecimal_representation}")
    print(f"The number in binary is: {binary_representation}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")