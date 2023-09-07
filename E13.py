limit = int(input(
    "Enter the limit till which you wish to generate the Fibonacci sequence: "))


def fibonacci(num):
    f = [0, 1]
    for i in range(2, num+1):
        f.append(f[i-1] + f[i-2])
    return f


print("Fibonacci sequence:", fibonacci(limit))
