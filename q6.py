def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide_numbers(10, 2))  
print(divide_numbers(10, 0))  
