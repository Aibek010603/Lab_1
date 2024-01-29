import itertools

def print_permutations(s):
    for p in itertools.permutations(s):
        print(''.join(p))

# Example usage
user_string = input("Enter a string: ")
print_permutations(user_string)
