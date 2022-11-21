# [07.2.1] Measurement noise
import random


def random20number(a):
    for i in range(20):
        a.append(random.randint(0, 99))
    return a


def mean_of_the_list(name_of_list):
    total = 0
    for i in range(len(name_of_list)):
        total = total + name_of_list[i]
    return total/len(name_of_list)


def measurment_noise(the_list,mean_of_the_list):
    for i in range(len(the_list)):
        the_list[i] = mean_of_the_list
    return the_list
def main():
    my_list = []
    my_list = random20number(my_list)

    print(f"List: {my_list}\n"
          f"Length: {len(my_list)}\n"
          f"Mean of list: {mean_of_the_list(my_list)}\n"
          f"My final list is {measurment_noise(my_list,mean_of_the_list(my_list))}")


main()
