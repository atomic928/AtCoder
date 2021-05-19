n, k = map(int,input().split())
ans = 0

for i in range(1, n+1):
  count = 1/n
  while i < k:
    i *= 2
    count /= 2
  ans += count

print(ans)