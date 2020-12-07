N, M, K = map(int, input().split(' '))
num_arr = list(map(int, input().split(' ')))

first = second = 0

for num in num_arr:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num

second_count = int(M / (K + 1))
result = (M - second_count) * first + second_count * second

print(result)