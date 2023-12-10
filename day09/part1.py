import re


def sequence_differences(sequence: list[int]) -> list[int]:
    return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]


input_data = open('input.txt').read().splitlines()
extrapolated_values = []
histories = [[int(value) for value in re.findall(r'-?\d+', history)]
             for history in input_data]
for history in histories:
    sequences = [history]
    while not all(value == 0 for value in sequences[-1]):
        sequences.append(sequence_differences(sequences[-1]))

    extrapolated_value = 0
    for sequence in reversed(sequences):
        extrapolated_value += sequence[-1]
    extrapolated_values.append(extrapolated_value)

print(sum(extrapolated_values))
