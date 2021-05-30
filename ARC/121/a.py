import sys
from operator import itemgetter

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
xy = LLI(N)
xdis = [0]*2
ysubd = [0]*2
ydis = [0]*2
xsubd = [0]*2
tyebi = []

xy.sort(key = itemgetter(0), reverse=True)

xdis[0] = abs(xy[0][0]-xy[N-1][0])
ysubd[0] = abs(xy[0][1]-xy[N-1][1])
if abs(xy[0][0]-xy[N-2][0]) > abs(xy[1][0]-xy[N-1][0]):
  xdis[1] = abs(xy[0][0]-xy[N-2][0])
  ysubd[1] = abs(xy[0][1]-xy[N-2][1])
else:
  xdis[1] = abs(xy[1][0]-xy[N-1][0])
  ysubd[1] = abs(xy[1][1]-xy[N-1][1])

tyebi.append(max(xdis[0],ysubd[0]))
tyebi.append(max(xdis[1],ysubd[1]))
xy.sort(key = itemgetter(1), reverse=True)

ydis[0] = abs(xy[0][1]-xy[N-1][1])
xsubd[0] = abs(xy[0][0]-xy[N-1][0])
if abs(xy[0][1]-xy[N-2][1]) > abs(xy[1][1]-xy[N-1][1]):
  ydis[1] = abs(xy[0][1]-xy[N-2][1])
  xsubd[1] = abs(xy[0][0]-xy[N-2][0])
else:
  ydis[1] = abs(xy[1][1]-xy[N-1][1])
  xsubd[1] = abs(xy[1][0]-xy[N-1][0])

tyebi.append(max(ydis[0],xsubd[0]))
tyebi.append(max(ydis[1],xsubd[1]))

if tyebi[0] == tyebi[1] or tyebi[2] == tyebi[3]:
  tyebi.sort(reverse=True)
else:
  tyebi = list(set(tyebi))
  tyebi.sort(reverse=True)
if len(tyebi) == 1:
  print(tyebi[0])
else:
  print(tyebi[1])