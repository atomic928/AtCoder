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

n, k = MI()
h = LI() + [10**10]*101

dp = [10**10]*10**6
dp[0] = 0

#iから行ける場所はk個ある
for i in range(n):
  for j in range(1, k+1):
    dp[i+j] = min(dp[i+j], dp[i]+abs(h[i]-h[i+j]))

print(dp[n-1])