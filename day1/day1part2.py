with open("day1\input.txt") as file:
    text = file.read()
    elves = text.split("\n\n")
    calories = []
    for elf in elves:
        calories.append(sum(map(int, filter(None, elf.split("\n")))))

    calories.sort()
    print(calories[-1]+calories[-2]+calories[-3])
