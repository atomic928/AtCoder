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

from heapq import heappop, heappush

def dijkstra(s, g): # 始点・隣接グラフ
    INF = 10 ** 18
    check = [False] * n
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)] # 距離・ノード
    while q:
        node = heappop(q)[1] # 今いる所までの距離・そのノード
        if check[node]: continue
        check[node] = True
        for i in g[node]: # これから行く所までの距離・そのノード
            if check[i]: continue
            if dist[i] <= dist[node] + 1: continue
            dist[i] = dist[node] + 1
            heappush(q, [dist[i], i])
    return dist

n,m = MI()
graph = [[] for _ in range(n)]

for _ in range(m):
  a,b = MI()
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

dis = dijkstra(0, graph)

print(dis)
