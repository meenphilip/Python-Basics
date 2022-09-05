def city_country(city_name, country_name):
    name = f"{city_name}, {country_name} "
    return name.title()


describe_place = city_country('Nairobi', 'kenya')
print(describe_place)
describe_place = city_country('Cairo', 'Egypt')
print(describe_place)
describe_place = city_country('Cape town', 'south africa')
print(describe_place)
