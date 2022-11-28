# 1.2] Buffe.r
import random


def main():
    my_list = []
    for i in range(6):
        my_list.append(random.randint(1, 10))
    copy_list = my_list
    print(my_list)

    copy_list.insert(0, my_list[-1])
    print(copy_list)
    copy_list.pop(-1)
    print(copy_list)


if __name__ == '__main__':
    main()
