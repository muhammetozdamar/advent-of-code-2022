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
knots = []
for i in range(10):
    knots.append({'x': 0, 'y': 0})

positions.add(tuple(knots[-1].items()))

for command in commands_raw:
    direction, count = command.split()
    count = int(count)
    for x in range(0, count):
        dx, dy = directions[direction]
        knots[0]['x'] += dx
        knots[0]['y'] += dy
        for i in range(1, len(knots)):
            prev_knot = knots[i-1]
            curr_knot = knots[i]
            # Check if T has to move or not
            x_dist = abs(prev_knot['x'] - curr_knot['x'])
            y_dist = abs(prev_knot['y'] - curr_knot['y'])

            if (x_dist >= 2 or y_dist >= 2):
                rdx, rdy = compare_positions(prev_knot, curr_knot)
                curr_knot['x'] += rdx
                curr_knot['y'] += rdy
                if (i == len(knots)-1):
                    positions.add(tuple(knots[-1].items()))

print(len(positions))
