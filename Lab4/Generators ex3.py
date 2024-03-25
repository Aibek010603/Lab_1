def divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("Enter a number: "))
divisible_gen = divisible_by_3_and_4(n)
print("Numbers divisible by 3 and 4 up to", n, ":", end=" ")
print(*divisible_gen, sep=", ")