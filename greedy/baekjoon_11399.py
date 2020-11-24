num = int(input())
data = list(map(int, input().split()))
data.sort()
total = 0

for i in range(1, num+1):
  total += sum(data[0:i])

print(total)
