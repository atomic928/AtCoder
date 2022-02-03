import sys

#input()
def I(): return sys.stdin.readline().rstrip()
#list(input())
def SI(): return list(I())
#int(input())
def II(): return int(I())
#map(int,input().split())
def MI(): return map(int, I().split())
#map(str, input().split())
def MS(): return map(str, I().split())
#list(map(int,input().split()))
def LI(): return list(MI())
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]
#文字の行列
def LSI(rows_number): return [SI() for _ in range(rows_number)]

n, m = MI()
a = LLI(m)
stair = [1]*n
dp = [0]*n

for i in a:
  stair[i[0]-1] = 0
  
if stair[0]:
  dp[0] = 1
if n > 1:
  if stair[1]:
    dp[1] = 1
  if stair[0] and stair[1]:
    dp[1] = 2

for i in range(n-2):
  dp[i+2] = dp[i+1]*stair[i+1] + dp[i]*stair[i]
 
print(dp[n-1]%(10**9+7))
