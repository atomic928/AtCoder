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

x,y,r = MI()
x2,y2,x3,y3 = MI()

#四角の中に〇があるか
if x2 <= x-r and x+r <= x3 and y2 <= y-r and y+r <= y3:
  print("NO")
  print("YES")
  exit()

#逆
dist = [(x2-x)**2+(y2-y)**2, (x2-x)**2+(y3-y)**2, (x3-x)**2+(y2-y)**2, (x3-x)**2+(y3-y)**2]

for i in dist:
  if i > r**2:
    break
else:
  print("YES")
  print("NO")
  exit()

print("YES")
print("YES")
