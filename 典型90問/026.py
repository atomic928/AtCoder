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

sys.setrecursionlimit(10**6)

n = int(input())
G = [[] for _ in range(n)]

for i in range(n-1):
  a,b = MI()
  G[a-1].append(b-1)
  G[b-1].append(a-1)

color = [-1]*n

def dfs(node, col):
  color[node] = col
  for i in G[node]:
    if color[i] == -1:
      dfs(i, 1-col)

dfs(0, 0)

G0 = []
G1 = []


for i in range(n):
  if color[i]:
    G1.append(i+1)
  else:
    G0.append(i+1)

for i in range(n//2):
  if len(G0) < len(G1):
    print(G1[i], end=" ")
  else:
    print(G0[i], end=" ")

