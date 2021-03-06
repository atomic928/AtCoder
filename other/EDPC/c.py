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

n = II()
abc = LLI(n)
dp = [[0,0,0] for _ in range(10**6)]

for i in range(n):
  for j in range(3):
    for k in range(3):
      if j == k: continue
      dp[i+1][k] = max(dp[i+1][k], dp[i][j]+abc[i][k])

print(max(dp[n]))