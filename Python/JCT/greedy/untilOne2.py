N, K = map(int, input().split())

count = 0
while N > 1:
    quotient = N // K
    k_multiple = quotient * K

    if (N == k_multiple):
        N = quotient
        count += 1
    else:
        diff = N - k_multiple
        N -= diff
        count += diff

print(count)