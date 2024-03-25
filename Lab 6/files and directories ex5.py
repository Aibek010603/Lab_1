def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

filename = input("Enter the name of the file to write to: ")
data = [1, 2, 3, 4, 5]  # Example list to write to the file
write_list_to_file(filename, data)
print(f"The list has been written to {filename}.")