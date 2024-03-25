import re

def insert_spaces_before_capitals(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)

print("Task 9:", insert_spaces_before_capitals("InsertSpacesBeforeCapitals"))