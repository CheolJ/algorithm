num, total = map(int, input().split())
coins = list(int(input()) for _ in range(num))
coins.sort(reverse=True)

coin_total = 0

for coin in coins:
  if total % coin == total:
    continue
  
  else:
    imsi = int(total/coin)
    total -= coin*imsi
    coin_total += imsi

print(coin_total)
