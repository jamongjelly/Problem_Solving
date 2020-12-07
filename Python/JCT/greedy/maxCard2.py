N, M = map(int, input().split(' '))

def min(a, b):
    return a if a < b else b

def max(a, b):
    return a if a > b else b

max_val = 1
for row in range(0, N):
    min_val = 10001
    data = list(map(int, input().split()))
    for num in data:
        min_val = min(min_val, num)
    max_val = max(min_val, max_val)

print(max_val)