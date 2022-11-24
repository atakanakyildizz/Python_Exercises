# [2.1]

def main():
    alfa = 32310901
    beta = 1729
    m = 224
    r = int(input("Enter the initial value for r: "))
    for i in range(100):
        r = (alfa*r+beta) % m
        print(r)


if __name__ == '__main__':
    main()
