n, m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(m)]

def find(x):
  if par[x] == x:
    return x
  else:
    par[x] = find(par[x])
    return par[x]

def unite(x, y):
  x = find(x)
  y = find(y)
  if (x == y): return
  par[x] = y

def same(x, y):
  return find(x) == find(y)

ans = 0

for i in range(m):
  par = [*range(n)]
  for j in range(m):
    if j == i: continue
    unite(ab[j][0]-1, ab[j][1]-1)
  for k in range(1,n):
    if same(0, k): continue
    ans += 1
    break

print(ans)