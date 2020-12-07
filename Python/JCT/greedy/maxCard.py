N, M = map(int, input().split(' '))

def max(list):
    maxVal = 1
    for num in list:
        if (maxVal < num):
            maxVal = num
    return maxVal

def min(list):
    minVal = 100
    for num in list:
        if (minVal > num):
            minVal = num
    return minVal

minArr = []
for i in range(0, N):
    minArr.append(min(map(int, input().split(' '))))

print(max(minArr))