def is_even(number):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Please enter a number: "))
print(is_even(num))