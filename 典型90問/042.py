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

K = II()
dp = [0]*(K+1)

if K%9 != 0:
  sys.exit(print(0))

dp[0] = 1

for i in range(K):
  roup = min(i+1, 9)
  for j in range(roup):
    dp[i+1] += dp[i-j]%(10**9+7)

print(dp[K]%(10**9+7))