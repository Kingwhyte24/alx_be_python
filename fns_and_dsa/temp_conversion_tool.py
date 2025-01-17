FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    print(f"{fahrenheit}°F is {(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C") 


def convert_to_fahrenheit(celsius):
    # return (celsius + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celsius}°C is {(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32}°F")

temperature = float(input("Enter the temperature to convert: "))
temperature_degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if type(temperature) == float:
    if temperature_degree == 'C':
        convert_to_fahrenheit(temperature)
    elif temperature_degree == 'F':
        convert_to_celsius(temperature)
    else:
        raise ValueError("Enter a valid temperature and unit.")

else:
    raise ValueError("Invalid temperature. Please enter a numeric value.”")