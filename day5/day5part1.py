with open("day5\input.txt") as file:
    sections = file.read().split("\n\n")
    stacks_raw = sections[0]
    commands = sections[1]
    
    stack_lines = stacks_raw.splitlines()
    stack_amount = len(stack_lines.pop().split())
    stacks = []
    for stack_index in range(stack_amount):
        stacks.append("")
        for line in stack_lines:
            crate = line[1+stack_index * 4]
            if(crate != " "):
                stacks[stack_index] += crate;
    
    command_lines = commands.splitlines()
    for command in command_lines:
        command_parts = command.split(" ")
        crate_amount =  int(command_parts[1])
        source = int(command_parts[3])-1
        destination = int(command_parts[5])-1

        for i in range(crate_amount):
            crate = stacks[source][0]
            stacks[source] = stacks[source][1:]
            stacks[destination] = crate + stacks[destination]

    top_of_stacks= ""
    for stack in stacks:
        top_of_stacks += stack[0]

    print(top_of_stacks)




        