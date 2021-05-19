n, m = map(int,input().split())
mi = 0
mx = 10e10

for i in range(m):
  l, r = map(int,input().split())
  mi = max(mi, l)
  mx = min(mx, r)

ans = mx-mi+1

print(ans if ans > 0 else 0)