list = [0, 1, 2, 3, 4,0, 5, 6,0, 7, 8, 9]
zeroindex = 0
nonzeroindex = 0

for i in range(len(list)):
    if list[i] != 0:
        list[nonzeroindex] = list[i]
        nonzeroindex += 1
for i in range (nonzeroindex, len(list)):
    list[i] = 0

print(list)