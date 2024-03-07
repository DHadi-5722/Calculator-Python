# Function to get a valid numeric input from the user
def get_number_from_user():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to get a valid operation from the user
def get_operation_from_user():
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid input. Please enter a valid operation.")

# Function to perform the calculation based on the operation
def perform_calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            exit(1)

# Display a welcome message
print("Simple Calculator")

# Prompt user for the first number
num1 = get_number_from_user()

# Prompt user for the operation
operation = get_operation_from_user()

# Prompt user for the second number
num2 = get_number_from_user()

# Perform the calculation based on the operation
result = perform_calculation(num1, num2, operation)

# Display the result
print(f"Result: {num1} {operation} {num2} = {result}")
