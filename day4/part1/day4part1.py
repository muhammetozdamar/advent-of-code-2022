counter = 0;
with open("day4\input.txt") as file:
    pairs = file.read().splitlines()
    for pair in pairs:
        if(len(pair.strip()) == 0): continue
        groups = pair.split(',');
        first_group_min = int(groups[0].split('-')[0]);
        first_group_max = int(groups[0].split('-')[1]);
        second_group_min = int(groups[1].split('-')[0]);
        second_group_max = int(groups[1].split('-')[1]);
        if(first_group_min<=second_group_min and first_group_max>=second_group_max or first_group_min>=second_group_min and first_group_max<=second_group_max):
            counter+=1


print(counter)