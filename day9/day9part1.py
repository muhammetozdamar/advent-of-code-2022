def compare_positions(pos1, pos2):
    x1 = pos1['x']
    y1 = pos1['y']
    x2 = pos2['x']
    y2 = pos2['y']

    if x1 > x2 and y1 > y2:
        return directions['RU']
    elif x1 > x2 and y1 == y2:
        return directions['R']
    elif x1 > x2 and y1 < y2:
        return directions['RD']
    elif x1 == x2 and y1 > y2:
        return directions['U']
    elif x1 == x2 and y1 == y2:
        return directions['O']
    elif x1 == x2 and y1 < y2:
        return directions['D']
    elif x1 < x2 and y1 > y2:
        return directions['LU']
    elif x1 < x2 and y1 == y2:
        return directions['L']
    elif x1 < x2 and y1 < y2:
        return directions['LD']


with open("day9\input.txt") as file:
    commands_raw = file.read().strip().splitlines()

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
    'RU': (1, 1),
    'RD': (1, -1),
    'LU': (-1, 1),
    'LD': (-1, -1),
    'O': (0, 0)
}

positions = set()
h_pos = {'x': 0, 'y': 0}
t_pos = {'x': 0, 'y': 0}
positions.add(tuple(t_pos.items()))

for command in commands_raw:
    direction, count = command.split()
    count = int(count)
    for x in range(0, count):
        dx, dy = directions[direction]
        h_pos['x'] += dx
        h_pos['y'] += dy

        # Check if T has to move or not
        x_dist = abs(h_pos['x'] - t_pos['x'])
        y_dist = abs(h_pos['y'] - t_pos['y'])

        if (x_dist >= 2 or y_dist >= 2):
            rdx, rdy = compare_positions(h_pos, t_pos)
            t_pos['x'] += rdx
            t_pos['y'] += rdy
            positions.add(tuple(t_pos.items()))

print(len(positions))
