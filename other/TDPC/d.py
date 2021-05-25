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


dp = defaultdict(int)
dp[(0,0,0)] = 1
print(dp)