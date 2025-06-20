def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    current = begin
    for i in range(end):
        yield current
        current = func(current)

begin = int(input("Input first element: "))
end = int(input("Input last element: "))

gen = some_gen(begin, end, pow)

for value in gen:
    print(value, end=" ")