from functools import cache


@cache
def move_north(rock_map: tuple[str]) -> tuple[str]:
    rock_map = list(rock_map)
    for y, row in enumerate(rock_map):
        for x, char in enumerate(row):
            if char != 'O':  # skip non-moving rocks
                continue
            obstacles_y = [y for y in range(y) if rock_map[y][x] in '#O']
            new_y = max(obstacles_y, default=-1) + 1
            if new_y != y:
                rock_map[y] = rock_map[y][:x] + '.' + rock_map[y][x+1:]
                rock_map[new_y] = rock_map[new_y][:x]+'O'+rock_map[new_y][x+1:]
    return tuple(rock_map)


@cache
def turn_clockwise(rock_map: tuple[str]) -> tuple[str]:
    return tuple(''.join(row) for row in zip(*rock_map[::-1]))


@cache
def thousand_cycles(rock_map: tuple[str]) -> tuple[str]:
    for _ in range(4 * 1000):
        rock_map = move_north(rock_map)
        rock_map = turn_clockwise(rock_map)
    return rock_map


def calculate_load(rock_map: tuple[str]) -> int:
    height = len(rock_map)
    return sum(row.count('O') * (height - y) for y, row in enumerate(rock_map))


rock_map = tuple(open('input.txt').read().splitlines())
for i in range(1_000_000_000 // 1000):
    rock_map = thousand_cycles(rock_map)

final_load = calculate_load(rock_map)
print(final_load)
