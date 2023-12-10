import re

input_data = open('input.txt').read().splitlines()
scores = []
for line in input_data:
    left, right = line.split(':')[1].split('|')
    winning_numbers = {int(number) for number in re.findall(r'\d+', left)}
    my_numbers = {int(number) for number in re.findall(r'\d+', right)}
    num_matches = len(winning_numbers & my_numbers)
    points = 2 ** (num_matches - 1) if num_matches > 0 else 0
    scores.append(points)

print(sum(scores))
