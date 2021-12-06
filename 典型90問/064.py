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

n,q = MI()
a = LI()
e = []
ans = 0

for i in range(n-1):
  e.append(a[i]-a[i+1])
  ans += abs(a[i]-a[i+1])

for i in range(q):
  l,r,v = MI()
  if l != 1 and r!= n:
    pre = abs(e[l-2])+abs(e[r-1])
  elif l != 1:
    pre = abs(e[l-2])
  elif r != n:
    pre = abs(e[r-1])
  else:
    pre = 0
  if l != 1:
    e[l-2] -= v
  if r != n:
    e[r-1] += v
  if l!= 1 and r != n:
    crr = abs(e[l-2])+abs(e[r-1])
  elif l!=1:
    crr = abs(e[l-2])
  elif r!=n:
    crr = abs(e[r-1])
  else:
    crr = 0
  
  ans += crr-pre
  print(ans)

