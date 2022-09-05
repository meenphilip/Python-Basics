def build_profile(first, last, **user_info):
    profile = {}
    profile['first-name'] = first
    profile['last-name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    'Meen', 'tycoon', age=25, school='jkuat', dream='Great Web Developer')
print(user_profile)
