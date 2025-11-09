import math

# Get the radius from the user
try:
    radius = float(input("Enter the radius of the circle: "))
except ValueError:
    print("Invalid input. Please enter a numerical value for the radius.")
    exit()

# Check if the radius is non-negative
if radius < 0:
    print("Radius cannot be negative. Please enter a positive value.")
else:
    # Calculate the area and circumference
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius

    # Display the results
    print(f"The area of the circle with radius {radius} is: {area:.2f}")
    print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")