
from taxi import Taxi
from taxi_modified import TaxiModified

prius_1 = Taxi("Prius 1", 100, 1.23)
prius_1.drive(40)
print(prius_1)
print(prius_1.get_fare())

prius_1.start_fare()
prius_1.drive(100)
print(prius_1)          # out of fuel
print(prius_1.get_fare())

# # # test again with class variable

prius_1 = TaxiModified("Prius 1", 100)
prius_1.drive(40)
print(prius_1)
print(prius_1.get_fare())

prius_1.start_fare()
prius_1.drive(100)
print(prius_1)          # same output
print(prius_1.get_fare())


