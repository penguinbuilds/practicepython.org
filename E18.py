import random

ans = random.randint(1000, 9999)

guessed = False
guess = 0


def cows_and_bulls(num):
    global guessed
    global guess
    cows = 0
    bulls = 0

    x = [int(i) for i in str(num)]
    y = [int(j) for j in str(ans)]

    if ans == num:
        print("Correct Answer.")
        guess += 1
        guessed = True
    else:
        for i in range(0, 4):
            if x[i] == y[i]:
                cows += 1
        bulls = len(list(set(x) & set(y)))
        bulls = bulls - cows
        guess += 1
        print(f"{cows} cow(s), {bulls} bull(s)")


def main():
    global num
    while not guessed:
        num = int(input("Guess the 4-digit number: "))
        cows_and_bulls(num)


if __name__ == "__main__":
    main()
