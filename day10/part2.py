with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)
direction_mappings = {
    '|': (N, S),
    '-': (E, W),
    'L': (N, E),
    'J': (N, W),
    '7': (S, W),
    'F': (S, E),
}

graph = {}  # of directions per coordinate
start = None
for y, line in enumerate(input_data):
    for x, char in enumerate(line):
        if char in '|-LJ7F':
            graph[(x, y)] = direction_mappings[char]
        if char == 'S':
            start = (x, y)


def move(from_coordinates: tuple[int, int], to: tuple[int, int]) -> tuple[int, int]:
    return (from_coordinates[0] + to[0], from_coordinates[1] + to[1])


def initial_direction_options(start: tuple[int, int]) -> list[tuple[int, int]]:
    options = []
    expected_adjacent_chars = {
        N: '|7F',
        S: '|LJ',
        E: '-7J',
        W: '-LF'
    }
    for direction in (N, S, E, W):
        x, y = move(start, direction)  # skipping boundary checks
        if input_data[y][x] in expected_adjacent_chars[direction]:
            options.append(direction)
    return options


x, y = start
start_options = initial_direction_options(start)
current_coords = move(start, start_options[0])
visited = {start}

while True:
    visited.add(current_coords)
    possible_directions = graph[current_coords]
    unvisited_neighbors = [neighbor for direction in possible_directions
                           if (neighbor := move(current_coords, direction)) not in visited]
    if len(unvisited_neighbors) == 0:
        break  # back at start
    current_coords = unvisited_neighbors[0]


is_enclosed = False
enclosed_tiles = 0
width, height = len(input_data[0]), len(input_data)

for x in range(width):
    for y in range(height):
        is_pipe = (x, y) in visited

        if not is_pipe:
            if is_enclosed:
                enclosed_tiles += 1
            continue

        char = input_data[y][x]
        if char == 'S':
            start_options = initial_direction_options(start)
            start_pipe_type = [char for char, directions in direction_mappings.items()
                               if set(directions) == set(start_options)][0]
            char = start_pipe_type

        is_starting_corner = char in 'F7'
        is_ending_corner = char in 'LJ'
        is_horizontal_pipe = char == '-'

        if is_horizontal_pipe:
            is_enclosed = not is_enclosed
        if is_starting_corner:
            source_direction = E if char == 'F' else W
        if is_ending_corner:
            target_direction = E if char == 'L' else W
            if target_direction != source_direction:
                is_enclosed = not is_enclosed

print(enclosed_tiles)
