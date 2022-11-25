# [07.1.3] Remove the minimum value

my_list = [91, 2, -3, 2]
my_min = 9999999999999999


def remove_min(v):
    myMin = 9999999999999999
    t = 0
    for i in range(len(v)):
        if v[i] < myMin:
            myMin = v[i]
            t = i
    v.pop(t)
    return v


def main():
    print(remove_min(my_list))


if __name__ == '__main__':
    main()
