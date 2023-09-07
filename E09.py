import random

playAgain = True
while playAgain:
    ans = random.randint(1, 9)
    attempts = 1
    print("Guess the special number between 1 and 9 to win.")
    guessed = False
    while not guessed:
        guess = int(input("Enter your guess: "))
        if guess > ans:
            print("Sorry, you guessed too high!")
            attempts += 1
        elif guess < ans:
            print("Sorry, you guessed too low!")
            attempts += 1
        else:
            print("Wow! Exactly right!")
            guessed = True
    print(f"It took you {attempts} attempt(s) to guess the number.")
    replay = input(
        "Type 'exit' to exit the game otherwise press enter: ").lower()
    if replay == "exit":
        playAgain = False
