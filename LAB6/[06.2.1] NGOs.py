# [06.2.1] NGOs

def calculating_subsity():
    annual_income = int(input("Enter the annual income: "))
    number_of_kids = int(input("Enter the number of kids: "))
    if 30000 < annual_income < 40000 and number_of_kids > 3:
        print(f"Subsity is {number_of_kids} x $1000 = ${number_of_kids * 1000}")
    elif 20000 < annual_income < 30000 and number_of_kids > 2:
        print(f"Subsity is {number_of_kids} x $1500 = ${number_of_kids * 1500}")
    elif annual_income < 20000:
        print(f"Subsity is {number_of_kids} x $2000 = ${number_of_kids * 2000}")
    else:
        print("Do not gain anything :(")


def main():
    a = 0
    while a != -1:
        calculating_subsity()
        a = int(input("If you want to exit press -1: "))
    print("Thank You ")


if __name__ == "__main__":
    main()
