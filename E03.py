a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    if i < 5:
        b.append(i)

for i in b:
    print(i)

num = int(input("Please enter a number: "))
c = []

for i in a:
    if i < num:
        c.append(i)

for i in c:
    print(i)
