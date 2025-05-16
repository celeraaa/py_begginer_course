num1 = float(input("Please insert your first digit: "))
num2 = float(input("Please input your second digit: "))
operation = input("Please input your desired operator (+, -, * or /):")
result = 0

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("This calculator wont let you divide by zero, please reconsider your choice")
    else:
        result = num1 / num2
else:
    print("Invalid operator")


print(result)