import re

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

maps = []
for line in input_data[2:]:
    if 'map' in line:
        maps.append(dict())
    elif line != '':
        destination, source, length = [int(value) for value in line.split()]
        maps[-1][range(source, source+length)] \
            = range(destination, destination+length)


# The strategy used here is an improvement over a naive brute force approach,
# but can be optimized by checking whole ranges at a time (while taking
# into account where they 'split')

def reverse_lookup_seed(location: int) -> int:
    value = location
    for current_map in reversed(maps):
        value = next(
            (source_range.start + (value - destination_range.start)
             for source_range, destination_range in current_map.items()
             if value in destination_range),
            value  # fallback
        )
    return value


initial_seed_data = [int(seed) for seed in re.findall(r'\d+', input_data[0])]
seed_ranges = []
for index in range(0, len(initial_seed_data) - 1, 2):
    start, length = initial_seed_data[index:index+2]
    seed_ranges.append(range(start, start+length))

location = 0
while True:
    potential_seed = reverse_lookup_seed(location)
    if any(potential_seed in seed_range for seed_range in seed_ranges):
        print(location)
        break
    location += 1
