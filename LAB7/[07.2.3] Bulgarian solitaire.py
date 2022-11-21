# [07.2.3] Bulgarian solitaire
import random


def random_45_cards(list1):
    for i in range(45):
        list1.append(random.randint(0, 99))
    return list1


def my_piles(list1, list2):
    size_piles = random.randint(1, 45)
    for i in range(size_piles):
        a = random.randint(0, size_piles)
        list2.append(list1[a])
    return list2


def each_turn(list1, list2):
    for list2 in list1:
        print(f"The element removed: {list1.pop(random.randint(0, len(list1) - 1))} \n"
              f"Number of cards: {len(list1)}\n"
              f"My list: {list1}")


my_list = []
my_second_list = []

my_list = random_45_cards(my_list)


print(f"listem= {my_list}, \n"
      f"My piles: {my_piles(my_list,my_second_list)}\n")
each_turn(my_list, my_piles(my_list,my_second_list))
