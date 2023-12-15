def move_north(rock_map: list[str]) -> list[str]:
    for y, row in enumerate(rock_map):
        for x, char in enumerate(row):
            if char != 'O':  # skip non-moving rocks
                continue
            obstacles_y = [y for y in range(y) if rock_map[y][x] in '#O']
            new_y = max(obstacles_y, default=-1) + 1
            if new_y != y:
                rock_map[y] = rock_map[y][:x] + '.' + rock_map[y][x+1:]
                rock_map[new_y] = rock_map[new_y][:x]+'O'+rock_map[new_y][x+1:]
    return rock_map


def calculate_load(rock_map: list[str]) -> int:
    height = len(rock_map)
    return sum(row.count('O') * (height - y) for y, row in enumerate(rock_map))


rock_map = open('input.txt').read().splitlines()
print(calculate_load(move_north(rock_map)))
