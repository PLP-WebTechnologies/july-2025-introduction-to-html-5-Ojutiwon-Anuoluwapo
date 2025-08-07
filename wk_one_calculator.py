# Get inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Function to print result neatly
def print_result(num1, num2, operation, result):
    if isinstance(result, float) and result.is_integer():
        # If result is a float but has no fractional part, show as int
        result_display = int(result)
    else:
        result_display = result
    print(f"{num1} {operation} {num2} = {result_display}")

# Perform the operation and print the result
if operation == '+':
    result = num1 + num2
    print_result(num1, num2, operation, result)
elif operation == '-':
    result = num1 - num2
    print_result(num1, num2, operation, result)
elif operation == '*':
    result = num1 * num2
    print_result(num1, num2, operation, result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print_result(num1, num2, operation, result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
