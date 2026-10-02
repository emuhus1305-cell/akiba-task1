print("========================================")
print("       TEMPERATURE STATION")
print("========================================")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print()
print(f"Celsius: {celsius}°C")
print(f"Fahrenheit: {fahrenheit}°F")
print()
print("Fahrenheit to Celsius")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

celsius_result = (fahrenheit_input - 32) * 5 / 9

print(f"Fahrenheit: {fahrenheit_input}°F")
print(f"Celsius: {celsius_result}°C")

print("========================================")