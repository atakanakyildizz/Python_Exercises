# [07.1.6] Ordered list

import random

my_list = []


def random20number(a):
    for i in range(20):
        a.append(random.randint(0, 99))
        a = sorted(a)
    print(a)


random20number(my_list)
