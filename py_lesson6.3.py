number = int(input("Please insert your number: "))

while number > 9:
    prod = 1
    temp = number
    while temp > 0:
        digit = temp % 10
        prod = prod * digit
        temp = temp // 10

    number = prod

print(number)