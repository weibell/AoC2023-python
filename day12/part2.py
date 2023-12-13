def number_of_arrangements(record: str, groups: list[int]) -> int:
    if len(groups) == 0:  # base case
        no_broken_springs_remaining = '#' not in record
        return 1 if no_broken_springs_remaining else 0

    # there needs to be enough space for all groups plus separators
    group_min_start = 0
    group_max_start = len(record) - sum(groups) - len(groups) + 1

    if '#' in record:  # cannot start first damaged spring
        group_max_start = min(record.index('#'), group_max_start)

    first_group_size, *remaining_groups = groups
    arrangements_counter = 0
    for group_start in range(group_min_start, group_max_start + 1):  # sliding window
        group_end = group_start + first_group_size
        group = record[group_start:group_end]

        is_group_possible = all(char in '#?' for char in group)
        is_end_of_record = group_end >= len(record)
        is_group_separated = is_end_of_record or record[group_end] in '.?'
        if not is_group_possible or not is_group_separated:
            continue

        remaining_record_after_separator = record[group_end+1:]

        arguments = (remaining_record_after_separator, tuple(remaining_groups))
        if arguments not in cache:  # memoization for significant speedup
            cache[arguments] = number_of_arrangements(*arguments)
        arrangements_counter += cache[arguments]

    return arrangements_counter


input_data = open('input.txt').read().splitlines()
cache = {}
total_arrangements = 0
for line in input_data:
    record, groups = line.split(' ')
    record = '?'.join(record for _ in range(5))
    groups = ','.join(groups for _ in range(5))

    group_sizes = map(int, groups.split(','))
    total_arrangements += number_of_arrangements(record, tuple(group_sizes))

print(total_arrangements)
