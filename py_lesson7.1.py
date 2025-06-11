def say_hi():
    print(f"Hi! My name is {name} and I`m {age} years old.")

name = input("Insert your name to generate a greeting: ")
age = int(input("Insert your age: "))

assert age > -1, "Sorry, you aint born yet, I cant let you use this program. Wait for a year or something."

say_hi()
