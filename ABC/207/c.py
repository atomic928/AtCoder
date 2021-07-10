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
tln = [list(map(float, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ans = 0

for i in range(N):
  if tln[i][0] == 1:
    continue
  elif tln[i][0] == 2:
    tln[i][2] -= 0.1
  elif tln[i][0] == 3:
    tln[i][1] += 0.1
  else:
    tln[i][1] += 0.1
    tln[i][2] -= 0.1

for i in range(N-1):
  for j in range(i+1, N):
    x1,x2,y1,y2 = tln[i][1],tln[j][1],tln[i][2],tln[j][2]
    if y1 < x2 or y2 < x1:
      continue
    
    ans += 1

print(ans)