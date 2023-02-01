def extract_numbers_from_str(s):
    numbers = ''.join(c for c in s if c.isdigit() or c.isspace())
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    return numbers


def perform_operation(x, op, y):
    return eval(f'{x} {op} {y}')


with open("day11\input.txt") as file:
    monkey_data = file.read().split('\n\n')

monkey_items = {}
monkey_inspections = []


for i, monkey in enumerate(monkey_data):
    monkey_items[i] = extract_numbers_from_str(monkey.splitlines()[1])
    monkey_inspections.append(0)

for round in range(0, 10000):
    for i, monkey in enumerate(monkey_data):
        for item in reversed(monkey_items[i]):
            operation = monkey.splitlines()[2].split()
            index_of_equal_sign = operation.index('=')
            op = operation[index_of_equal_sign+2]
            v = operation[index_of_equal_sign+3]
            v = int(v) if v.isnumeric() else item

            new_value = (perform_operation(item, op, v))
            test = monkey.splitlines()[3]
            v = extract_numbers_from_str(test)[0]

            if (new_value % v == 0):
                next_monkey_line = monkey.splitlines()[4]
                while (new_value % v == 0):
                    new_value = new_value/v
            else:
                next_monkey_line = monkey.splitlines()[5]

            next_monkey = extract_numbers_from_str(next_monkey_line)[0]

            monkey_items[i].remove(item)
            monkey_items[next_monkey].append(new_value)
            monkey_inspections[i] += 1


monkey_inspections = sorted(monkey_inspections, reverse=True)
print(monkey_items)
print(monkey_inspections)
print(monkey_inspections[0]*monkey_inspections[1])
