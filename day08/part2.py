import re

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

network = {}
for line in input_data[2:]:
    node, left, right = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', line)[0]
    network[node] = (left, right)


def direction_sequence():
    sequence = input_data[0]
    while True:
        for direction in sequence:
            yield direction


direction = direction_sequence()
current_nodes = [node for node in network.keys() if node.endswith('A')]
counter = 0
while not all(node.endswith('Z') for node in current_nodes):
    next_direction = next(direction)
    for i, current_node in enumerate(current_nodes):
        left, right = network[current_node]
        current_nodes[i] = left if next_direction == 'L' else right
    counter += 1

print(counter)
