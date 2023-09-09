import random
import secrets


def pass_gen(num):
    password = ''
    a = random.sample(range(33, 127), num)
    b = [chr(x) for x in a]
    for i in b:
        password += str(i)
    return password


def main():
    word_list = ['auroras', 'moonstone', 'saturday', 'honeysuckle', 'deuterium',
                 'spacetime', 'gigapixel', 'carbohydrates', 'adamantium', 'dodecagon']
    password = ""
    match pass_strength:
        case 1:
            password = secrets.choice(word_list)
        case 2:
            password = secrets.choice(word_list) + \
                secrets.choice(word_list)
        case 3:
            password = pass_gen(32)
        case 4:
            password = pass_gen(64)
        case 5:
            password = pass_gen(72)
        case _:
            print("INVALID ARGUMENT.")

    print(f"The password generated for you is: {password}")


pass_strength = int(
    input("On a scale of 1-5, how strong do you want your password to be? "))

if __name__ == "__main__":
    main()
