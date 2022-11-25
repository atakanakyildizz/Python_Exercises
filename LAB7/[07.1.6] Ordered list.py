# [07.1.6] Ordered list

import random


def random20number(a):
    for i in range(20):
        a.append(random.randint(0, 99))
        a = sorted(a)
    print(a)


def main():
    my_list = []
    random20number(my_list)


if __name__ == '__main__':
    main()
