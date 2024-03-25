from functools import reduce

def multiply_numbers(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers)
print("Result of multiplying all numbers in the list:", result)