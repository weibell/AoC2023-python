def positions_and_values(line: str, dir: str) -> list[tuple[int, int]]:
    # returns a list of (index, value)
    mappings = {
        '1': 1, 'one': 1,
        '2': 2, 'two': 2,
        '3': 3, 'three': 3,
        '4': 4, 'four': 4,
        '5': 5, 'five': 5,
        '6': 6, 'six': 6,
        '7': 7, 'seven': 7,
        '8': 8, 'eight': 8,
        '9': 9, 'nine': 9,
    }
    line_find_fn = line.find if dir == 'left' else line.rfind
    return [(line_find_fn(digit), value)
            for digit, value in mappings.items()
            if line_find_fn(digit) != -1]


input_data = open('input.txt').read().splitlines()
calibration_values = [int(
    str(min(positions_and_values(line, dir='left'))[1]) +
    str(max(positions_and_values(line, dir='right'))[1])
) for line in input_data]

print(sum(calibration_values))
