# User se temperature input lena
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Fahrenheit ko Celsius me convert karna
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Result print karna
print(f"Temperature: {fahrenheit}F = {celsius}C")
