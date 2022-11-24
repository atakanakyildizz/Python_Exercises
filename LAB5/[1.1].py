# LAB5
# [1.1]


def main():
    user_pin = 1234
    counter = 0
    for i in range(3):
        entered_pin = int(input("Enter your pin: "))
        if entered_pin == user_pin:
            print("Your PIN is correct ")
            break
        else:
            print("Your PIN is incorrect")
            counter += 1
    if counter == 3:
        print("Your bank card is blocked")


if __name__ == "__main__":
    main()
