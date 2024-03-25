import time
from math import sqrt

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
input_number = 25100
input_milliseconds = 2123
square_root_after_milliseconds(input_number, input_milliseconds)