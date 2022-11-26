# [1.6]
number = 30


def main():
    first_n_prime_number(number)


def first_n_prime_number(my_number):
    my_list = []
    for i in range(2, my_number):
        if check_prime(i):
            my_list.append(i)
    print(my_list)


def check_prime(my_number):
    counter = 0
    numbers = []
    for i in range(2, my_number):
        if my_number % i == 0:
            counter += 1
            numbers.append(i)
    if counter == 0:
        solution = True

    else:
        solution = False

    return solution


if __name__ == '__main__':
    main()
