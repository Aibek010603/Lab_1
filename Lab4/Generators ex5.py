def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
print("Counting down from", n, "to 0:")
for num in countdown(n):
    print(num)