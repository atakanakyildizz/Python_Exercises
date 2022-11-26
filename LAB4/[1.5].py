# [1.5]

def main():
    number = int(input("Enter the number that you want to check: "))
    (check_prime(number))


def check_prime(number):
    counter = 0
    numbers = []
    for i in range(2, number):
        if number % i == 0:
            counter += 1
            numbers.append(i)
    if counter == 0:
        print("Prime number")
    else:
        print("Not A Prime Number")
        print(numbers)


if __name__ == '__main__':
    main()
