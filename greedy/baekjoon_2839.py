def greedy_2839(kg):
  if (kg%5)%3==0:
    return int(kg/5) + int((kg%5)/3)

  else:
    num = int(kg/5)
    result = 0
    for i in range(num, -1, -1):
      imsi = kg - 5*i
      if imsi%3==0:
        if result==0 or result > i+imsi/3:
          result = i + int(imsi/3)
        continue
    if result == 0 :
      return -1
    else:
      return result


kg = int(input())

print(greedy_2839(kg))