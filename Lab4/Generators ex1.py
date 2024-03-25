def generate_squares(N):
    """Generate squares of numbers up to N."""
    for num in range(1, N + 1):
        yield num ** 2

N = 5
squares_generator = generate_squares(N)

print(f"Squares of numbers up to {N}:")
for square in squares_generator:
    print(square)