import sys

#input()
def I(): return sys.stdin.readline().rstrip()
#list(input())
def SI(): return list(sys.stdin.readline().rstrip())
#int(input())
def II(): return int(sys.stdin.readline().rstrip())
#map(int,input().split())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
#map(str, input().split())
def MS(): return map(str, sys.stdin.readline().rstrip().split())
#list(map(int,input().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]
#文字の行列
def LSI(rows_number): return [SI() for _ in range(rows_number)]

from collections import defaultdict

N = II()
A = LI()

rank = [1]*(2*10**5+1)
par = [*range(2*10**5+1)]

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

replace = defaultdict(int)

if N == 1:
  sys.exit(print(0))

ans = 0

for i in range(N//2):
  if A[i] == A[N-1-i]:
    unite(A[i], A[N-1-i])
  else:
    if same(A[i],A[N-1-i]):
      continue
    else:
      unite(A[i],A[N-1-i])
      ans += 1


print(ans)