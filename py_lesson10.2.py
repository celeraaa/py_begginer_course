import re

sentence = input("Please input your sentence: ")

def first_word(sentence):
    clean_sentence = ""
    for char in sentence:
        if char.isalpha():
            clean_sentence += char
        else:
            clean_sentence += " "
    words = clean_sentence.split()

    if len(words) > 0:
        print(words[0])
    else:
        print("No words here")

print(first_word(sentence))