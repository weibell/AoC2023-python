import re

input_data = open('input.txt').read().splitlines()
maps = []
for line in input_data[2:]:
    if 'map' in line:
        maps.append(dict())
    elif line != '':
        destination, source, length = [int(value) for value in line.split()]
        maps[-1][range(source, source+length)] \
            = range(destination, destination+length)


def lookup_location(initial_value: int) -> int:
    value = initial_value
    for current_map in maps:
        value = next(
            (destination_range.start + (value - source_range.start)
             for source_range, destination_range in current_map.items()
             if value in source_range),
            value  # fallback
        )
    return value


seeds = [int(seed) for seed in re.findall(r'\d+', input_data[0])]
locations = [lookup_location(seed) for seed in seeds]

print(min(locations))