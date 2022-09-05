favourite_language = {
    'jen': ['python', 'ruby', 'javascript'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
# main loop holds the key->value
# the inner loop hold the value ofthe list

for name, languages in favourite_language.items():
    if len(languages) == 1:
        print("\n" + name.title()+"'s favourite language is:")
        for language in languages:
            print("\t"+language.title())
    else:
        print("\n" + name.title()+"'s favourite languages are:")
        for language in languages:
            print("\t"+language.title())
