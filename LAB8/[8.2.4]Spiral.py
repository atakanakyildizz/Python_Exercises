# [08.2.4] Spiral


def make_spiral(n, table):
    print_table(table)
    counter = 1
    copy_counter = 0
    table[0][0] = f"{counter}"
    for i in range(n):
        for j in range(n):
            if i == 0:
                table[i][j] = f"{counter}"
                counter = counter + 1
                copy_counter = counter

            elif (i+1) % n == 0:
                table[i][j] = f"{copy_counter + i}"
                copy_counter = copy_counter - 1
                counter = counter + 1

            elif (j+1) % n == 0:
                table[i][j] = f"{counter }"
                counter = counter + 1
                copy_counter = counter

            elif j == 0:

                if n == 3:
                    table[i][j] = f"{-i+9}"
                elif n == 4:
                    table[i][j] = f"{-i+13}"
                elif n == 5:
                    table[i][j] = f"{-i+17}"
                elif n == 6:
                    table[i][j] = f"{-i+20}"
                elif n == 7:
                    table[i][j] = f"{-i+25}"
                elif n == 8:
                    table[i][j] = f"{-i+29}"
                copy_counter = copy_counter + 1

    #counter = counter + copy_counter
    print("\n")
    print_table(table)


def print_table(table):
    print('\n'.join(['\t'.join([asd for asd in row]) for row in table]))


def make_empty_table(row, column):
    table = [[[] for i in range(row)] for j in range(column)]
    for i in range(row):
        for j in range(column):
            table[i][j] = "_"
    return table


def main():
    n = int(input('Enter the n value: '))
    table = make_empty_table(n, n)
    make_spiral(n, table)


if __name__ == '__main__':
    main()
