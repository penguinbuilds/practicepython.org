import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("Common elements in given lists:", list(set(a) & set(b)))

c = random.sample(range(0, 100), 8)
d = random.sample(range(0, 100), 10)

print("Randomly generated list 1:", c)
print("Randomly generated list 2:", d)

print("Common elements among randomly generated lists:", list(set(c) & set(d)))
