import re


def max_cubes(line: str, comparison_color: str) -> int:
    cubes = re.findall(r'(\d+) (\w+)', line)
    return max(int(count) for count, color in cubes if color == comparison_color)


with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

set_powers = []
for line in input_data:
    set_powers.append(max_cubes(line, 'red') *
                      max_cubes(line, 'green') *
                      max_cubes(line, 'blue'))

print(sum(set_powers))
