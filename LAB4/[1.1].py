# [1.1]

def main():
    a = int(input("Enter the first value: "))
    print(a)
    b = int(input("Enter the second value: "))
    print(f"{a} + {b} = {a+b}")
    c = int(input("Enter the third value: "))
    print(f"{a} + {b} + {c} = {a+b+c}")
    d = int(input("Enter the fourth value: "))
    print(f"{a} + {b} + {c} + {d} = {d+c+a+b}")


if __name__ == '__main__':
    main()
