"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "my Car")
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car(100, "limo")         # Question 1
    limo.add_fuel(20)       # Question 2
    print(limo.fuel)        # Question 3
    limo.drive(115)         # Question 4
    print("odo =", limo.odometer)       # Question 5
    print(limo)             # Question 6

    new_limo = Car(100, "New Limo")     # Question 7
    print(new_limo)


main()
