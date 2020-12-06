N = int(input("금액을 입력해주세요: "))

numOfCoins = 0

coins = [500, 100, 50, 10]

for coin in coins:
    numOfCoins += N // coin
    N %= coin

print(numOfCoins)