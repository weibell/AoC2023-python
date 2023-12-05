import re

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

card_counter = {card_number: 1 for card_number in range(1, len(input_data)+1)}
for card_number, line in enumerate(input_data, start=1):
    left, right = line.split(':')[1].split('|')
    winning_numbers = {int(number) for number in re.findall(r'\d+', left)}
    my_numbers = {int(number) for number in re.findall(r'\d+', right)}
    num_matches = len(winning_numbers & my_numbers)

    for won_copies in range(card_number+1, card_number+1 + num_matches):
        card_counter[won_copies] += card_counter[card_number]

print(sum(card_counter.values()))
