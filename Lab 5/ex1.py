import re

file_path = r'C:\Users\Damir\OneDrive\Рабочий стол\row.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

pattern = 'ab*'

matches = re.findall(pattern, data)
for match in matches:
    print(match)