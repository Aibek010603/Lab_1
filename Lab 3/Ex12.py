def is_palindrome(s):
   
    cleaned_s = ''.join(s.split()).lower()

    return cleaned_s == cleaned_s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
