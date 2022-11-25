# [07.1.4] Local highs

my_list = [2, 33, 6, 74, 7, 24]


def local_maksima(mylist):
    a = mylist[0]
    counter = 0
    for i in range(len(mylist)):
        if a < mylist[i]:
            a = mylist[i]
        elif a == mylist[i]:
            counter += 1
    if counter > 1:
        print("There is no local maxima")
    else:
        return a


def main():
    print(f"Local max is = {local_maksima(my_list)}")


if __name__ == '__main__':
    main()
