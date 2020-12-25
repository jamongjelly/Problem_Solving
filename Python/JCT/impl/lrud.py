N = int(input())
directions = input().split()

x = y = 1

for direction in directions:
    if direction == 'L':
        y -= 1 if y > 1 else 0
    elif direction == 'R':
        y += 1 if y < N else 0
    elif direction == 'U':
        x -= 1 if x > 1 else 0
    elif direction == 'D':
        x += 1 if x < N else 0

print(x, y)