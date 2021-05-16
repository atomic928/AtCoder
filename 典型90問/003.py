from heapq import heappop, heappush

def dijkstra(s, g): #(始点、辺)
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
  return dist

n = int(input())
adj = [[] for _ in range(n)]
for i in range(n-1):
  a, b = map(int,input().split())
  adj[a-1].append(b-1)
  adj[b-1].append(a-1)

zerodis = dijkstra(0, adj) #始点からそれぞれの距離を求める
maxdisnode = zerodis.index(max(zerodis)) #始点から最も遠いノード
saityou = dijkstra(maxdisnode, adj) #求めたノードから最も遠いノード
print(max(saityou)+1) #最終的に輪にするので+1
