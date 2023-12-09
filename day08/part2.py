import re
import math

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

network = {}
for line in input_data[2:]:
    node, left, right = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', line)[0]
    network[node] = (left, right)


def direction_sequence() -> str:
    sequence = input_data[0]
    while True:
        for direction in sequence:
            yield direction


counters = []
starting_nodes = [node for node in network.keys() if node.endswith('A')]
for starting_node in starting_nodes:
    current_node = starting_node
    counter = 0
    instruction = direction_sequence()
    while not current_node.endswith('Z'):
        next_left, next_right = network[current_node]
        current_node = next_left if next(instruction) == 'L' else next_right
        counter += 1
    counters.append(counter)

# the input data appears to be designed to allow this trick
print(math.lcm(*counters))
