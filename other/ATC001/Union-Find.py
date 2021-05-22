n, q = map(int,input().split())

rank = [1]*n

par = [*range(n)]

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
  #ランクの高いほうが親になるようにする
  if rank[x] > rank[y]:
    x,y = y,x
  if rank[x] == rank[y]:
    rank[y] += 1
  par[x] = y

def same(x, y):
  return find(x) == find(y)


for i in range(q):
  p, a, b = map(int,input().split())
  if p:
    if same(a, b):
      print("Yes")
    else:
      print("No")
  else:
    unite(a, b)