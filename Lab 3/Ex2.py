def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
centigrade = fahrenheit_to_centigrade(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {centigrade} degrees Centigrade")
