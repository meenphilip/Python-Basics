cities = {
    'Nairobi': {
        'country': 'kenya',
        'population': 200000,
        'fact': 'capital city of kenya'
    },
    'juba': {
        'country': 'south sudan',
        'population': 84000,
        'fact': 'capital city of south sudan'
    },
    'new york': {
        'country': 'united state of america',
        'population': 24000000,
        'fact': 'world trade center'
    }
}
# loop thro the dict
for city_name, city_info in cities.items():
    print("\n"+city_name.title())
    for k, v in city_info.items():
        print("\t"+k.title() + " : " + str(v))
