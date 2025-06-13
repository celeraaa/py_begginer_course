def add_one(num):
    num = num + 1
    new_num = (list(str(num)))
    return new_num

num = int(input("Insert your number: "))
print(add_one(num))