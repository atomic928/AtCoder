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

N,K = MI()
dp = [[[0]*3 for _ in range(2)] for _ in range(N+1)]



kl = [0]*N

for i in range(K):
  a,b = MI()
  kl[a-1] = b

if kl[0]:
  dp[1][0][kl[0]-1] = 1
else:
  for i in range(3):
    dp[1][0][i] = 1

for i in range(1,N):
  if kl[i]:
      dp[i+1][1][kl[i]-1] += dp[i][0][kl[i]-1] #連続
      dp[i+1][0][kl[i]-1] += sum(dp[i][0]) + sum(dp[i][1]) - dp[i][1][kl[i]-1] - dp[i][0][kl[i]-1] #非連続
      for j in range(3):
        if kl[i]-1 != j:
          dp[i+1][1][j] = 0
          dp[i+1][0][j] = 0
  else:
    for j in range(3):
      dp[i+1][1][j] += dp[i][0][j]
      dp[i+1][0][j] += sum(dp[i][0])+sum(dp[i][1])-dp[i][0][j]-dp[i][1][j]
      

print((sum(dp[N][0])+sum(dp[N][1]))%10000)

