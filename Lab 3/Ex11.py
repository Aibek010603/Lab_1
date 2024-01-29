def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst

original_list = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
new_list = unique_elements(original_list)
print(f"Original list: {original_list}")
print(f"List with unique elements: {new_list}")
