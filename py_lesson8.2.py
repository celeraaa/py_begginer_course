def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input("Insert your word to check for palindrome: ")
print(is_palindrome(word))