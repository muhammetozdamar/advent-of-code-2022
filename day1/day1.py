with open("input.txt") as file:
    text = file.read()
    elves = text.split("\n\n")
    calories = []
    for elf in elves:
        calories.append(sum(map(int, filter(None, elf.split("\n")))))

print(max(calories))
