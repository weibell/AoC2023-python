def count_differences(a: str, b: str) -> int:
    return sum(1 for x, y in zip(a, b) if x != y)


def find_vertical_reflection(pattern: list[str], differences: int) -> int:
    width = len(pattern[0])
    for x in range(1, width):
        num_cols = min(x, width-x)  # number of columns to compare
        left = [row[x-num_cols:x] for row in pattern]
        right = [''.join(reversed(row[x:x+num_cols])) for row in pattern]
        if count_differences(''.join(left), ''.join(right)) == differences:
            return x


def find_horizontal_reflection(pattern: list[str], differences: int) -> int:
    height = len(pattern)
    for y in range(1, height):
        num_rows = min(y, height-y)  # number of rows to compare
        top = pattern[y-num_rows:y]
        bottom = list(reversed(pattern[y:y+num_rows]))
        if count_differences(''.join(top), ''.join(bottom)) == differences:
            return y


input_data = open('input.txt').read().splitlines()
empty_rows = [y for y, row in enumerate(input_data) if row == '']
totals = 0
for start, end in zip([-1]+empty_rows, empty_rows+[len(input_data)]):
    pattern = input_data[start+1:end]
    totals += find_vertical_reflection(pattern, differences=1) or 0
    totals += 100 * (find_horizontal_reflection(pattern, differences=1) or 0)

print(totals)
