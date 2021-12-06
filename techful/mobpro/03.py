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

from itertools import accumulate

E = II()
N = II()
lis = [0]*(E+1)

for i in range(N):
  s,t = MI()
  lis[s] += 1
  lis[t] -= 1
  
lis = list(accumulate(lis))

lis = lis[:-1]
mi = min(lis)

for i in range(E):
  if lis[i] == mi:
    print(i, end= " ")
    