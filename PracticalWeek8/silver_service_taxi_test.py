from silver_service_taxi import SilverServiceTaxi


hummer_taxi = SilverServiceTaxi("hummer", 200, 4)
print(hummer_taxi)


limo_taxi = SilverServiceTaxi("limo", 100, 2)
limo_taxi.drive(18)
print(limo_taxi)
print(limo_taxi.get_fare())


test_taxi = SilverServiceTaxi("limo", 100, 2)
print(test_taxi.get_fare())