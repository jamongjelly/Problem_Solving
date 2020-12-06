N, M, K = map(int, input().split(' '))
numArr = list(map(int, input().split(' ')))

first = second = 0

for num in numArr:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num

multiple = int(M / (K + 1)) * K + M % (K+1)
result = multiple * first + (M - multiple) * second

print(result)