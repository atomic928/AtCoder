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

n = II()
s = LI()
t = LI()

dp = [t] + [[0]*n for _ in range(n-1)]

for i in range(n):
  dp[(i+1)%n] = dp[i]
  for j in range(n):
    if dp[(i+1)%n][j] > dp[i][(j-1)%n]+s[(j-1)%n]:
      dp[(i+1)%n][j] = dp[i][(j-1)%n]+s[(j-1)%n]

for i in range(n):
  print(dp[n-1][i])
