# Prompt the user to enter the temperature in Celsius
try:
    celsius = float(input("Enter temperature in Celsius: "))

    # Apply the conversion formula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32

    # Display the result
    print(f"{celsius}°C is equal to {fahrenheit}°F")

except ValueError:
    print("Invalid input. Please enter a numeric value for temperature.")