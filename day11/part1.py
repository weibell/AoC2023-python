from itertools import combinations

image = open('input.txt').read().splitlines()
empty_rows = [y for y, row in enumerate(image)
              if all(char == '.' for char in row)]
empty_cols = [x for x, cols in enumerate(zip(*image))
              if all(char == '.' for char in cols)]

initial_width = len(image[0])
for row in reversed(empty_rows):
    image.insert(row, '.' * initial_width)

initial_height = len(image)
for col in reversed(empty_cols):
    for row in range(initial_height):
        image[row] = image[row][:col] + '.' + image[row][col:]

galaxy_coords = []
for y, row in enumerate(image):
    for x, char in enumerate(row):
        if char == '#':
            galaxy_coords.append((x, y))


def manhattan_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


shortest_paths = [manhattan_distance(galaxy1, galaxy2)
                  for galaxy1, galaxy2 in combinations(galaxy_coords, 2)]
print(sum(shortest_paths))
