import re

input_data = open('input.txt').read().replace(' ', '')
race_duration = int(re.findall(r'\d+', input_data)[0])
record_distance = int(re.findall(r'\d+', input_data)[1])


# brute-force solution...
def number_of_ways_to_win(race_duration: int, record_distance: int) -> int:
    wins = 0
    for hold_duration in range(1, race_duration):
        speed = hold_duration
        distance = (race_duration - hold_duration) * speed
        if distance > record_distance:
            wins += 1
    return wins


winning_options = number_of_ways_to_win(race_duration, record_distance)
print(winning_options)
