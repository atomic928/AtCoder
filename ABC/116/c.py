n = int(input())
h = list(map(int,input().split()))
isUp = True
isLast = False
ans = 0

if n == 1:
  exit(print(h[0]))

for i in range(n-1):
  if isUp:
    if h[i] > h[i+1]:
      ans += h[i]
      isUp = False
  else:
    if h[i] < h[i+1]:
      ans -= h[i]
      isUp = True
  if i == n-2:
    if isUp:
      ans += h[-1]
print(ans)