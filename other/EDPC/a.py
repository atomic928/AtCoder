n = int(input())
h = list(map(int,input().split()))
node = [0]*n #それぞれのノードに行く最小のコスト
hen1 = [abs(h[i]-h[i-1]) for i in range(1,n)] #隣同士の辺の重み
hen2 = [abs(h[i]-h[i-2]) for i in range(2,n)] #ひとつ飛ばしの辺の重み

node[1] = hen1[0]

for i in range(2, n):
  node[i] = min(node[i-1]+hen1[i-1], node[i-2]+hen2[i-2]) #それぞれのノードには二通りの行き方がある

print(node[-1])
