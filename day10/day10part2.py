def render(crt, crt_width, cycle, sprite):
    row = int(cycle / crt_width)
    column = cycle % crt_width

    if (row >= len(crt)):
        crt.append('')

    current_row = crt[row]
    if (column >= len(current_row)):
        current_row += (sprite[column])

    crt[row] = current_row


def get_sprite(x):
    temp = '........................................'
    for i in range(-1, 2):
        temp = temp[:(x+i)] + '#' + temp[(x+i)+1:]
    return temp


with open("day10\input.txt") as file:
    commands_raw = file.read().strip().splitlines()

crt_width = 40
x = 1
cycle = 0
crt = []
sprite = get_sprite(x)
for command in commands_raw:
    command = command.split()
    if (command[0] == 'noop'):
        render(crt, crt_width, cycle, sprite)
        cycle += 1
    else:
        render(crt, crt_width, cycle, sprite)
        cycle += 1
        render(crt, crt_width, cycle, sprite)
        cycle += 1
        x += int(command[1])
        sprite = get_sprite(x)

for row in crt:
    print(row, end='\n')
