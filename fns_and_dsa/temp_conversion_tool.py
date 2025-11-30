temperature = float(input("Enter the temperature to convert: "))
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F) ").strip().upper()
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 * temperature - 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 * temperature + 32
def convert_to_celsius(fahrenheit):
    print(f"{temperature}""°F" " is " f"{FAHRENHEIT_TO_CELSIUS_FACTOR}""°C")
def convert_to_fahrenheit(celsius):
    print(f"{temperature}""°C" " is " f"{CELSIUS_TO_FAHRENHEIT_FACTOR}""°F")
if scale == 'C':
    convert_to_fahrenheit(temperature)
elif scale == 'F':
     convert_to_celsius(temperature)
else:
    print("Invalid temperature. please input a numeric value.")