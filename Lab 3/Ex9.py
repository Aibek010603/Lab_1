def spy_game(nums):
    code = [0, 0, 7, 'x']  #'x' is used as a marker 
    for num in nums:
        if num == code[0]:  
            code.pop(0)  #the first element was removed if it matches
        if not code:  
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  #True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  #True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  #False
