def calculator():
    print("Simple Calculator")

    num1 = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ")
    num2 = float(input("Second number: "))

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")

calculator()