import random
from pprint import pprint


def make_empty_table(row, column):
    A = [[[] for i in range(row)] for i in range(column)]
    for i in range(row):
        for j in range(column):
            A[i][j] = '_'
    return A


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
    define = True
    if table[0][0] == table[0][1] == table[0][2] or \
            table[0][1] == table[1][1] == table[2][1] or \
            table[0][2] == table[1][2] == table[2][2] or \
            table[0][0] == table[1][0] == table[2][0] or \
            table[0][1] == table[1][1] == table[2][1] or \
            table[0][2] == table[1][2] == table[2][2] or \
            table[0][0] == table[1][1] == table[2][2] or \
            table[0][2] == table[1][1] == table[2][0]:
            define = False
    return define


def game():
    table = (make_empty_table(3, 3))
    first_player_move(table)
    second_player_move(table)

    for i in range(9):
        first_player_move(table)
        print_table(3, 3, table)
        if check_winning(table) == False:
            print("First player win ")
            break
        for a in table:
            if a != ' ':
                break
                break
        second_player_move(table)
        if check_winning(table) == False:
            print("Second player win ")
            break
        for a in table:
            if a != ' ':
                break
                break


def main():
    print("If you want to exit play any letter")
    game()


if __name__ == '__main__':
    main()
