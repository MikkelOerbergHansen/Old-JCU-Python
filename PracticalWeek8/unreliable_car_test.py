
from unreliable_car import UnreliableCar

car1 = UnreliableCar("prius", 100, 1)
car1.drive(40)
print(car1)      # prius fails to drive (almost always)


car2 = UnreliableCar("porsche", 100, 100)
car2.drive(40)
print(car2)     # porsche can drive

