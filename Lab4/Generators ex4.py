def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("Enter starting number (a): "))
b = int(input("Enter ending number (b): "))

print("Squares from", a, "to", b, ":")
for square in squares(a, b):
    print(square)