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

N = II()
A = LI()

dp = [[0]*21 for _ in range(N)]
dp[0][0] = 1

for i in range(N-1):
  for j in range(21):
    if j+A[i] < 21:
      dp[i+1][j] += dp[i][j+A[i]]
    if j-A[i] >= 0:
      dp[i+1][j] += dp[i][j-A[i]]
    
if A[0] == 0:
  print(dp[N-1][A[-1]]//2)
else:
  print(dp[N-1][A[-1]])
