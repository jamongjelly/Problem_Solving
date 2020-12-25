position = list(input())

position[0] = ord(position[0]) - 97
position[1] = int(position[1]) - 1

row_move = [2, -2, 1, -1]
col_move = [1, 1, 2, 2]

count = 0
for i in range(4):
    new_row = position[0] + row_move[i]
    if new_row >= 0 and new_row < 8:
        new_col1 = position[1] + col_move[i]
        new_col2 = position[1] - col_move[i]
        count += 1 if new_col1 >= 0 and new_row < 8 else 0
        count += 1 if new_col2 >= 0 and new_row < 8 else 0

print(count)