p = int(input())

count = 0
for i in range(1, 2*p-1):
  for j in range(1, 2*p-1):
    for k in range(1, 2*p-1):
      if (i/(2*p-i))*(j/(2*p-j))*(k/(2*p-k)) == 1:
        count += 1

print(count)
