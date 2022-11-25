# [07.1.7] Sum without the minimum.
import random


def random20number(a):
    for i in range(20):
        a.append(random.randint(0, 99))
        a = sorted(a)
    return a


def sum_without_smallest(v):
    a = random20number(v)
    if a[0] == a[1]:
        a.pop(1)
        a.pop(0)
    else:
        a.pop(0)
    print(f"List: {a}\nLength: {len(a)}")


def main():
    my_list = []
    sum_without_smallest(my_list)


if __name__ == '__main__':
    main()
