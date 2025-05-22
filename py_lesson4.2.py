list = [ ]
if list:
    list2 = sum(list[::2])
    mult = list[-1]
    result = int(list2) * mult
else:
    result = 0

print(result)
