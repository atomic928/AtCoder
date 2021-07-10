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
plus = 0

for i in range(q):
  t,x,y = MI()
  if t == 1:
    a[(x-plus)%n-1],a[(y-plus)%n-1] = a[(y-plus)%n-1],a[(x-plus)%n-1]
  elif t == 2:
    plus += 1
  else:
    print(a[(x-plus)%n-1])