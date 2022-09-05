class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"Restaurant name: {self.name} and it's a {self.cuisine_type}"
        print(msg)

    def open_restaurant(self):
        print(self.name+" opens at 7:00 am")


my_rest = Restaurant("Omifoods", "French cuisine")
print("Restaurant Name: " + my_rest.name)
print("Cuisine Type: "+my_rest.cuisine_type+"\n")

my_rest.describe_restaurant()
my_rest.open_restaurant()

# Another object
print("\n------------------------------------------")
town = Restaurant("Big Knife", "Turkey Cuisine")
print("Restaurant name: " + town.name)
print("Style of cooking: " + town.cuisine_type)
# calling methods
town.describe_restaurant()
town.open_restaurant()
