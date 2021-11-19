def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


fahrenheit = input("Enter a temperature in degrees F: ")
celsius = convert_to_celsius(float(fahrenheit))

print(f"{fahrenheit} degrees F = {celsius:.2f} degrees C")


celsius = input("Enter a temperature in degrees C: ")
fahrenheit = convert_to_fahrenheit(float(celsius))

print(f"{celsius} degrees C = {fahrenheit:.2f} degrees F")
