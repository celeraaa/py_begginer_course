def second_index(text, some_string):
    x = text.find(some_string)
    y = text.find(some_string, x + 1)
    if y != -1:
        return y
    else:
        return None

text = input("Insert your text: ")
some_string = input("Insert your letter: ")

print(second_index(text, some_string))