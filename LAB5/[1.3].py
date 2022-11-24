# [1.3]

def factorize(number):
    while int(number) != 1:
        for i in range(2, int(number)+1):
            if number % i == 0:
                print(i)
                number = number/i


def main():
    factorize(150)


if __name__ == "__main__":
    main()
