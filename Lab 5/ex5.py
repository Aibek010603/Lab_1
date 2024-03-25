import re

def match_a_to_b():
    file_path = r'C:\Users\Damir\OneDrive\Рабочий стол\row.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    pattern = re.compile(r'a.*b')
    matches = pattern.findall(data)
    return matches

print("Task:", match_a_to_b())