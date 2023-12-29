import sys
sys.setrecursionlimit(10_000)

N = complex(0, -1)  # x, y
S = complex(0, 1)
E = complex(1, 0)
W = complex(-1, 0)

reflected_direction = {
    '/':  {N: E,  S: W,  E: N,  W: S},
    '\\': {N: W,  S: E,  E: S,  W: N}
}
splitter_directions = {
    '-':  {N: (E, W),  S: (E, W),  E: (E,),    W: (W,)},
    '|':  {N: (N,),    S: (S,),    E: (N, S),  W: (N, S)},
}


def beam_enters_tile(position: complex, direction: complex):
    x, y = int(position.real), int(position.imag)
    if (position, direction) in visited or not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
        return
    visited.add((position, direction))  # used in count_energized_tiles()

    match tile_type := grid[y][x]:
        case '.':
            beam_enters_tile(position + direction, direction)
        case '/' | '\\':
            new_direction = reflected_direction[tile_type][direction]
            beam_enters_tile(position + new_direction, new_direction)
        case '-' | '|':
            for new_direction in splitter_directions[tile_type][direction]:
                beam_enters_tile(position + new_direction, new_direction)


def count_energized_tiles(position: complex, direction: complex) -> int:
    visited.clear()
    beam_enters_tile(position, direction)
    unique_energized_tiles = set(position for position, _ in visited)
    return len(unique_energized_tiles)


def starting_positions_and_directions() -> tuple[complex, complex]:
    width, height = len(grid[0]), len(grid)
    for x in range(width):
        yield (complex(x, 0), S)
        yield (complex(x, height-1), N)
    for y in range(height):
        yield (complex(0, y),  E)
        yield (complex(width-1, y),  W)


grid = open('input.txt').read().splitlines()
visited = set()  # tuples of (position, direction)
print(max(count_energized_tiles(pos, dir)
      for pos, dir in starting_positions_and_directions()))
