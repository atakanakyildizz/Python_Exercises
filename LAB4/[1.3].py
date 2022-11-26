# [1.3]
n = 4


def first_question(x):
#   x = int(input(""Enter the n value: ))
    for a in range(x):
        print(f"{'*' * x}")


def second_question(x):
    for a, b in zip(range(x, 0, -1), range(x)):
        print(f"{(a-1)*' '}{b*'*'}*{b*'*'}")

    for c, d in zip(range(1, x), range(x-2, -1, -1)):
        print(f"{c*' '}{d*'*'}*{d*'*'}")


def main():
    first_question(n)
    print("\n")
    second_question(n)


if __name__ == '__main__':
    main()
