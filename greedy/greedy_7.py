"""
백준 - 거스름돈
"""

amount = int(input())
change = 1000 - amount

cnt = 0
coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    if change >= coin:
        cnt += change // coin
        change %= coin

print(cnt)
