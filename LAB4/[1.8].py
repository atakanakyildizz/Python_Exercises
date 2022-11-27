# [1.7]
sequence_list = []
lenght = 9

def not_in_duplicate_list(sequence, lenght):
    for i in range(lenght):
        new_number = int(input("Enter the number: "))
        sequence.append(new_number)
    temp_list = []

    for i in sequence:
        if i not in temp_list:
            temp_list.append(i)

    return (temp_list)


def main():
    print (not_in_duplicate_list(sequence_list, lenght))


if __name__ == '__main__':
    main()
