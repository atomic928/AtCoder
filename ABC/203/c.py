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

n,k = MI()
ab = [[0,0]]+LLI(n)
ab.sort(key=itemgetter(0))
ans = 0

for i in range(n):
  if ab[i+1][0]-ab[i][0] <= k:
    ans += ab[i+1][0]-ab[i][0]
    k -= ab[i+1][0]-ab[i][0]
    k += ab[i+1][1]
  else:
    break

ans += k
print(ans)