import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            pass  

generate_files()
print("Text files from A.txt to Z.txt have been generated.")