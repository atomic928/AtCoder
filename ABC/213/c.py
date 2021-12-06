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

h,w,n = MI()
gyou = []
retu = []

for _ in range(n):
  a,b = MI()
  gyou.append(a)
  retu.append(b)

g_indices = [*range(h)]
r_indices = [*range(w)]
sorted_g_indices = sorted(g_indices,reverse=True, key = lambda i: -gyou[i])
sorted_r_indices = sorted(r_indices,reverse=True, key = lambda i: -retu[i])
sorted_g = [gyou[i] for i in sorted_g_indices]
sorted_r = [retu[i] for i in sorted_r_indices]

for i in range(n):
  