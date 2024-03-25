import re

def camel_case_to_snake_case(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

print("Task 10:", camel_case_to_snake_case("ConvertCamelCaseToSnakeCase"))