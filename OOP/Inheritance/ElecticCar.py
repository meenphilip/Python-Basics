class Car():
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it")

    # Modifying an Attribute’s Value Through a Method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rool back an odometer!")

    # Incrementing an Attribute’s Value Through a Method
    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('Audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement decribing the battery size"""
        print("This car has a "+str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on full charge"
        print(message)


class ElectircCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     """Print a statement decribing the battery size"""
    #     print("This car has a "+str(self.battery_size) + "-kWh battery.")


tesla = ElectircCar('tesla', 'model s', 2016)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
