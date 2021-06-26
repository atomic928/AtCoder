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

from collections import defaultdict

N,K = MI()
A = LI()

check = defaultdict(int)
start = 0
ans = 0

for stop in range(N):
  check[A[stop]] += 1
  while 1:
    if len(check) <= K:
      break
    check[A[start]] -= 1
    start += 1
    if check[A[start-1]] == 0:
      del check[A[start-1]]
  ans = max(ans, stop-start+1)

print(ans)