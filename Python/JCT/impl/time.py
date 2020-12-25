N = int(input())

limitArr = [5, 9, 5]
arr = [600, 60, 10]
save_point = 1

for index in range(2, -1, -1):
    temp = 0
    for digit in range(0, limitArr[index]+1):
        temp += arr[index] if digit == 3 else save_point
    save_point = temp

result = 0
for hour in range(0, N+1):
    result += 3600 if hour % 10 == 3 else save_point

print(result)