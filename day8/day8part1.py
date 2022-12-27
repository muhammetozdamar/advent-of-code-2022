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

openTrees = 0
for x in range(0, rows):
    for y in range(0, cols):
        if (x == 0 or x == rows-1 or y == 0 or y == cols-1):
            openTrees += 1
            continue

        # Check each direction until edge
        height = grid[x][y]

        openFromDown = True
        for down in range(x+1, rows):
            if (grid[down][y] >= height):
                openFromDown = False
                break

        openFromUp = True
        for up in range(0, x):
            if (grid[up][y] >= height):
                openFromUp = False
                break

        openFromLeft = True
        for left in range(y+1, cols):
            if (grid[x][left] >= height):
                openFromLeft = False
                break

        openFromRight = True
        for right in range(0, y):
            if (grid[x][right] >= height):
                openFromRight = False
                break

        if (openFromDown or openFromLeft or openFromRight or openFromUp):
            openTrees += 1

print(openTrees)
