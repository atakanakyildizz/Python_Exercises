# [06.2.2] Roman Numbers

def making_roman_numbers(number):
    if number == "M":
        number = 1000
    elif number == "C":
        number = 100
    elif number == "L":
        number = 50
    elif number == "X":
        number = 10
    elif number == "V":
        number = 5
    elif number == "I":
        number = 1
    return int(number)


def main():
    total = 0
    s = "MCMLXXVIII"
    print(s)
    while len(s) > 0:
        if len(s) == 1 or making_roman_numbers(s[0]) >= making_roman_numbers(s[1]):
            total = total + making_roman_numbers(s[0])
            s = s[1:]
        else:
            diffrence = making_roman_numbers(s[1])-making_roman_numbers(s[0])
            total = total + diffrence
            s = s[1:]
    print(s, total)


if __name__ == "__main__":
    main()
