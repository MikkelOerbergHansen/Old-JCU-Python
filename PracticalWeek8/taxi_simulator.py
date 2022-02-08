from silver_service_taxi import SilverServiceTaxi
from taxi_modified import TaxiModified


def main():
    print("Let's Drive")
    taxis = [TaxiModified("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    my_taxi = None
    main_menu(taxis, bill_to_date, my_taxi)


def main_menu(taxis, bill_to_date, my_taxi):
    while True:
        menu = """
C - Choose a taxi
D - Drive
Q - Quit"""
        print(menu)
        choice = input(">>> ").upper()
        choice = error_check(choice)

        if choice == "C":
            choice = ""
            my_taxi = list_taxis(taxis)
            bill_to_date = bill_to_date
            print("Bill to date ${:.2f}".format(bill_to_date))

        if choice == "D":
            choice = ""
            if my_taxi is None:
                print("please select a taxi first")
                main_menu(taxis, bill_to_date, my_taxi)
            else:
                drive_a_taxi(my_taxi)
                bill_to_date = bill_to_date + my_taxi.get_fare()
                print("Bill to date ${:.2f}".format(bill_to_date))

        if choice == "Q":
            print("have a nice day :)")
            print("Total Cost is: ${:.2f}".format(bill_to_date))
            print("Taxis are now:")
            list_index = 1
            for taxi in taxis:
                print("{}".format(list_index), taxi)
                list_index += 1
            raise SystemExit(0)


def error_check(choice):
    while choice != "Q" and choice != "C" and choice != "D":
        print("wrong input. please try again")
        choice = input(">>> ").upper()
    return choice


def list_taxis(taxis):
    list_index = 1
    print("taxis available:")
    for taxi in taxis:
            print("{}".format(list_index), taxi)
            list_index += 1
    chosen_taxi = input("Choose your taxi: ")
    while int(chosen_taxi) > len(taxis) or int(chosen_taxi) < 1:
        chosen_taxi = input("Wrong input....Please select a taxi: ")
    return taxis[int(chosen_taxi) - 1]


def drive_a_taxi(my_taxi):
    distance = input("Drive how far? ")
    while int(distance) <= 0:
        distance = input("distance cannot be smaller than or equal to zero. please try again: ")
    trip_price = int(distance) * my_taxi.price_per_km
    print("Your {} trip cost you ${:.2f}".format(my_taxi.name, trip_price))
    my_taxi.drive(int(distance))
    return my_taxi


if __name__ == '__main__':
    main()
