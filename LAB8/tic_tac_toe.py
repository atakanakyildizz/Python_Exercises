
def make_empty_table(row, column):
    a = [[[] for i in range(row)] for i in range(column)]
    for i in range(row):
        for j in range(column):
            a[i][j] = '_'
    return a


def print_table(row, column, table):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in table]))


def first_player_move(table):
    print("FIRST PLAYER")
    try:
        print("---------")
        print_table(3, 3, table)
        print("---------")

        row = int(input("Enter the ROW number: "))
        column = int(input("Enter the column number: "))
        symbol = input("Enter the symbol (O or X): ")
        if table[row-1][column-1] == '_':
            table[row - 1][column - 1] = symbol
        else:
            print("Please try again")

    except ValueError:
        print("Good BYE !!!")
    return table


def second_player_move(table):
    print("SECOND PLAYER")
    try:
        print("---------")
        print_table(3, 3, table)
        print("---------")

        row = int(input("Enter the ROW number: "))
        column = int(input("Enter the column number: "))
        symbol = input("Enter the symbol (O or X): ")
        if table[row-1][column-1] == '_':
            table[row - 1][column - 1] = symbol
        else:
            print("Please try again")

    except ValueError:
        print("Good BYE !!!")
    return table


def check_winning(table):
    my_return = False
    if (table[0][0]) == "X" or "x":
        if table[0][0] == table[0][1] == table[0][2] or table[0][0] == table[1][1] == table[2][2] or \
                table[0][0] == table[1][0] == table[2][0] or table[0][0] == table[1][0] == table[2][0]:
            my_return = True

    elif table[0][1] == 'X' or "x":
        if table[0][1] == table[1][1] == table[2][1] or table[0][1] == table[1][1] == table[2][1]:
            my_return = True

    elif table[0][2] == 'x' or 'X':
        if table[0][2] == table[1][2] == table[2][2] or \
                table[0][2] == table[1][2] == table[2][2] or table[0][2] == table[1][1] == table[2][0]:
            my_return = True

    elif (table[0][0]) == "O" or "o":
        if table[0][0] == table[0][1] == table[0][2] or table[0][0] == table[1][1] == table[2][2] or \
                table[0][0] == table[1][0] == table[2][0] or table[0][0] == table[1][0] == table[2][0]:
            my_return = True

    elif table[0][1] == 'O' or "o":
        if table[0][1] == table[1][1] == table[2][1] or table[0][1] == table[1][1] == table[2][1]:
            my_return = True

    elif table[0][2] == 'O' or 'o':
        if table[0][2] == table[1][2] == table[2][2] or\
                table[0][2] == table[1][2] == table[2][2] or table[0][2] == table[1][1] == table[2][0]:
            my_return = True


    return my_return


def spaces_in_table(table):
    counter = 0
    my_return = False
    for i in range(3):
        for j in range(3):
            if table[i][j] == "_":
                counter = counter + 1
    return counter


def game():
    table = (make_empty_table(3, 3))

    while True:
        first_player_move(table)
        print_table(3, 3, table)
        if check_winning(table) == True:
            print("First player win\n ")
            break
        if spaces_in_table(table) == 0:
            print("Its draw ")
            break
        second_player_move(table)
        print_table(3, 3, table)
        if check_winning(table) == True:
            print("Second player win\n ")
            break
        if spaces_in_table(table) == 0:
            print("Its draw ")
            break


def main():
    print("If you want to exit play any letter")
    game()


if __name__ == '__main__':
    main()
