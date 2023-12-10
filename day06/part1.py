import math
import re

input_data = open('input.txt').read().splitlines()
race_durations = [int(ms) for ms in re.findall(r'\d+', input_data[0])]
record_distances = [int(mm) for mm in re.findall(r'\d+', input_data[1])]


# brute-force solution...
def number_of_ways_to_win(race_duration: int, record_distance: int) -> int:
    wins = 0
    for hold_duration in range(1, race_duration):
        speed = hold_duration
        distance = (race_duration - hold_duration) * speed
        if distance > record_distance:
            wins += 1
    return wins


winning_options_per_race = [number_of_ways_to_win(race_duration, record_distance)
                            for race_duration, record_distance in zip(race_durations, record_distances)]
print(math.prod(winning_options_per_race))
