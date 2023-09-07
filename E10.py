import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("List 1:", a)
print("List 2:", b)
c = []
for a in a:
    if a not in c:
        c.append(a)
print("Common elements:", list(c for c in c if c in b))

d = random.sample(range(100), 8)
e = random.sample(range(100), 10)
print("Random list 1:", d)
print("Random list 2:", e)
f = []
for d in d:
    if a not in f:
        f.append(d)
print("Common elements:", list(f for f in f if f in e))
