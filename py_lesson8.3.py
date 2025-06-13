def find_unique_value(values):
    original = []
    copy = []
    for value in values:
        if value in copy:
            continue
        if value in original:
            original.remove(value)
            copy.append(value)
        else:
            original.append(value)


    return original


values = list(input("Insert your values: "))

print(find_unique_value(values))