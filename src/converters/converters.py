import sys # demo un-used import for linter

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float|int) -> float:
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    celsius = 0
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
    celsius_again = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius_again}°C")
