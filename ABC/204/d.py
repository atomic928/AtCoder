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
T = LI()
SUM = sum(T)

if N == 1:
  print(T[0])

#部分和dp
dp = [[0]*(SUM//2+1) for _ in range(N+1)]

for i in range(N):
  if T[i] < SUM//2+1:
    dp[i+1][T[i]] = 1
  for j in range(SUM//2+1):
    if dp[i][j]: 
      dp[i+1][j] = 1
      if j + T[i] < SUM//2+1:
        dp[i+1][j+T[i]] = 1


for i in range(SUM//2+1):
  if dp[N][-1-i]:
    print(SUM-SUM//2+i)
    exit()