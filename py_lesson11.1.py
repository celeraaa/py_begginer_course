import math

def prime_generator(fin):
    for i in range(2, fin):
        for j in range(2, 1 + int(math.sqrt(i))):
            if not i % j:
                break
        else:
            yield i




fin = int(input("Please enter the end number: "))
primes = prime_generator(fin)
for value in primes:
    print(value, end=" ")