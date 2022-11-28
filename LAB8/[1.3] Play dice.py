# [1.3] Play dice

import random
NUMBER_OF_LIST = 20
# dice_list = [1, 2, 5, 5, 3, 1, 2, 4, 3, 2, 2, 2, 2, 3, 6, 5, 5, 6, 3, 1]


def generate_a_list(list_length):
    my_list = []
    for i in range(list_length):
        my_list.append(random.randint(1, 6))
    return my_list


def find_max_length(my_list):
    new_list = []
    old_counter, new_counter = 0, 0
    for i in range(len(my_list)-1):
        if my_list[i] == my_list[i+1]:
            new_list.append(my_list[i])

    for i in range(len(new_list) - 1):
        if new_list[i] == new_list[i+1]:
            old_counter = old_counter + 1
            if old_counter > new_counter:
                new_counter = old_counter
    return old_counter+2


def write_last_situation(my_list, max_length):
    copy_list = my_list
    for i in range(len(my_list)-max_length):
        if my_list[i] == my_list[i+max_length-1] and my_list[i] == my_list[i+max_length-2] and\
                my_list[i] == my_list[i+1]:
            copy_list.insert(i+max_length, ")")
            copy_list.insert(i, "(")
            break
    return copy_list


def main():
    dice_list = generate_a_list(NUMBER_OF_LIST)
    print(dice_list)
    find_max_length(dice_list)
    dice_list_last = write_last_situation(dice_list, find_max_length(dice_list))
    print(*dice_list_last, sep=" ")


if __name__ == '__main__':
    main()