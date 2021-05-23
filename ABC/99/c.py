import sys

#input()
def I(): return sys.stdin.readline()
#int(input())
def II(): return int(sys.stdin.readline())
#map(int,input().split())
def MI(): return map(int, sys.stdin.readline().split())
#list(map(int,input().split()))
def LI(): return list(map(int, sys.stdin.readline().split()))
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]

n = II()

dp = [*range(10**6)]

for i in range(n):
  for j in range(1, 7):
    dp[i+6**j] = min(dp[i+6**j], dp[i]+1)
  for k in range(1, 6):
    dp[i+9**k] = min(dp[i+9**k], dp[i]+1)

print(dp[n])