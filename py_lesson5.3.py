import string

initial = input("Please type your text to turn it into a hashtag: ")
'''
for char in initial:
    if string.punctuation in char:
        initial = initial.replace(char, '')
'''
if len(initial) > 139:
    initial = initial[:139]

words = initial.split()
capitals = [word.title() for word in words]


w_punct = ''.join(capitals)
result = ''.join(char for char in w_punct if char not in string.punctuation)
print("#" + result)