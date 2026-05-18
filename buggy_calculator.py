# buggy_calculator.py

def divide_numbers(numerator, denominator):
    # CRITICAL BUG: Division by zero risk if denominator is 0
    val = numerator / denominator
    
    # Style: Unused variable
    dummy_calculation = numerator * 100
    
    print("The output value is: " + str(val)) # PRINT statement instead of logging
    return val

divide_numbers(100, 0) # CRITICAL BUG: division by zero on run
