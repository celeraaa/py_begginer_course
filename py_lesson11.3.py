def is_even(num):
    num = str(num)
    evens = ['0', '2', '4', '6', '8',]
    if num[-1] in evens:
        return True
    else:
        return False

num = input("Please enter a number: ")
print(is_even(num))