# bad_code.py
import sys

def calculate_something(x, y):
    # Bug: Division by zero possibility if y is 0
    result = x / y
    
    # Style: unused variable
    unused_var = 100
    
    print("Result is: " + str(result)) # Style: print instead of logging
    return result

calculate_something(10, 0) # Bug: will crash on import/run
