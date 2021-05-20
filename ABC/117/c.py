n, m = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
dist = []

if n >= m:
  print(0)
else:
  ans = 0
  for i in range(m-1):
    dist.append(x[i+1]-x[i])
  dist.sort()
  for i in range(m-n):
    ans += dist[i]
  print(ans)