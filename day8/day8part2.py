with open("day8\input.txt") as file:
    lines = file.read().strip().splitlines()

rows = len(lines)
cols = len(lines[0])
grid = [[]]
for x in range(0, rows):
    grid.append([])
    line = lines[x]
    for y in range(0, cols):
        grid[x].append(int(line[y]))

highest_point = 0

for x in range(0, rows):
    for y in range(0, cols):

        if (x == 0 or x == rows-1 or y == 0 or y == cols-1):
            continue

        tree = grid[x][y]
        # Check each direction until edge
        point = 1

        count = 0
        for down in range(x+1, rows):
            count += 1
            if (grid[down][y] >= tree):
                break
        point = point * count

        count = 0
        for up in range(x-1, -1, -1):
            count += 1
            if (grid[up][y] >= tree):
                break
        point = point * count

        count = 0
        for left in range(y+1, cols):
            count += 1
            if (grid[x][left] >= tree):
                break
        point = point * count

        count = 0
        for right in range(y-1, -1, -1):
            count += 1
            if (grid[x][right] >= tree):
                break
        point = point * count

        if (point > highest_point):
            highest_point = point

print(highest_point)
