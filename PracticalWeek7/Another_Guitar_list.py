"""
practical 07 do from scratch exercise
"""
from Guitars import Guitar
import csv


def main():
    print("you personal guitar list")
    guitars = load_guitars()
    main_menu(guitars)


def load_guitars():
    guitars = []
    with open("PracticalWeek7/the_guitar_list.csv", "r") as file:
        read_guitars = list(csv.reader(file))
        for temp_guitars in read_guitars:
            name = temp_guitars[0]
            year = int(temp_guitars[1])
            cost = float(temp_guitars[2])
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
        print(str(len(guitars)) + " guitars loaded")
        return guitars


def main_menu(guitars):
    while True:
        menu = """
    L - List Guitars
    A - Add a new guitar
    Q - Quit"""
        print(menu)
        choice = input(">>> ").upper()
        choice = error_check(choice)

        if choice == "L":
            choice = ""
            list_guitars(guitars)

        if choice == "A":
            choice = ""
            add_new_guitar(guitars)

        if choice == "Q":
            print("have a nice day :)")
            raise SystemExit(0)


def error_check(choice):
    while choice != "Q" and choice != "L" and choice != "A":
        print("wrong input. please try again")
        choice = input(">>> ").upper()
    return choice


def list_guitars(guitars):
    list_index = 1
    for guitar in guitars:
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} ({})".format(
            list_index, guitar.name, guitar.year, guitar.cost,
            "vintage" if (guitar.is_vintage() is True) else ""))
        list_index += 1


def add_new_guitar(guitars):
    while True:
        try:
            name = input("name: ")
            if not name:
                print("input can not be blank")
                raise ValueError()
            for guitar in guitars:
                if name.lower() == str(guitar.name).lower():
                    print("the guitar is already in the list")
                    raise ValueError()
            break
        except ValueError:
            continue

    while True:
        try:
            year = input("Year: ")
            try:
                year = int(year)
            except ValueError:
                print("invalid input; enter a valid year")
                continue
            if year < 0:
                print("The year must be >= 0")
                raise ValueError()
            if len(str(year)) < 4 or len(str(year)) > 4:
                print("the year must have 4 digits; enter a valid year")
                raise ValueError
            break
        except ValueError:
            continue

    while True:
        try:
            cost = input("Cost: ")
            try:
                cost = float(cost)
            except ValueError:
                print("invalid input; enter a valid cost")
                continue
            if cost < 0:
                print("The cost must be >= 0")
                raise ValueError()
            break
        except ValueError:
            continue

    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print("{} ({}): {} added to guitar list".format(name, year, cost))
    main_menu(guitars)


if __name__ == '__main__':
        main()
