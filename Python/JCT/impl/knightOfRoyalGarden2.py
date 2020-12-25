position = list(input())
position[0] = ord(position[0]) - ord('a') + 1
position[1] = int(position[1])

steps = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

result = 0
for step in steps:
    next_row = position[0] + step[0]
    next_col = position[1] + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)