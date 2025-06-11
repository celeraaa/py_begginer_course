def correct_sentence(text):
    text = text.title()
    if text [-1] != ".":
        text = text + "."
    return text


text = correct_sentence(input("Insert your sentence: "))
print(text)