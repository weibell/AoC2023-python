import re

input_data = open('input.txt').read().splitlines()
network = {}
for line in input_data[2:]:
    node, left, right = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', line)[0]
    network[node] = (left, right)


def direction_sequence() -> str:
    sequence = input_data[0]
    while True:
        for direction in sequence:
            yield direction


current_node = 'AAA'
counter = 0
instruction = direction_sequence()
while current_node != 'ZZZ':
    next_left, next_right = network[current_node]
    current_node = next_left if next(instruction) == 'L' else next_right
    counter += 1

print(counter)
