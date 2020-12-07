N, M = map(int, input().split(' '))

def max(list):
    max_value = 1
    for num in list:
        if (max_value < num):
            max_value = num
    return max_value

def min(list):
    min_value = 10001
    for num in list:
        if (min_value > num):
            min_value = num
    return min_value

minArr = []
for i in range(0, N):
    minArr.append(min(map(int, input().split(' '))))

print(max(minArr))