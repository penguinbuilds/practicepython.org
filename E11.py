num = int(input("Enter a number: "))


def checkPrime(num):
    div = 0
    for i in range(1, num+1):
        if num % i == 0:
            div += 1

    if div == 2:
        print("Entered number is a prime number.")
    else:
        print("Entered number is not a prime number.")


checkPrime(num)
