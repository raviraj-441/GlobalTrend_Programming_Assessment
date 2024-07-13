def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operator"

print(arithmetic_operation(10, 5, '+'))  
print(arithmetic_operation(10, 0, '/'))  
