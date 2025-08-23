import math

print("Supported operations: + , - , * , / , % , ** , !")

while True:
    op = input("\nEnter operator (or 'exit' to quit): ")

    if op.lower() == "exit":
        print("Calculator closed.")
        break

    # Factorial needs only one number
    if op == "!":
        num = int(input("Enter a number: "))
        if num < 0:
            print("Error! Factorial not defined for negative numbers.")
        else:
            print("Result:", math.factorial(num))

    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        try:
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            elif op == "%":
                result = num1 % num2
            elif op == "**":
                result = num1 ** num2
            else:
                result = "Invalid operator!"
            
            print("Result:", result)

        except ZeroDivisionError:
            print("Error! Division or modulus by zero is not allowed.")