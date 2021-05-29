from collections import defaultdict
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

N, D = MI()
x,y,z = 0,0,0

while D%2 == 0:
  x += 1
  D //= 2
while D%3 == 0:
  y += 1
  D //= 3
while D%5 == 0:
  z += 1
  D //= 5
if D != 1:
  sys.exit(print(0))


#dp[i][a][b][c] := i回さいころを振ったときに2がa,3がb,5がc個ある確率
dp = [[[[0.0]*(z+1) for _ in range(y+1)] for _ in range(x+1)] for _ in range(N+1)]

dp[0][0][0][0] = 1

for i in range(N):
  for a in range(x+1):
    for b in range(y+1):
      for c in range(z+1):
        prob = dp[i][a][b][c]/6
        dp[i+1][a][b][c] += prob #1が出たときの確率
        dp[i+1][min(a+1, x)][b][c] += prob #2
        dp[i+1][a][min(b+1, y)][c] += prob #3
        dp[i+1][min(a+2, x)][b][c] += prob #4
        dp[i+1][a][b][min(c+1, z)] += prob #5
        dp[i+1][min(a+1, x)][min(b+1, y)][c] += prob #6


print(dp[N][x][y][z])