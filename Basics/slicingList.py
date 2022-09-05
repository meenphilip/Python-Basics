players = ['Mo salah', 'mane', 'firmino',
           'Van Virk', 'thiago', 'Curtis', 'fabinho']
# print(players[0:3])
# print(players[2:])

# looping through the sliced list
# print('Here are the first three players on my team:')
# for player in players[:3]:
#     print(player.title())


# Copying a List:
foods = ['Pizza', 'falafel', 'carrot cake']
friend_foods = foods[:]
foods.append('Connolis')
friend_foods.insert(0, 'ice cream')
print('My Favoutite foods')
print(foods)

print("\n my friend's favourite foods:")
print(friend_foods)
 