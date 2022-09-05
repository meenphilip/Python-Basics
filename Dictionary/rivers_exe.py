rivers = {
    'Sudan': 'nile',
    'brazil': 'amazon',
    'zambia': 'zambezi'
}
# for country, river in rivers.items():
#     print(river.title() + " runs through " + country.title())

# printing each river name
# for name in rivers.values():
#     print(name.title())

# print each country name in the dict
for country in rivers:
    print(country.upper())
