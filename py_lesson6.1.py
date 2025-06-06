from datetime import datetime

initial_time = int(input("Please insert your number of seconds: "))

days, seconds = divmod(initial_time, 86400)
hours, remainder = divmod(seconds, 3600)
minutes,seconds = divmod(remainder, 60)
formatted = (f"{hours:02d}:{minutes:02d}:{seconds:02d}")

if days % 10 == 1 and days % 100 != 11:
    dayz = ("день")
elif days % 10 in [2, 3, 4] and days %100 not in [12, 13, 14]:
    dayz = ("дні")
else:
    dayz = ("днів")


print(f"{days} {dayz} {formatted}")