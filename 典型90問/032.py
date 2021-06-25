import sys
from itertools import permutations

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
A = LLI(N)
M = II()

fav = [[1]*N for _ in range(N)]
for _ in range(M):
  x,y = MI()
  fav[x-1][y-1] = fav[y-1][x-1] = 0

ans = 10**18

for i in permutations([*range(N)], N):
  tf = True
  for j in range(N-1):
    if not fav[i[j]][i[j+1]]:
      tf = False
      break

  count = 0
  if tf:
    for j in range(N):
      count += A[i[j]][j]
    ans = min(ans, count)

if ans == 10**18:
  print(-1)
else:
  print(ans)