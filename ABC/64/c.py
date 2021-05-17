n = int(input())
a = list(map(int,input().split()))
color = [False]*8
free = 0

for i in a:
  if i >= 3200:
    free += 1
    continue
  if color[i//400]: continue
  color[i//400] = True

mi = sum(color) if sum(color) != 0 else 1
mx = sum(color) + free

print(mi, mx)