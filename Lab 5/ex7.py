def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_str = "hello_world"
print("Snake case string:", snake_str)
print("Camel case string:", snake_to_camel(snake_str))