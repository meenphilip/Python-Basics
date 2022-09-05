favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edwards': 'ruby',
    'phil': 'python'
}
# looping throu the dictionary using items()
# for name, language in favourite_languages.items():
#     print(name.title() + "'s favourite language is : " + language.title())


# looping throu the dictionary using keys()
# for key in favourite_languages.keys():
#     print(key.title())

friends = ['phil', 'sarah']
for name in sorted(favourite_languages.keys()):
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", i see your favourite laguage is " +
              favourite_languages[name].title() + "!")
