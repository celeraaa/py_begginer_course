while True :
    char = input("Press q to quit or input your desired operator (+,-,*,/) to continue: ")
    if char.lower == "q":
        break

    elif char not in '+, -, /, *':
        print("Invalid input, please try again")
        continue

    num1 = float(input("Please insert your first digit: "))
    num2 = float(input("Please input your second digit: "))
    result = 0


    if char == '+':
        result = num1 + num2
    elif char == '-':
        result = num1 - num2
    elif char == '*':
        result = num1 * num2
    elif char == '/':
        if num2 == 0:
            print("This calculator wont let you divide by zero, please reconsider your choice")
            continue
        else:
            result = num1 / num2

    print("Your result is:", (result))

