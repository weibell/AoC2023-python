import math
import re


with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()


def substring(x: int, y1: int, y2: int) -> str:  # y1 is inclusive, y2 is exclusive
    return input_data[x][max(y1, 0):min(y2, len(input_data[0]))] if x >= 0 and x < len(input_data) else ''


parts_coordinates = {}
for x, line in enumerate(input_data):
    for number in re.finditer(r'\d+', line):
        left = number.start() - 1
        right = number.end()
        adjacent_characters = \
            substring(x-1, left, right + 1) + \
            substring(x, left, left + 1) + \
            substring(x, right, right + 1) + \
            substring(x+1, left, right + 1)
        is_part_number = set(adjacent_characters) != {'.'}

        if is_part_number:
            part_number = int(number.group())
            for y in range(number.start(), number.end()):
                parts_coordinates[(x, y)] = part_number

gear_ratios = []
for gear_x, line in enumerate(input_data):
    for gear in re.finditer('\*', line):
        gear_y = gear.start()
        adjacent_coordinates = [(x, y) for x in range(gear_x-1, gear_x+2) for y in range(gear_y-1, gear_y+2)
                                if (x, y) != (gear_x, gear_y)
                                and x >= 0 and x < len(input_data)
                                and y >= 0 and y < len(line)]
        adjacent_parts = set([parts_coordinates[x_y]
                              for x_y in adjacent_coordinates if x_y in parts_coordinates])

        if len(adjacent_parts) == 2:
            gear_ratios.append(math.prod(adjacent_parts))

print(sum(gear_ratios))
