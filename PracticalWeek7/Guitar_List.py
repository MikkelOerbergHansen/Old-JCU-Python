"""
practical 07 do from scratch exercise
"""
from Guitars import Guitar
import csv


def main():
    print("your personal guitar list")
    guitars = load_guitars()
    add_new_guitar(guitars)


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


def list_guitars(guitars):
    list_index = 1
    for guitar in guitars:
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} ({})".format(
            list_index, guitar.name, guitar.year, guitar.cost,
            "vintage" if (guitar.is_vintage() is True) else ""))
        list_index += 1


def add_new_guitar(guitars):
    while True:
        name = input("name: ")
        year = input("Year: ")
        cost = input("Cost: ")
        if not name:
            if not year:
                if not cost:
                    list_guitars(guitars)
                    raise SystemExit(0)
        else:
            new_guitar = Guitar(name, int(year), int(cost))
            guitars.append(new_guitar)
            print("{} ({}): {} added to guitar list".format(name, year, cost))


if __name__ == '__main__':
        main()
