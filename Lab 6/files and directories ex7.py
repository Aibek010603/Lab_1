def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())

source_file = input("Enter the path of the source file: ")
destination_file = input("Enter the path of the destination file: ")
copy_file(source_file, destination_file)
print(f"Contents of {source_file} have been copied to {destination_file}.")