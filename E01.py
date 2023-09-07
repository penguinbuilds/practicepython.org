name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
num = int(input("Please enter the number of times you wish to recieve our message: "))

for i in range(num):
    print(f"Hi {name}, you will turn 100 in the year {2023-age+100}.")
