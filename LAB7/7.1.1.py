
def main():
    a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    b = []

    for i in range(len(a)):
        if (i % 2) == 1:
            b.append((-1*a[i]))
        else:
            b.append(a[i])
    total = 0

    for i in range(len(b)):
        total = total + b[i]

    print(f"list = {b}")
    print(f"total is = {total}")


if __name__ == '__main__':
    main()
