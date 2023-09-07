a = input("Enter a string with multiple words: ")


def reverse(a):
    b = a.split()
    for i in range(1, (len(b)+1)):
        print(b[-i], end=' ')
    print("")


reverse(a)
