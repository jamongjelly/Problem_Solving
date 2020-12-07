N, M, K = map(int, input().split(' '))
numArr = list(map(int, input().split(' ')))

first = second = 0

for num in numArr:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num

secondCount = int(M / (K + 1))
result = (M - secondCount) * first + secondCount * second

print(result)