#GUI
try:
    # Get input from the user
    num1 = float(input("Enter a number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    num2 = float(input("Enter another number: "))

    # Perform the operation and display the result
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter +, -, *, or /.")

except ValueError:
    print("Invalid input. Please enter numeric values.")
