def get_signal_str(cycle, x):
    i = (cycle/20)
    if (i % 2 == 1 and i <= 11):
        return cycle * x
    return 0


with open("day10\input.txt") as file:
    commands_raw = file.read().strip().splitlines()

x = 1
cycle = 0
total = 0
for command in commands_raw:
    command = command.split()
    if (command[0] == 'noop'):
        cycle += 1
        total += get_signal_str(cycle, x)
    else:
        cycle += 1
        total += get_signal_str(cycle, x)
        cycle += 1
        total += get_signal_str(cycle, x)
        x += int(command[1])

print(total)
