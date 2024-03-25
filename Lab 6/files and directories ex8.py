import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File {path} deleted successfully.")
        else:
            print(f"Error: No write access to {path}.")
    else:
        print(f"Error: File {path} does not exist.")

file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)