# Lowercase item types a through z have priorities 1 through 26.  -> 97-122
# Uppercase item types A through Z have priorities 27 through 52. -> 65-90

def char_to_priority(char):
    val = ord(char);
    if(val>=97 and val<=122):
        return (val - 96)
    elif(val>=65 and val <=90):
        return (val-38)
    return 0


total_priorities = 0
with open("day3\input.txt") as file:
    rucksacks = file.read().split("\n")
    for rucksack in rucksacks:
        rucksack = rucksack.strip();
        len_rucksack = len(rucksack);
        if(len_rucksack == 0): continue
        first_compartment =  rucksack[:len_rucksack//2]
        second_compartment =  rucksack[len_rucksack//2:]
        common = ''.join(set(first_compartment).intersection(second_compartment))
        for char in common:
            total_priorities += char_to_priority(char)

print(total_priorities)