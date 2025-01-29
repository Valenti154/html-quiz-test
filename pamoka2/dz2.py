def basic_math(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    print("Basic Math Tests:")
    print(f"5 + 3 = {basic_math(5, 3, '+')}")
    # print(f"10 - 2 = {basic_math(10, 2, '-')}")
    # print(f"4 * 7 = {basic_math(4, 7, '*')}")
    # print(f"8 / 2 = {basic_math(8, 2, '/')}")
    # print(f"8 / 0 = {basic_math(8, 0, '/')} (Error expected)")