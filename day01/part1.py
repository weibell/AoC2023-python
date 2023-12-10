input_data = open('input.txt').read().splitlines()
calibration_values = []
for line in input_data:
    digits = [char for char in line if char in '0123456789']
    calibration_values.append(int(digits[0] + digits[-1]))

print(sum(calibration_values))
