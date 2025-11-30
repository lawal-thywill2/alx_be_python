temperature = float(input("Enter the temperature to convert: "))
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F) ").strip().upper()
FAHRENHEIT_TO_CELSIUS = (temperature - 32) * 5.0/9.0
CELSIUS_TO_FAHRENHEIT = (temperature * 9.0/5.0) + 32
def convert_to_celsius(fahrenheit):
    print(f"{temperature}""°F" " is " f"{FAHRENHEIT_TO_CELSIUS}""°C")
def convert_to_fahrenheit(celsius):
    print(f"{temperature}""°C" " is " f"{CELSIUS_TO_FAHRENHEIT}""°F")
if scale == 'C':
    convert_to_fahrenheit(temperature)
elif scale == 'F':
    convert_to_celsius(temperature)
else:
    print("Invalid temperature. please input a numeric value.")