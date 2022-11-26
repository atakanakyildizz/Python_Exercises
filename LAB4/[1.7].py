# [1.7]


def the_question(my_string):

    for i in range(len(my_string)):
        print(my_string[i])
    for i in range(len(my_string[1:3])):
        print(my_string[i:i+2])
    for i in range(len(my_string[1:2])):
        print(my_string[i:i+3])


def main():
    the_question("rum")


if __name__ == '__main__':
    main()
