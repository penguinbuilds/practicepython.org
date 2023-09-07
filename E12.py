import random

a = random.sample(range(100), 10)


def newList(a):
    b = [a[0], a[-1]]
    return b


print("Random list:", a)
print("New list:", newList(a))
