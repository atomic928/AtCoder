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

sys.setrecursionlimit(10000)

N, M = MI()
paths = [[] for _ in range(N)]

for _ in range(M):
  a,b = MI()
  paths[a-1].append(b-1)

def dfs(x):
  if check[x]: return
  check[x] = 1
  for xx in paths[x]: dfs(xx)

ans = 0

for i in range(N):
  check = [0]*N
  dfs(i)
  ans += sum(check)
  
print(ans)