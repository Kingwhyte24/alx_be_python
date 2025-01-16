def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    if operation == "subtract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide":
        if num2 == 0.0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    elif num2 == 0:
       raise ValueError("Division by zero is not allowed.")     

if __name__ == "__main__":
    perform_operation()