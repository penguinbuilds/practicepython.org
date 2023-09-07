a = [1, 1, 2, 4, 8, 8, 16, 16, 16, 32, 64, 128,
     256, 256, 512, 512, 512, 512, 1024, 2048]
print("Original list:", a)


def d1(a):
    b = a
    return (set(a) & set(b))


def d2(a):
    c = []
    for a in a:
        if a not in c:
            c.append(a)
    return (c)


print("List without duplicates, using sets:", sorted(list(d1(a))))
print("List without duplicates, using functions:", sorted(list(d2(a))))
