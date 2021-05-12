s = input()
k = int(input())
count = 0
for i in s:
  if i == "1":
    count += 1
  else:
    print(i)
    exit()
  
  if count == k:
    print(i)
    exit()