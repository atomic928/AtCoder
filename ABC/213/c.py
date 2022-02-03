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

from operator import itemgetter
from collections import defaultdict
  
h,w,n = MI()
ab = LLI(n)
ab_c = ab.copy()
row = defaultdict(int)
col = defaultdict(int)

ab_c.sort(key=itemgetter(1))
same = 0
for i in range(n):
  if col[str(ab_c[i][1])] == 0:
    col[str(ab_c[i][1])] = i+1-same
  else:
    same += 1

ab_c.sort(key = itemgetter(0))
same = 0
for i in range(n):
  if row[str(ab_c[i][0])] == 0:
    row[str(ab_c[i][0])] = i+1-same
  else:
    same += 1
for i in range(n):
  print(row[str(ab[i][0])], col[str(ab[i][1])])