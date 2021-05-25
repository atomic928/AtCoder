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
p = LI()
MAX = sum(p)+1
dp = [[0]*MAX for _ in range(101)]

dp[0][0] = 1
dp[0][p[0]] = 1

for i in range(1, n):
  for j in range(MAX):
    if dp[i-1][j]:
      dp[i][j] = 1
      dp[i][j+p[i]] = 1

print(sum(dp[n-1]))