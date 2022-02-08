
from taxi_modified import TaxiModified


class SilverServiceTaxi(TaxiModified):

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1.00):
        super().__init__(name, fuel)
        self.price_per_km = TaxiModified.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
