# Program for perimeter and Area#
try:
    side = float(input("Enter the side length of the square: "))

    if side < 0:
        print("Side length cannot be negative. Please enter a positive value.")
    else:
        perimeter = 4 * side

        area = side * side

        print(f"The perimeter of the square is: {perimeter}")
        print(f"The area of the square is: {area}")

except ValueError:
    print("Invalid input. Please enter a numerical value for the side length.")