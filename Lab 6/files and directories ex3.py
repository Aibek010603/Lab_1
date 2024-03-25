import os

def check_path(path):
    if os.path.exists(path):
        print("The path exists.")
        
        dirname, filename = os.path.split(path)
        print("Directory:", dirname)
        print("Filename:", filename)
    else:
        print("The path does not exist.")

path = 'C:/Users/Damir/OneDrive/Рабочий стол/row.txt'
check_path(path)