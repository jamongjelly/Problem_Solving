N = int(input("금액을 입력해주세요: "))

num_of_coins = 0

coins = [500, 100, 50, 10]

for coin in coins:
    num_of_coins += N // coin
    N %= coin

print(num_of_coins)