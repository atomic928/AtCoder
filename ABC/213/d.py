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

sys.setrecursionlimit(10**7)

n = II()
graph = [[] for _ in range(n)]
ans = []

for i in range(n-1):
  a, b = MI()
  graph[a-1].append(b)
  graph[b-1].append(a)

for i in range(n):
  graph[i].sort()


def dfs(cur, pre):
  ans.append(cur)
  for nex in graph[cur-1]:
    if nex != pre:
      dfs(nex, cur)
      ans.append(cur)

dfs(1,0)
print(*ans)