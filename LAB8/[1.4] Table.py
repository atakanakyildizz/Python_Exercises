# [1.4] Table

m = 3
n = 2


def nice_print(row, column, table):

    for i in range(row):
        for a in range(column):
            print(table)


def table_function():
    table = []
    for i in range(m):
        for a in range(n):
            if i % 3 == 0 :
                print("\n")
            table.append([i, a])
    return (table)


def main():
    print(table_function())
    #nice_print(m, n, table_function())


if __name__ == '__main__':
    main()
