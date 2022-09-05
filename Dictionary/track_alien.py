alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}

print(f"Original x-position: {alien_o['x_position']}")
# Move the alien to right
# Determine how far to move the alien based on its speed
if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# the new position is the old position plus the increment
# alien_o['x_position'] = alien_o['x_position'] + x_increment
alien_o['x_position'] += x_increment

print(f"New x-position: {alien_o['x_position']}")
