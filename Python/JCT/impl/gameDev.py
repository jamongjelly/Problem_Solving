M, N = map(int, input().split())
x, y, direction = map(int, input().split())

map_arr = [list(map(int, input().split())) for _ in range(M)]

visited = [[0] * N for _ in range(M)]
visited[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction = 3 if direction == 0 else direction - 1

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == 0 and map_arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if map_arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)