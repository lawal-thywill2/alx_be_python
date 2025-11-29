def perform_operation () :
    """Performs a simple arithmetic operation and returns the result."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation =input("Enter the operation (add,substract,multiply,divide): "). strip().lower()
    if operation == "add":
        return num1 + num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
result = perform_operation()
print(f"Result: {result}")