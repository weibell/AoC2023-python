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

calibration_values = []
for line in input:
  positions_and_values = sorted([(line.find(digit), value) for digit, value in mappings.items()
                          if line.find(digit) != -1])
  first_value = positions_and_values[0][1]
  last_value = positions_and_values[-1][1]
  calibration_values.append(int(str(first_value) + str(last_value)))

print(sum(calibration_values))
