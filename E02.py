A = int(input("Please enter a number: "))

if A % 4 == 0:
    print("The number you entered is even and is divisible by 4.")
else:
    if A % 2 == 0:
        print("The number you have entered is even.")
    else:
        print("The number you have entered is odd.")

num = int(input("Please enter the dividend: "))
check = int(input("Please enter the divisor: "))

if num % check == 0:
    print(f"{check} divides evenly into {num} and the quotient is {int(num/check)}.")
else:
    print(f"{check} does not evenly divide into {num}")
