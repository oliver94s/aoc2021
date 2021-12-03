commands = []
with open('input', 'r') as f:
    for line in f.readlines():  
        direction, value = line.split(' ')  
        commands.append((direction, int(value)))

x_pos = 0
y_pos = 0
for cmd in commands:
    direction = cmd[0]
    value = cmd[1]
    if direction == 'forward':
        x_pos += value
    elif direction == 'up':
        y_pos -= value
    elif direction == 'down':
        y_pos += value

print(y_pos * x_pos)