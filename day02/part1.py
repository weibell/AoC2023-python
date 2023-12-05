import re


def max_cubes(line: str, comparison_color: str) -> int:
    cubes = re.findall(r'(\d+) (\w+)', line)
    return max(int(count) for count, color in cubes if color == comparison_color)


with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

possible_game_ids = []
for game_id, line in enumerate(input_data, start=1):
    if max_cubes(line, 'red') <= 12 and max_cubes(line, 'green') <= 13 and max_cubes(line, 'blue') <= 14:
        possible_game_ids.append(game_id)

print(sum(possible_game_ids))
