# [1.4]

def main():
    number_of_tickets = 100
    counter = 0
    while number_of_tickets > 0:
        taken_ticket = int(input("Enter the desired number of tickets: "))
        if taken_ticket <= 4:
            number_of_tickets = number_of_tickets - taken_ticket
            print(f"There are {number_of_tickets} tickets left ")
            counter = counter+1
        else:
            print("You can take buy most 4 tickets")

    print(f"Total numbers of buyers is: {counter}")
    print("Thank you")


if __name__ == '__main__':
    main()
