import sys
from itertools import accumulate

#input()
def I(): return sys.stdin.readline()
#int(input())
def II(): return int(sys.stdin.readline())
#map(int,input().split())
def MI(): return map(int, sys.stdin.readline().split())
#list(map(int,input().split()))
def LI(): return list(map(int, sys.stdin.readline().split()))
#行列
def LLI(rows_number): return [LI() for _ in range(rows_number)]

n = II()
a = LI()

mx = [0]*n
mx[0] = a[0]

aacu = list(accumulate(accumulate(a)))

for i in range(1, n):
  mx[i] = max(mx[i-1], a[i])

for i in range(n):
  ans = aacu[i]+mx[i]*(i+1)
  print(ans)