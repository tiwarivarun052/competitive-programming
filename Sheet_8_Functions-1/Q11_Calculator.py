# WAPtomake a calculator by using functions.
def calc(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"
print(calc(10, 5, 'add'))