import string

margins = input("Please insert two letters through a '-': ")

start, end = margins.split('-')
start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)

resut = string.ascii_letters[start_index:end_index+1]
print(resut)