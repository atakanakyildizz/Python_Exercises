# [1.2]

my_string = "adeesfADAADFasdafs"

def main():
#   my_string = input("Enter your string: ")
    second_question = []
    print(f"Capitalize = {my_string.capitalize()}")
    for i in range(len(my_string)):
        if i % 2 == 0:
            second_question.append(my_string[i])
    print(f"Even posiitions in my string {second_question}")

    my_list = list(my_string.lower())
    for i in range(len(my_string)):
        if my_list[i] == "a" or my_list[i] == "e" or\
                my_list[i] == "i" or my_list[i] == "o" or my_list[i] == "u":
            my_list[i] =  "_"
    print("".join(my_list))

if __name__ == '__main__':
    main()
