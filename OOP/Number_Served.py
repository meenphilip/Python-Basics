class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"Restaurant name: {self.name} and it's a {self.cuisine_type}"
        print(msg)

    def open_restaurant(self):
        print(self.name+" opens at 7:00 am")

        # modify default value via method
    def set_number_served(self, served_customers):
        if served_customers >= self.number_served:
            self.number_served = served_customers
            print("The number of customers served : "+str(served_customers))
        else:
            print("You can't rool back the number of customers served")

    # Incrementing an Attribute’s Value Through a Method
    def increment_number_served(self, increase_customers):
        self.number_served += increase_customers

    def get_customers_serverd(self):
        print("The number of customers served: " + str(self.number_served))


restaurant = Restaurant("Big Knife", "Turkey Cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# print("The number of served customers: "+str(restaurant.number_served))

# change the value directly
# restaurant.number_served = 6
# print("The number of customers served : "+str(restaurant.number_served))

restaurant.set_number_served(40)

restaurant.increment_number_served(56)
restaurant.get_customers_serverd()
