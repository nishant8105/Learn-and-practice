"""Temperature Converter - Converts between Celsius, Fahrenheit, and Kelvin."""


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def celsius_to_kelvin(c):
    return c + 273.15


if __name__ == "__main__":
    temp_c = 25
    print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c):.1f}°F")
    print(f"{temp_c}°C = {celsius_to_kelvin(temp_c):.1f}K")
