with open('input.txt', 'r') as f:
  input = f.read().splitlines()

mappings = {
  'one': 1, 'two': 2, 'three': 3,
  'four': 4, 'five': 5, 'six': 6,
  'seven': 7, 'eight': 8, 'nine': 9,
  '1': 1, '2': 2, '3': 3, 
  '4': 4, '5': 5, '6': 6, 
  '7': 7, '8': 8, '9': 9
}

def positions_and_values(line: str, from_left: bool):
  line_find = line.find if from_left else line.rfind
  return [(line_find(digit), value) for digit, value in mappings.items() if line_find(digit) != -1]

calibration_values = []
for line in input:
  first_value = sorted(positions_and_values(line, from_left=True))[0][1]
  last_value = sorted(positions_and_values(line, from_left=False))[-1][1]

  calibration_values.append(int(str(first_value) + str(last_value)))

print(sum(calibration_values))
