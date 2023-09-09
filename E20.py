def binary_search(int_list, num):
    present = False

    low = 0
    high = len(int_list)-1

    while low <= high:

        mid = (low + high) // 2

        if int_list[mid] == num:
            present = True
            return present
        elif int_list[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return present


def main():

    str_list = input("Enter a list of numbers: ")
    num = int(input("Enter the number that has to be searched: "))

    input_list = str_list.split()
    int_list = [int(i) for i in input_list]

    int_list.sort()
    result = (binary_search(int_list, num))

    if result:
        print(f"{num} is present in the list.")
    else:
        print(f"{num} is not present in the list.")


if __name__ == "__main__":
    main()
