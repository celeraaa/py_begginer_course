def popular_words(text, words):
    text = text.lower().split()
    dict = {}
    for word in words:
        word = word.lower()
        occur = text.count(word)
        dict[word] = occur
    return dict

text = " i love apples apples apples apples apples and bananas"
words = ['apples', 'banana', 'bana', 'app']


print(popular_words(text, words))
