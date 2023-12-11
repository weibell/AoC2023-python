from itertools import combinations

image = open('input.txt').read().splitlines()
empty_rows = [y for y, row in enumerate(image)
              if all(char == '.' for char in row)]
empty_cols = [x for x, cols in enumerate(zip(*image))
              if all(char == '.' for char in cols)]


def coords_after_expansion(coords: tuple[int, int], multiplier: int) -> tuple[int, int]:
    empty_cols_before = sum([1 for col in empty_cols if col < coords[0]])
    empty_rows_before = sum([1 for row in empty_rows if row < coords[1]])
    return (coords[0] + empty_cols_before * (multiplier - 1),
            coords[1] + empty_rows_before * (multiplier - 1))


def manhattan_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


galaxy_coords = []
expansion_factor = 1_000_000
for y, row in enumerate(image):
    for x, char in enumerate(row):
        if char == '#':
            new_x, new_y = coords_after_expansion((x, y), expansion_factor)
            galaxy_coords.append((new_x, new_y))

shortest_paths = [manhattan_distance(galaxy1, galaxy2)
                  for galaxy1, galaxy2 in combinations(galaxy_coords, 2)]
print(sum(shortest_paths))
