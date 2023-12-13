import re
from itertools import combinations


def is_valid_arrangement(record: str, expected_group_sizes: list[int]) -> bool:
    actual_groups = re.findall(r'#+', record)
    actual_group_sizes = list(map(len, actual_groups))
    return actual_group_sizes == expected_group_sizes


input_data = open('input.txt').read().splitlines()
total_arrangements = 0
for line in input_data:
    record, groups = line.split(' ')
    group_sizes = list(map(int, groups.split(',')))

    total_springs = sum(group_sizes)
    unassigned_springs = total_springs - record.count('#')
    unassigned_positions = [i for i, char in enumerate(record) if char == '?']

    arrangements_counter = 0
    for assignment in combinations(unassigned_positions, unassigned_springs):
        new_record = list(record)
        for position in assignment:
            new_record[position] = '#'
        if is_valid_arrangement(''.join(new_record), group_sizes):
            arrangements_counter += 1

    total_arrangements += arrangements_counter

print(total_arrangements)
