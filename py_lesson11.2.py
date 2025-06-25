def generate_cube_number(end):
    n = 1
    while True:
        cube = n ** 3
        if cube >= end:
            break
        yield cube
        n += 1

end = int(input("Please enter the end number: "))
cube_number = generate_cube_number(end)
for value in cube_number:
    print(value, end=" ")
