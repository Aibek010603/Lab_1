def even_numbers_generator(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

n = int(input("Enter a number: "))
even_gen = even_numbers_generator(n)
print("Even numbers up to", n, ":", end=" ")
print(*even_gen, sep=", ")