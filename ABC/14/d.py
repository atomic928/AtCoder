from heapq import heappop, heappush

def dijkstra(s, g, e): #(始点、辺)
  check = [False]*n #ノードが確定しているか
  dist = [10**10]*n #（始点から各ノードへの距離）
  dist[s] = 0
  hq = [(0, s)] #（距離、ノード）
  while hq:
    node = heappop(hq)[1] #ノードをpopする
    check[node] = True
    for hen in g[node]:
      if check[hen] == False and dist[node] + 1 < dist[hen]:
        dist[hen] = dist[node] + 1
        heappush(hq, (dist[hen], hen))
    if check[e]:
      return dist[e]


n = int(input())

graph = [[] for _ in range(n)]

for i in range(n-1):
  x, y = map(int,input().split())
  graph[x-1].append(y-1)
  graph[y-1].append(x-1)

q = int(input())

for i in range(q):
  a, b = map(int,input().split())
  adis = dijkstra(a-1, graph, b-1)
  print(adis+1)