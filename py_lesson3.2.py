num = [1, 2, 3, 4, 5]
lstnum = 0

if num:
    lstnum = num[-1]
    num.insert(0, lstnum)
    num.pop(-1)

print(num)