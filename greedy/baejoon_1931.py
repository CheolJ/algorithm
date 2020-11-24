num = int(input())
data = [tuple(int(x) for x in input().split()) for _ in range(num)]
data.sort(key = lambda x :(x[1], x[0]))
max_count = 0
next_item = 0
for i in range(0, num):
  if next_item <= data[i][0]:
    next_item = data[i][1]
    max_count +=1

print(max_count)
