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

N, W = MI()
weight = [0]*N
value = [0]*N
dp = [[0]*100001 for _ in range(101)]

for i in range(N):
  w, v = MI()
  weight[i] = w
  value[i] = v
  for j in range(W+1):
    if j - weight[i] >= 0:
      dp[i+1][j] = max(dp[i+1][j], dp[i][j-weight[i]]+value[i])
    dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(dp[N][W])
