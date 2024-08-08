# Hacky way to avoid overriding PYTHONPATH or use a package
# Relative import must change (.. vs .) depending where the script is run from
import sys

sys.path.insert(0, ".")

from converters import celsius_to_fahrenheit, fahrenheit_to_celsius


celsius = 0
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
celsius_again = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius_again}°C")
