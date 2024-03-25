def all_true_in_tuple(t):
    return all(t)

my_tuple = (True, True, True)
print(all_true_in_tuple(my_tuple))  
my_tuple = (True, False, True)
print(all_true_in_tuple(my_tuple))  