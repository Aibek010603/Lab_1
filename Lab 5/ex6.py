import re

def replace_with_colon():
    file_path = r'C:\Users\Damir\OneDrive\Рабочий стол\row.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    data = re.sub(r'[ ,.]', ':', data)
    return data

print("Result:", replace_with_colon())