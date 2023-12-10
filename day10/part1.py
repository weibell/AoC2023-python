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


def initial_direction(start: tuple[int, int]) -> tuple[int, int]:
    for direction in (N, S, E, W):
        expected_adjacent_chars = [char for char, connections in direction_mappings.items()
                                   if direction in connections]
        x, y = move(start, direction)  # skipping boundary checks
        if input_data[y][x] in expected_adjacent_chars:
            return direction


x, y = start
current_coords = move(start, initial_direction(start))
visited = {start}

while True:
    visited.add(current_coords)
    possible_directions = graph[current_coords]
    unvisited_neighbors = [neighbor for direction in possible_directions
                           if (neighbor := move(current_coords, direction)) not in visited]
    if len(unvisited_neighbors) == 0:
        break  # back at start
    current_coords = unvisited_neighbors[0]

print(len(visited) // 2)
