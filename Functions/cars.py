def make_car(manufacture, model, **car_info):
    car = {}
    car['manufacture'] = manufacture
    car['model'] = model
    print("\nCar information: ")
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
car1 = make_car('bmw', 'ford', color='red', last=2014)
car2 = make_car('ferrari', 'ford', color='beige', last_made=341, total=45678)
print(car)
print(car1)
print(car2)
