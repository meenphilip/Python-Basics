alien_o = {
    'color': 'green',
    'point': 5
}
# print(alien_o['color'])
# print(alien_o['point'])
print(alien_o)
new_point = alien_o['point']
print(f"You have just earned {new_point} points.")
# adding new key:value to the alien_o
alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)
