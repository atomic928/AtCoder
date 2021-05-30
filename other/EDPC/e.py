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

N, W = MI()
#価値vを達成するためのwの最小値を保存
dp = [[10**9+1]*(100001) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
  a, b = MI()
  for j in range(100001):
    dp[i+1][j] = dp[i][j]
    if dp[i][j-b] != 10**9+1:
      dp[i+1][j] = min(dp[i][j], dp[i][j-b]+a)
    
for i in range(100000, -1,-1):
  if dp[N][i] <= W:
    sys.exit(print(i))