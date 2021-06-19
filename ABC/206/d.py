import sys
import bisect

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
a.sort()

c = [0]*n

c[0] = a[0]-1

for i in range(1,n):
  c[i] = c[i-1]+a[i]-a[i-1]-1

for i in range(q):
  k = II()
  if k > c[n-1]:
    print(a[n-1]+k-c[n-1])
  else:
    INDEX = bisect.bisect_left(c,k)
    print(k-c[INDEX]+a[INDEX]-1)