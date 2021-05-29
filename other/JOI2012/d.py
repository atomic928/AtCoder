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

D, N = MI()
temp = [II() for _ in range(D)]
clothe = LLI(N)
dp = [-1]*101

for i in range(N):
  if clothe[i][0] <= temp[0] <= clothe[i][1]:
    dp[i] = 0

for t in temp[1:]:
  ndp = [0]*101
  for i in range(1,N):
    if clothe[i][0] <= t <= clothe[i][1]:
      for j in range(101):
        if dp[j] == -1:
          continue
        ndp[clothe[i][2]] = max(ndp[clothe[i][2]], dp[])
